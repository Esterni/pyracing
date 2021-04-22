from pyracing import constants as ct

from pyracing import logger
from pyracing.helpers import now_five_min_floor
from pyracing.response_objects import (
    career_stats,
    chart_data,
    historical_data,
    iracing_data,
    session_data,
    upcoming_events,
    league_data
)
from .exceptions.authentication_error import AuthenticationError

from datetime import datetime
import httpx
import time


# This module authenticates a session, builds a URL query from parameters,
# and parses returned data into instanced objects from iRacing endpoints.
# Each method contains all **known** paramaters available for an endpoint.
# Cookies are handled by the httpx module behind the scenes and are not
# written to file.

# Authentication happens automatically on the first method call from Client().
# When a request fails from an expired cookie, a re-auth is triggered and
# the last request that failed is tried again.


class Client:
    def __init__(self, username: str, password: str):
        """ This class is used to interact with all iRacing endpoints that
        have been discovered so far. After creating an instance of Client
        it is required to call authenticate(), due to async limitations.

        An alternative to storing credentials as string in the class arguments
        is to store then in your OS environment and call with os.getenv().
        """
        self.username = username
        self.password = password
        self.session = httpx.AsyncClient()

    async def _authenticate(self):
        """ Sends a POST request to iRacings login server, initiating a
        persistent connection stored in self.session
        """
        logger.info('Authenticating...')

        login_data = {
            'username': self.username,
            'password': self.password,
            'utcoffset': round(abs(time.localtime().tm_gmtoff / 60)),
            'todaysdate': ''  # Unknown purpose, but exists as a hidden form.
        }

        auth_response = await self.session.post(ct.URL_LOGIN2, data=login_data)

        if 'failedlogin' in str(auth_response.url):
            logger.warning(
                'The login POST request was redirected to /failedlogin, '
                'indicating an authentication failure. If credentials are '
                'correct, check that a captcha is not required by manually '
                'visiting members.iracing.com')
            raise AuthenticationError('Login Failed', auth_response)
        else:
            logger.info('Login successful')

    async def _build_request(self, url, params):
        """ Builds the final GET request from url and params
        """
        if not self.session.cookies.__bool__():
            logger.info("No cookies in cookie jar.")
            await self._authenticate()

        logger.info(f'Request being sent to: {url} with params: {params}')

        response = await self.session.get(
            url,
            params=params,
            allow_redirects=False,
            timeout=10.0
        )
        logger.info(f'Request sent for URL: {response.url}')
        logger.info(f'Status code of response: {response.status_code}')
        logger.debug(f'Contents of the response object: {response.__dict__}')

        if response.is_error or response.is_redirect:
            logger.info(
                'Request was redirected, indicating that the cookies are '
                'invalid. Initiating authentication and retrying the request.'
            )
            await self._authenticate()
            return await self._build_request(url, params)

        return response

    async def active_op_counts(
            self,
            count_max=250,
            include_empty='n',
            cust_id=None
    ):
        """ Returns session information for all 'open practice' sessions that
        are currently active. By default this only includes sessions with
        registered drivers. Use include_empty flag to see all sessions.
        """
        url = ct.URL_ACTIVEOP_COUNT
        payload = {
            'custid': cust_id,  # Purpose of cust_id unknown
            'maxcount': count_max,
            'include_empty': include_empty,
            'excludeLite': None  # Purpose of excludeLite unknown
        }
        response = await self._build_request(url, payload)

        return [upcoming_events.OpenPractice(x) for x in response.json()["d"]]

    async def all_subsessions(self, subsession_id):
        """ If the given SubSessionID is one of many race splits, this
        returns the SubSessionID for each additional split.
        """
        payload = {'subsessionid': subsession_id}
        url = ct.URL_ALL_SUBSESSIONS
        response = await self._build_request(url, payload)
        return [x['subsessionid'] for x in response.json()]

    async def car_class(self, car_class_id=0):
        """ Returns the CarClass data for the associated car_class_id

        The default "0" is a "master" CarClass containing a list of CarClass
        names and their respective car_class_id.
        """
        payload = {'carclassid': car_class_id}
        url = ct.URL_CAR_CLASS

        response = await self._build_request(url, payload)

        # Returns a single dictionary
        return iracing_data.CarClass(response.json()['carclass'])

    async def career_stats(self, cust_id):
        """ Returns driver career stats as seen on the driver profile page.\n
        E.g. Starts, Avg Inc., Win %, etc.
        """
        payload = {'custid': cust_id}
        url = ct.URL_CAREER_STATS
        response = await self._build_request(url, payload)

        if not response.json():
            return []

        return [career_stats.CareerStats(x) for x in response.json()]

    async def current_seasons(
            self,
            only_active=True,
            series_name_short=True,
            cat_id=True,
            season_id=True,
            year=True,
            quarter=True,
            series_id=True,
            active=True,
            license_eligible=True,
            is_lite=True,
            car_classes=True,
            tracks=True,
            start=True,
            end=True,
            cars=True,
            race_week=True,
            category=True,
            series_lic_group_id=True,
            car_id=True
    ):
        """ Returns data about all SeasonIDs. A SeasonID is unique to a series
        for a specific year:quarter, so in 1 year a series will have gone
        through 4 different SeasonIDs.

        only_active is a flag to return results of only the currently running
        series. The remaining kwargs change which fields are returned for each
        SeasonID. Setting only 'category' and 'only_active' to True will give
        you *only* a list of items with a single number between 1 and 4
        indicating Road, Oval, Dirt Road, Dirt Oval, respectively.
        """
        field_dict = {
            'year': year,
            'quarter': quarter,
            'seriesshortname': series_name_short,
            'seriesid': series_id,
            'active': active,
            'catid': cat_id,
            'licenseeligible': license_eligible,
            'islite': is_lite,
            'carclasses': car_classes,
            'tracks': tracks,
            'start': start,
            'end': end,
            'cars': cars,
            'raceweek': race_week,
            'category': category,
            'serieslicgroupid': series_lic_group_id,
            'carid': car_id,
            'seasonid': season_id,
        }
        # Adds the key name to key_list if set to True
        key_list = [key for key in field_dict if field_dict.get(key)]

        # iRacing accepts these as a single, comma seperated, parameter
        key_list = ','.join(key_list)

        payload = {
            'onlyActive': 1 if only_active else 0,
            'fields': key_list
        }
        url = ct.URL_CURRENT_SEASONS
        response = await self._build_request(url, payload)

        return [iracing_data.Season(x) for x in response.json()]

    async def driver_stats(
            self,
            search='null',
            country='null',
            category=ct.Category.road.value,
            class_low=None,
            class_high=None,
            irating_low=None,
            irating_high=None,
            ttrating_low=None,
            ttrating_high=None,
            starts_avg_low=None,
            starts_avg_high=None,
            finish_avg_low=None,
            finish_avg_high=None,
            points_avg_low=None,
            points_avg_high=None,
            inc_avg_low=None,
            inc_avg_high=None,
            result_num_low=1,
            result_num_high=25,
            sort=ct.Sort.irating.value,
            order=ct.Sort.descending.value,
            active=1,
            friend=None,
            watched=None,
            recent=None,
            cust_id=None  # Does not appear to affect results
    ):
        """ Returns a list of drivers that match the given parameters.
        This is the backend source for /DriverLookup.Do AKA 'Driver Stats.'

        This function can be used to search drivers by name using the search=
        field and entering their full driver name. custid is only used for
        showing where you are in relation to the list of drivers when using
        the main /DriverLookup page on iRacing.
        """
        payload = {
            'search': search,
            'friend': friend,
            'watched': watched,
            'recent': recent,
            'country': country,
            'category': category,
            'classlow': class_low,
            'classhigh': class_high,
            'iratinglow': irating_low,
            'iratinghigh': irating_high,
            'ttratinglow': ttrating_low,
            'ttratinghigh': ttrating_high,
            'avgstartlow': starts_avg_low,
            'avgstarthigh': starts_avg_high,
            'avgfinishlow': finish_avg_low,
            'avgfinishhigh': finish_avg_high,
            'avgpointslow': points_avg_low,
            'avgpointshigh': points_avg_high,
            'avgincidentslow': inc_avg_low,
            'avgincidentshigh': inc_avg_high,
            'custid': cust_id,
            'lowerbound': result_num_low,
            'upperbound': result_num_high,
            'sort': sort,
            'order': order,
            'active': active
        }
        url = ct.URL_DRIVER_STATS
        response = await self._build_request(url, payload)

        return [historical_data.DriverStats(x) for
                x in response.json()["d"]["r"]]

    async def event_results(
            self,
            cust_id,
            quarter,
            show_races=1,
            show_quals=None,
            show_tts=None,
            show_ops=None,
            show_official=1,
            show_unofficial=None,
            show_rookie=1,
            show_class_d=1,
            show_class_c=1,
            show_class_b=1,
            show_class_a=1,
            show_pro=1,
            show_prowc=1,
            result_num_low=1,
            result_num_high=25,
            sort=ct.Sort.start_time.value,
            order=ct.Sort.descending.value,
            data_format='json',
            category=ct.Category.road.value,
            year=datetime.today().year,
            race_week=None,
            track_id=None,
            car_class=None,
            car_id=None,
            start_low=None,
            start_high=None,
            finish_low=None,
            finish_high=None,
            incidents_low=None,
            incidents_high=None,
            points_champ_low=None,
            points_champ_high=None
    ):
        """ Returns a list with an EventResults object for each of a driver's
        past events that meet the selected criteria. Default is to show the
        last 25 official road races, sorted by most recent as first result.
        """
        payload = {
            'custid': cust_id,
            'showraces': show_races,
            'showquals': show_quals,
            'showtts': show_tts,
            'showops': show_ops,
            'showofficial': show_official,
            'showunofficial': show_unofficial,
            'showrookie': show_rookie,
            'showclassd': show_class_d,
            'showclassc': show_class_c,
            'showclassb': show_class_b,
            'showclassa': show_class_a,
            'showpro': show_pro,
            'showprowc': show_prowc,
            'lowerbound': result_num_low,
            'upperbound': result_num_high,
            'sort': sort,
            'order': order,
            'format': data_format,
            'category[]': category,
            'seasonyear': year,
            'seasonquarter': quarter,
            'raceweek': race_week,
            'trackid': track_id,
            'carclassid': car_class,
            'carid': car_id,
            'start_low': start_low,
            'start_high': start_high,
            'finish_low': finish_low,
            'finish_high': finish_high,
            'incidents_low': incidents_low,
            'incidents_high': incidents_high,
            'champpoints_low': points_champ_low,
            'champpoints_high': points_champ_high
        }
        url = ct.URL_RESULTS
        response = await self._build_request(url, payload)

        event_result_dict = response.json()['d']
        if event_result_dict:
            return [historical_data.EventResults(x)
                    for x in response.json()["d"]["r"]]
        else:
            return []

    async def irating(self, cust_id, category) -> \
            chart_data.ChartData[chart_data.IRating]:
        """ Utilizes the stats_chart class to return a list of iRating values
        that are used in the /CareerStats charts. Accessing
        get_irating().current() will give the most recent irating of a cust_id
        """
        chart_type = ct.ChartType.irating.value
        response = await self._stats_chart(cust_id, category, chart_type)
        ir_list = []
        for irating in response.json():
            ir_list.append(
                chart_data.IRating(timestamp=irating[0], value=irating[1])
            )

        return chart_data.ChartData(
            category=category,
            type=chart_type,
            content=ir_list)

    async def ttrating(self, cust_id, category) -> \
            chart_data.ChartData[chart_data.TTRating]:
        """ Utilizes the stats_chart class to return a list of ttrating values
        that are used in the /CareerStats charts.
        """
        chart_type = ct.ChartType.ttrating.value
        response = await self._stats_chart(cust_id, category, chart_type)

        ttrating_list = []
        for ttrating in response.json():
            ttrating_list.append(
                chart_data.TTRating(timestamp=ttrating[0], value=ttrating[1])
            )

        return chart_data.ChartData(
            category=category,
            type=chart_type,
            content=ttrating_list)

    async def license_class(self, cust_id, category) -> \
            chart_data.ChartData[chart_data.LicenseClass]:
        """ Utilizes the stats_chart class to return a list of license values
        that are used in the /CareerStats charts. See the LicenseClass class
        for how to further use this data.
        """
        chart_type = ct.ChartType.license_class.value
        response = await self._stats_chart(cust_id, category, chart_type)

        license_class_list = []
        for license_class in response.json():
            license_class_list.append(
                chart_data.LicenseClass(
                    timestamp=license_class[0], license_number=license_class[1]
                ))

        return chart_data.ChartData(
            category=category,
            type=chart_type,
            content=license_class_list)

    async def _stats_chart(self, cust_id, category, chart_type):
        """ Returns a list in the form of time:value for the race category
        specified. chart_type changes values between iRating, ttRating, or
        Safety Rating. Category chooses 1 of the 4 disciplines.
        *NOTE* if you are using this, you should use `irating`, `ttrating`
        or `license_class` instead. This is used by those methods for the
        specific types of each of them.
        """
        payload = {
            'custId': cust_id,
            'catId': category,
            'chartType': chart_type
        }
        url = ct.URL_STATS_CHART
        return await self._build_request(url, payload)

    async def last_races_stats(self, cust_id):
        """ Returns stat summary for the driver's last 10 races as seen
        on the /CareerStats page.
        """
        payload = {'custid': cust_id}
        url = ct.URL_LASTRACE_STATS
        response = await self._build_request(url, payload)

        if not response.json():
            return []

        return [career_stats.LastRacesStats(x) for x in response.json()]

    async def last_series(self, cust_id):
        """ Returns a summary of stats about a driver's last 3 series as seen
        on the /CareerStats page.
        """
        payload = {'custid': cust_id}
        url = ct.URL_LAST_SERIES
        response = await self._build_request(url, payload)

        return [career_stats.LastSeries(x) for x in response.json()]

    async def member_cars_driven(self, cust_id):
        """ Returns which cars (car_id) someone has driven.
        """
        payload = {'custid': cust_id}
        url = ct.URL_CARS_DRIVEN
        response = await self._build_request(url, payload)
        return response.json()

    async def member_division(self, cust_id, season_id):
        """ Returns which division the driver was in for the
        specified season_id.
        """
        payload = {
            'seasonid': season_id,
            'custid': cust_id,
            'pointstype': 'race'
        }
        url = ct.URL_MEM_DIVISION
        response = await self._build_request(url, payload)

        return [iracing_data.MemberDivision(x) for x in response.json()]

    async def member_subsession_id_from_session(self, cust_id, session_id):
        """ Returns which SubSession ID that a member was
        in from a given Session ID.
        """
        payload = {'custid': cust_id, 'sessionID': session_id}
        url = ct.URL_MEM_SUBSESSID
        response = await self._build_request(url, payload)
        return response.json()

    async def driver_status(
            self,
            search_terms='null'
    ):
        """ Returns information about the member's current status. If logged
        in while also providing your custid, it will return the same info for
        your friends along with studied, and blacklisted drivers.
        """
        payload = {
            'searchTerms': search_terms
        }
        url = ct.URL_DRIVER_STATUS
        response = await self._build_request(url, payload)
        return [iracing_data.DriverStatus(x) for
                x in response.json()["searchRacers"]]

        #return response.json()["searchRacers"]

    async def next_event(
            self,
            series_id,
            event_type=ct.EventType.race.value,
            date=now_five_min_floor()
    ):
        """ Returns information about the next event (from the requested time)
        for the series_id.
        """
        payload = {
            'seriesID': series_id,
            'evtType': event_type,
            'date': date
        }
        url = ct.URL_NEXT_EVENT
        response = await self._build_request(url, payload)

        return upcoming_events.NextEvent(response.json())

    async def next_session_times(self, season_id):
        """ Returns the next 5 sessions with all of their attributes:\n
        starttime, registered drivers, session parameters, etc.
        """
        payload = {'season': season_id}
        url = ct.URL_SESSION_TIMES
        response = await self._build_request(url, payload)

        return [upcoming_events.NextSessionTimes(x) for
                x in response.json()["d"]["r"]]

    async def personal_bests(self, cust_id, car_id):
        """ Returns the drivers best laptimes for the given car_id, as seen on
        the /CareerStats page.
        """
        payload = {'custid': cust_id, 'carid': car_id}
        url = ct.URL_PERSONAL_BESTS
        response = await self._build_request(url, payload)

        return [career_stats.PersonalBests(x) for x in response.json()]

    async def private_results(
            self,
            cust_id,
            start_time_lower,
            start_time_upper,
            result_num_low=1,
            result_num_high=25,
            sort=ct.Sort.session_name.value,
            order=ct.Sort.ascending.value
    ):
        """ Returns private sessions that the driver
        has participated in.
        """
        payload = {
            'participant_custid': cust_id,
            'start_time_lowerbound': start_time_lower,
            'start_time_upperbound': start_time_upper,
            'lowerbound': result_num_low,
            'upperbound': result_num_high,
            'sort': sort,
            'order': order
        }
        url = ct.URL_PRIVATE_RESULTS
        response = await self._build_request(url, payload)

        return [historical_data.PrivateResults(x) for
                x in response.json()['rows']]

    async def race_guide(
            self,
            rookie=None,
            class_d=None,
            class_c=None,
            class_b=None,
            class_a=None,
            class_pro=None,
            class_prowc=None,
            oval=None,
            road=None,
            dirt_oval=None,
            dirt_road=None,
            fixed=None,
            multiclass=None,
            meets_mpr=None,
            populated=None,
            eligible=None,
            official=None,
            time=now_five_min_floor()
    ):
        """ Returns all data used by the race guide. Filters are identical
        to those found when visiting the race guide with a browser.
        """
        payload = {
            'at': time,
            'showRookie': rookie,
            'showClassD': class_d,
            'showClassC': class_c,
            'showClassB': class_b,
            'showClassA': class_a,
            'showPro': class_pro,
            'showProWC': class_prowc,
            'showOval': oval,
            'showRoad': road,
            'showDirtOval': dirt_oval,
            'showDirtRoad': dirt_road,
            'hideNotFixedSetup': fixed,
            'hideNotMultiClass': multiclass,
            'meetsMPR': meets_mpr,
            'hideUnpopulated': populated,
            'hideIneligible': eligible,
            'showOfficial': official
        }
        url = ct.URL_RACEGUIDE
        response = await self._build_request(url, payload)

        return [upcoming_events.RaceGuide(x) for
                x in response.json()['series']]

    async def race_laps_all(
            self,
            subsession_id,
            car_class_id=None,
            sim_session_type=ct.SimSessionType.race.value
    ):
        """ Returns information about all laps of a race for *every*
        driver. The class of car can be set for multiclass races.

        To specify laps of a single driver, use race_laps_driver().
        """
        payload = {
            'subsessionid': subsession_id,
            'carclassid': car_class_id,
            'simsesnum': sim_session_type
        }
        url = ct.URL_LAPS_ALL
        response = await self._build_request(url, payload)

        return session_data.RaceLapsAll(response.json())

    async def race_laps_driver(
            self,
            cust_id,
            subsession_id,
            sim_session_type=ct.SimSessionType.race.value
    ):
        """ Returns data for all laps completed of a single driver.
        sim_sess_id specifies the laps from practice, qual, or race.
        """
        payload = {
            'subsessionid': subsession_id,
            'simsessnum': sim_session_type,
            'groupid': cust_id
        }
        url = ct.URL_LAPS_SINGLE
        response = await self._build_request(url, payload)

        return session_data.RaceLapsDriver(response.json())

    async def season_from_session(self, session_id):
        """ Returns the season_id for a given session_id. That is this
        endpoints only purpose.
        """
        payload = {'sessionID': session_id}
        url = ct.URL_SEASON_FOR_SESSION
        response = await self._build_request(url, payload)
        return response.json()

    async def season_standings(
            self,
            season_id,
            race_week=1,
            car_class_id=None,
            club_id=None,
            division=None,
            result_num_low=1,
            result_num_high=25,
            sort=ct.Sort.champ_points.value,
            order=ct.Sort.descending.value
    ):
        """ Returns the championship point standings of a series.
        This is the same data found in /statsseries.jsp.
        """
        payload = {
            'seasonid': season_id,
            'carclassid': car_class_id,
            'clubid': club_id,
            # -1 for all weeks, or the week number to get a specific week.
            # 0 indexed in iRacing, so the user passes the week number and we
            # subtract one to get the 0 indexed position
            'raceweek': race_week if race_week == -1 else race_week - 1,
            'division': division,
            'start': result_num_low,
            'end': result_num_high,
            'sort': sort,
            'order': order
        }

        url = ct.URL_SEASON_STANDINGS
        response = await self._build_request(url, payload)

        return [historical_data.SeasonStandings(x) for
                x in response.json()["d"]["r"]]

    async def series_race_results(self, season_id, race_week=1):
        """ Returns the race results for a season_id. race_week can be
        specified to reduce the size of data returned.
        """
        payload = {
            'seasonid': season_id,
            # subtracts 1 so that entering 1 returns W1 instead of W2.
            # Does not accept a 'show all' value of -1 as others might
            'raceweek': race_week - 1
        }
        url = ct.URL_SERIES_RACERESULTS
        response = await self._build_request(url, payload)

        return [historical_data.SeriesRaceResults(x) for
                x in response.json()['d']]

    async def subsession_data(self, subsession_id, cust_id=None):
        """ Returns extensive data about a session. This endpoint contains
        data points about a session that are unavailable anywhere else.
        """
        payload = {
            'subsessionID': subsession_id,
            'custid': cust_id
        }
        url = ct.URL_SUBS_RESULTS
        response = await self._build_request(url, payload)

        # Returns a single dictionary
        return session_data.SubSessionData(response.json())

    # TODO Be bothered to finish this one
    async def team_standings(
            self,
            season_id,
            car_class_id,
            car_id=None,
            race_week=None
    ):
        """ Returns championship point standings of Teams.
        """
        payload = {
            'raceWeekNum': race_week,
            'seasonid': season_id,
            'carClassId': car_class_id,
            'carId': car_id
        }
        url = ct.URL_SUBS_RESULTS
        return await self._build_request(url, payload)

    # TODO Does not return JSON format. Find how to convert.
    async def total_registered_all(self):
        """ Returns a list of every upcoming session and the number of
        drivers that have registered. This data is used in the small text
        next to each series name in /Series.do that shows number of registered
        drivers for that series.
        """
        payload = {}
        url = ct.URL_TOTALREGISTERED
        response = await self._build_request(url, payload)

        return [upcoming_events.TotalRegistered(x) for x in response.json()]

    async def world_records(
            self,
            year,
            quarter,
            car_id,
            track_id,
            result_num_low=1,
            result_num_high=25,
            cust_id=None
    ):
        """ Returns laptimes with the requested paramaters. Filters can also
        be seen on the /worldrecords.jsp page on the membersite.
        """
        payload = {
            'seasonyear': year,
            'seasonquarter': quarter,
            'carid': car_id,
            'trackid': track_id,
            'custid': cust_id,
            'format': 'json',
            'lowerbound': result_num_low,
            'upperbound': result_num_high
        }
        url = ct.URL_WORLD_RECORDS
        response = await self._build_request(url, payload)

        return [historical_data.WorldRecords(x) for
                x in response.json()["d"]["r"]]

    async def yearly_stats(self, cust_id):
        """ Returns the breakdown of career stats by year, as seen on the
        /CareerStats driver profile.
        """
        payload = {'custid': cust_id}
        url = ct.URL_YEARLY_STATS
        response = await self._build_request(url, payload)

        if not response.json():
            return []

        return [career_stats.YearlyStats(x) for x in response.json()]

    async def league(self, league_id):
        """Get details about a given league"""
        payload = {
            'leagueid': league_id
        }
        url = ct.URL_LEAGUE
        response = await self._build_request(url, payload)

        # -1 cust_id means it could not be found
        if not response.json() or response.json()['custID'] == -1:
            return None

        return league_data.League(response.json())

    async def league_standings(self, league_id, league_season_id):
        """Get the standings for a league in a given season"""
        payload = {
            'leagueID': league_id,
            'leagueSeasonID': league_season_id
        }
        url = ct.URL_LEAGUE_SEASON_STANDINGS
        response = await self._build_request(url, payload)

        if not response.json():
            return []

        return league_data.SeasonStandings(response.json())

    async def league_seasons(self, league_id):
        """Get the season for a league"""
        payload = {'leagueID': league_id}

        url = ct.URL_LEAGUE_SEASONS
        response = await self._build_request(url, payload)

        if not response.json() or not response.json()['d']:
            return []

        return [league_data.LeagueSeason(x) for x in response.json()['d']['r']]
