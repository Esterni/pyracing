from . import constants as ct
# Imports CareerStats, YearlyStats, LastRaceStats, LastSeries, Personal Bests.
from .response_objects.career_stats import *
# Imports ChartData, IRating, TTRating, and LicenseClass
from .response_objects.chart_data import *

from .response_objects.iracing_data import *

import logging
import httpx
import sys
import time


# This module authenticates, builds, and sends url queries to iRacing.
# Each function is set with only the variables required, for the respective
# endpoint, to return the desired data.  Compared to the previous client.py,
# this module does not attempt to parse any of the data received.  Instead,
# each function returns the response object from httpx.AsyncClient() to
# provide more versatility from a function.

# Response objects include the .json() method, which is the same result
# that was found in util.py as parse().  Since new endpoints have been found,
# there is no longer a need for regex, drastically reducing the complexity
# of the code.

# Cookies are handled by the Session() object behind the scenes. Cookies are
# not written to file. If a session is closed, you must re-authenticate with
# the self.authenticate() method.


def default_logger():
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(asctime)s;%(levelname)s;%(message)s"
    )
    return logging.getLogger()


class Client:
    def __init__(self, username: str, password: str, log=default_logger()):
        """ This class is used to interact with all iRacing endpoints that
        have been discovered so far. After creating an instance of Client
        it is required to call authenticate(), due to async limitations.

        An alternative to storing credentials as string in the class arguments
        is to store then in your OS environment and call with os.getenv().
        """
        self.username = username
        self.password = password
        self.session = httpx.AsyncClient()
        self.log = log

    async def authenticate(self):
        """ Sends a POST request to iRacings login server, initiating a
        persistent connection stored in self.session
        """
        self.log.info('Authenticating...')

        login_data = {
            'username': self.username,
            'password': self.password,
            'utcoffset': round(abs(time.localtime().tm_gmtoff / 60)),
            'todaysdate': ''  # Unknown purpose, but present as a hidden form.
        }

        auth_post = await self.session.post(ct.URL_LOGIN2, data=login_data)

        if 'failedlogin' in str(auth_post.url):
            self.log.warning('Login Failed. Please check credentials')
            raise UserWarning(
                'The login POST request was redirected to /failedlogin, '
                'indicating an authentication failure. If credentials are '
                'correct, check that a captcha is not required by manually '
                'visiting members.iracing.com'
                )
        else:
            self.log.info('Login successful')

    # Wrapper for all functions that builds the final self.session.get()

    async def build_request(self, url, params):
        """ Builds the final GET request from url and params
        """
        self.log.info(f'Request being sent to: {url} with params: {params}')
        response = await self.session.get(
            url,
            params=params,
            allow_redirects=False
            )
        self.log.info(f'Request sent for URL: {response.url}')
        self.log.info(f'Status code of response: {response.status_code}')
        self.log.debug(f'Contents of the response object: {response.__dict__}')

        # Status code other than 200 assumes redirect to a failed auth page
        if not response.status_code == 200:
            self.log.info(
                'Request was redirected, indicating that the cookies are '
                'invalid. Initiating authentication and retrying the request.'
                )
            await self.authenticate()
            return await self.build_request(url, params)

        return response

    async def active_op_counts(
        self,
        maxCount=250,
        include_empty='n',  # This should be the string 'n' or 'y'
        custID=None
    ):
        """ Returns session information for all 'open practice' sessions that
        are currently active. By default this only includes sessions with
        registered drivers.
        """
        url = ct.URL_ACTIVEOP_COUNT
        payload = {
            'custid': custID,  # Purpose of custID unknown
            'maxcount': maxCount,
            'include_empty': include_empty,
            'excludeLite': None  # Purpose of excludeLite unknown
        }
        return await self.build_request(url, payload)

    async def all_subsessions(self, sub_sess_id):
        """ If the given SubSessionID is one of many race splits, this
        returns the SubSessionID for each additional split.
        """
        payload = {'subsessionid': sub_sess_id}
        url = ct.URL_ALL_SUBSESSIONS
        return await self.build_request(url, payload)

    async def car_class_by_id(self, carClassID):
        """ Returns the CarClass data for the associated carClassID

        Use id "0" for a "master" CarClass containing a list of CarClass
        names and their respective carClassID.
        """
        payload = {'carclassid': carClassID}
        url = ct.URL_CAR_CLASS
        return await self.build_request(url, payload)

    async def career_stats(self, custID):
        """ Returns driver career stats as seen on the driver profile page.\n
        E.g. Starts, Avg Inc., Win %, etc.
        """
        payload = {'custid': custID}
        url = ct.URL_CAREER_STATS
        response = await self.build_request(url, payload)

        if not response.json():
            return []

        return [CareerStats(x) for x in response.json()]

    async def current_seasons(
            self,
            only_active=True,  # Returns only seasons that are active
            series_short_name=True,
            cat_id=True,
            season_id=True,
            year=False,
            quarter=False,
            series_id=False,
            active=False,  # Field that indicates if season is active or not
            license_eligible=False,
            is_lite=False,
            car_classes=False,
            tracks=False,
            start=False,
            end=False,
            cars=False,
            race_week=False,
            category=False,
            series_lic_group_id=False,
            car_id=False
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
        # This is a single query string; Setting to False removes it.
        field_dict = {
            'year': year,
            'quarter': quarter,
            'seriesshortname': series_short_name,
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

        key_list = self.key_list_from_dict(field_dict)

        payload = {
            'onlyActive': 1 if only_active else 0,
            'fields': (','.join(key_list))
        }
        url = ct.URL_CURRENT_SEASONS
        response = await self.build_request(url, payload)
        return [Season(x) for x in response.json()]

    # TODO Use *kwargs with dictionary for default values? Very long list.

    async def driver_stats(
            self,
            custid,
            search='null',
            friend=-1,
            watched=-1,
            recent=-1,
            country='null',
            category=ct.Category.road,
            class_low=-1,
            class_high=-1,
            irating_low=-1,
            irating_high=-1,
            ttrating_low=-1,
            ttrating_high=-1,
            avg_start_low=-1,
            avg_start_high=-1,
            avg_finish_low=-1,
            avg_finish_high=-1,
            avg_points_low=-1,
            avg_points_high=-1,
            avg_inc_low=-1,
            avg_inc_high=-1,
            lower_bound=1,
            upper_bound=25,
            sort=ct.Sort.irating,
            order=ct.Sort.descending,
            active=1
    ):
        """ Returns a list of drivers that match the given parameters.
        This is the backend source for /DriverLookup.Do AKA 'Driver Stats.'

        This function can be used to search drivers by name using the search=
        field and entering their full driver name. custid is only used for
        showing where you are in relation to the list of drivers when using
        the main /DriverLookup page on iRacing.  """
        payload = {
            'search': str(search).replace(' ', '+'),
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
            'avgstartlow': avg_start_low,
            'avgstarthigh': avg_start_high,
            'avgfinishlow': avg_finish_low,
            'avgfinishhigh': avg_finish_high,
            'avgpointslow': avg_points_low,
            'avgpointshigh': avg_points_high,
            'avgincidentslow': avg_inc_low,
            'avgincidentshigh': avg_inc_high,
            'custid': custid,
            'lowerbound': lower_bound,
            'upperbound': upper_bound,
            'sort': sort,
            'order': order,
            'active': active
        }
        url = ct.URL_DRIVER_STATS
        return await self.build_request(url, payload)

    # TODO Find query string parameters for this url

    async def hosted_results(
            self,
            custid,
            start_time_lower,
            start_time_upper,
            lower_bound=1,
            upper_bound=25,
            sort=ct.Sort.session_name,
            order=ct.Sort.ascending
    ):
        """ Returns private sessions that the driver
        has participated in.
        """
        payload = {
            'participant_custid': custid,
            'start_time_lowerbound': start_time_lower,
            'start_time_upperbound': start_time_upper,
            'lowerbound': lower_bound,
            'upperbound': upper_bound,
            'sort': sort,
            'order': order
        }
        url = ct.URL_HOSTED_RESULTS
        return await self.build_request(url, payload)

    async def last_race_stats(self, custID):
        """ Returns stat summary for the driver's last 10 races as seen
        on the /CareerStats page.
        """
        payload = {'custid': custID}
        url = ct.URL_LASTRACE_STATS
        response = await self.build_request(url, payload)

        if not response.json():
            return []

        return [LastRaceStats(x) for x in response.json()]

    async def last_series(self, custID):
        """ Returns a summary of stats about a driver's last 3 series as seen
        on the /CareerStats page.
        """
        payload = {'custid': custID}
        url = ct.URL_LAST_SERIES
        return await self.build_request(url, payload)

    async def member_cars_driven(self, custID):
        """ Returns which cars (carID) someone has driven.
        """
        payload = {'custid': custID}
        url = ct.URL_CARS_DRIVEN
        return await self.build_request(url, payload)

    async def member_division(self, seasonID, custID):
        """ Returns which division the driver was in for the
        specified seasonID.
        """
        payload = {
            'seasonid': seasonID,
            'custid': custID,
            'pointstype': 'race'
        }
        url = ct.URL_MEM_DIVISION
        return await self.build_request(url, payload)

    async def member_sub_id_from_session(self, sessNum, custID):
        """ Returns which SubSession ID that a member was
        in from a given Session ID.
        """
        payload = {'custid': custID, 'sessionID': sessNum}
        url = ct.URL_MEM_SUBSESSID
        return await self.build_request(url, payload)

    # Might not be useful. Must be logged in and not affected by custID.

    async def my_racers(self, friends=1, studied=1, blacklisted=1):
        """ Not useful. Returns only friendslist for the person logged in """
        payload = {
            'friends': friends,
            'studied': studied,
            'blacklisted': blacklisted
        }
        url = ct.URL_MY_RACERS
        return await self.build_request(url, payload)

    async def next_event(
            self,
            series_id,
            event_type=ct.EventType.race,
            date=ct.now_unix_ms
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
        return await self.build_request(url, payload)

    async def personal_bests(self, carID, custID):
        """ Returns the drivers best laptimes for the given carID, as seen on
        the /CareerStats page.
        """
        payload = {'custid': custID, 'carid': carID}
        url = ct.URL_PERSONAL_BESTS
        return await self.build_request(url, payload)

    async def race_guide(
            self,
            unix_time=ct.now_unix_ms,
            show_rookie=None,
            show_class_d=None,
            show_class_c=None,
            show_class_b=None,
            show_class_a=None,
            show_class_pro=None,
            show_class_prowc=None,
            show_oval=None,
            show_road=None,
            show_dirt_oval=None,
            show_dirt_road=None,
            fixed_only=None,
            multiclass_only=None,
            meets_mpr=None,
            hide_unpopulated=None,
            hide_ineligible=None,
            show_official=None
    ):
        """ Returns all data used by the race guide page for the active
        seasons. Filters are identical to those found when visiting the
        race guide with a browser.
        """
        payload = {
            'at': unix_time,
            'showRookie': show_rookie,
            'showClassD': show_class_d,
            'showClassC': show_class_c,
            'showClassB': show_class_b,
            'showClassA': show_class_a,
            'showPro': show_class_pro,
            'showProWC': show_class_prowc,
            'showOval': show_oval,
            'showRoad': show_road,
            'showDirtOval': show_dirt_oval,
            'showDirtRoad': show_dirt_road,
            'hideNotFixedSetup': fixed_only,
            'hideNotMultiClass': multiclass_only,
            'meetsMPR': meets_mpr,
            'hideUnpopulated': hide_unpopulated,
            'hideIneligible': hide_ineligible,
            'showOfficial': show_official
        }
        url = ct.URL_RACEGUIDE
        return await self.build_request(url, payload)

    async def race_laps_all(self, sub_sess_id, carClassID=-1):
        """ Returns information about all laps of a race for *every*
        driver. The class of car can be set for multiclass races.

        To specify laps of a single driver, use race_laps_driver().
        """
        payload = {'subsessionid': sub_sess_id, 'carclassid': carClassID}
        url = ct.URL_LAPS_ALL
        return await self.build_request(url, payload)

    async def race_laps_driver(
            self,
            custID,
            sub_sess_id,
            sim_sess_id=ct.SimSesNum.race
    ):
        """ Returns data for all laps completed of a single driver.
        sim_sess_id specifies the laps from practice, qual, or race.
        """
        payload = {
            'subsessionid': sub_sess_id,
            'simsessnum': sim_sess_id,
            'groupid': custID
        }
        url = ct.URL_LAPS_SINGLE
        return await self.build_request(url, payload)

    # TODO Dictionary list of available flags/filters. custid required

    async def results(
            self,
            custID,
            show_races=1,
            show_quals=0,
            show_tts=0,
            show_ops=0,
            show_official=1,
            show_unofficial=0,
            show_rookie=1,
            show_class_d=1,
            show_class_c=1,
            show_class_b=1,
            show_class_a=1,
            show_pro=1,
            show_prowc=1,
            lower_bound=0,
            upper_bound=25,
            sort=ct.Sort.start_time,
            order=ct.Sort.descending,
            format='json',
            category1=1,
            category2=2,
            category3=3,
            category4=4,
            season_year=2020,
            season_quarter=3,
            race_week=-1,
            track_id=-1,
            car_class=-1,
            car_id=-1
    ):
        """ Returns all data about the results of a session. Providing a
        custID allows for returning all results by a specific driver.
        """
        payload = {
            'custID': custID,
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
            'lowerbound': lower_bound,
            'upperbound': upper_bound,
            'sort': sort,
            'order': order,
            'format': format,
            'category%5B%5D': category1,
            'category%5B%5D': category2,
            'category%5B%5D': category3,
            'category%5B%5D': category4,
            'seasonyear': season_year,
            'seasonquarter': season_quarter,
            'raceweek': race_week,
            'trackid': track_id,
            'carclassid': car_class,
            'carid': car_id
        }
        url = ct.URL_RESULTS
        return await self.build_request(url, payload)

    async def season_for_session(self, sessionID):
        """ Returns the seasonID for a given sessionID. That is this endpoints
        only purpose.
        """
        payload = {'sessionID': sessionID}
        url = ct.URL_SEASON_FOR_SESSION
        return await self.build_request(url, payload)

    async def season_standings(
            self,
            seasonID,
            carClassID=-1,
            clubID=-1,
            raceWeek=-1,
            division=-1,
            start=1,
            end=25,
            sort=ct.Sort.champ_points,
            order=ct.Sort.descending
    ):
        """ Returns the championship point standings of a series.
        This is the same data found in /statsseries.jsp
        """

        payload = {
            'seasonid': seasonID,
            'carclassid': carClassID,
            'clubid': clubID,
            'raceweek': raceWeek,
            'division': division,
            'start': start,
            'end': end,
            'sort': sort,
            'order': order
        }
        url = ct.URL_SEASON_STANDINGS
        return await self.build_request(url, payload)

    async def series_race_results(self, seasonID, raceWeek=-1):
        """ Returns the race results for a seasonID. raceWeek can be
        specified to reduce the size of data returned.
        """
        payload = {'seasonid': seasonID, 'raceweek': raceWeek}
        url = ct.URL_SERIES_RACERESULTS
        return await self.build_request(url, payload)

    async def session_times(self, seasonID):
        """ Returns the next 5 sessions and their starting times from a
        seasonID.
        """
        payload = {'season': seasonID}
        url = ct.URL_SESSION_TIMES
        return await self.build_request(url, payload)

    async def get_irating(self, category, custID):
        """ Utilizes the stats_chart class to return a list of iRating values
        that are used in the /CareerStats charts. Accessing
        get_irating().current will give the most recent irating of a custID
        """
        chart_type = ct.ChartType.irating
        response = await self.stats_chart(category, custID, chart_type)
        irating_list = [IRating(x) for x in response.json()]

        return ChartData(category, ct.ChartType.irating, irating_list)

    async def get_ttrating(self, category, custID):
        """ Utilizes the stats_chart class to return a list of ttrating values
        that are used in the /CareerStats charts.
        """
        chart_type = ct.ChartType.ttrating
        response = await self.stats_chart(category, custID, chart_type)
        ttrating_list = [TTRating(x) for x in response.json()]

        return ChartData(category, chart_type, ttrating_list)

    async def get_license_class(self, category, custID):
        """ Utilizes the stats_chart class to return a list of license values
        that are used in the /CareerStats charts. See the LicenseClass class
        for how to further use this data.
        """
        chart_type = ct.ChartType.license_class
        response = await self.stats_chart(category, custID, chart_type)
        license_class_list = [LicenseClass(x) for x in response.json()]

        return ChartData(category, chart_type, license_class_list)

    async def stats_chart(self, category, custID, chartType):
        """ Returns a list in the form of time:value for the race category
        specified. chartType changes values between iRating, ttRating, or
        Safety Rating. Category chooses 1 of the 4 disciplines.
        """
        payload = {
            'custId': custID,
            'catId': category,
            'chartType': chartType
        }
        url = ct.URL_STATS_CHART
        return await self.build_request(url, payload)

    # TODO New name to differentiate "event" results from session data (this)
    async def sub_sess_results(self, sub_sess_id, custID):
        """ Returns extensive data about a session. This endpoint contains
        data points about a session that are unavaible anywhere else.
        """
        payload = {
            'subsessionID': sub_sess_id,
            'custid': custID
        }
        url = ct.URL_SUBS_RESULTS
        return await self.build_request(url, payload)

    async def team_standings(
            self,
            season_id,
            car_class,
            car_id=-1,
            race_week=-1
    ):
        """ Returns championship point standings of Teams.
        """
        payload = {
            'raceWeekNum': race_week,
            'seasonid': season_id,
            'carClassId': car_id,
            'carId': car_id
        }
        url = ct.URL_SUBS_RESULTS
        return await self.build_request(url, payload)

    # TODO Does not return JSON format. Find how to convert.

    async def total_registered_all(self):
        """ Returns a list of every upcoming session and the number of
        drivers that have registered. This data is used in the small text
        next to each series name in /Series.do that shows number of registered
        drivers for that series.
        """
        payload = {}
        url = ct.URL_TOTALREGISTERED
        return await self.build_request(url, payload)

    async def world_records(self, year, quarter, carID, trackID, custID):
        """ Returns laptimes with the requested paramaters. Filters can also
        be seen on the /worldrecords.jsp page on the membersite.
        """
        payload = {
            'seasonyear': year,
            'seasonquarter': quarter,
            'carid': carID,
            'trackid': trackID,
            'custid': custID,
            'format': 'json',
            'upperbound': 1
        }
        url = ct.URL_WORLD_RECORDS
        return await self.build_request(url, payload)

    async def yearly_stats(self, custID):
        """ Returns the breakdown of career stats by year, as seen on the
        /CareerStats driver profile.
        """
        payload = {'custid': custID}
        url = ct.URL_YEARLY_STATS
        response = await self.build_request(url, payload)

        if not response.json():
            return []

        return [YearlyStats(x) for x in response.json()]

    # Returns a list of keys from the dictionary where values are truthy
    @staticmethod
    def key_list_from_dict(dictionary):
        key_list = []
        for key, value in dictionary.items():
            if value:
                key_list.append(key)

        return key_list
