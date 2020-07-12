from . import constants as ct
from .responses.last_races_stats import LastRaceStats
from .responses.career_stats import CareerStats
from .responses.yearly_stats import YearlyStats
from .responses.chart_data.chart_data import ChartData
from .responses.chart_data.irating import IRating
from .responses.chart_data.ttrating import TTRating
from .responses.chart_data.license_class import LicenseClass

import logging
import requests_async as requests
import sys
import time


# This module authenticates, builds, and sends url queries to iRacing.
# Each function is set with only the variables required, for the respective
# endpoint, to return the desired data.  Compared to the previous client.py,
# this module does not attempt to parse any of the data received.  Instead,
# each function returns the response object from requests.Session() to
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
        self.session = requests.Session()
        self.log = log

    async def authenticate(self):
        """ Sends a POST request to iRacings login server, initiating a
        persistent connection stored in self.session
        """
        self.log.info('Authenticating...')

        # Calculates accepted utcoffset from local system time
        utcoffset = round(
            abs(time.localtime().tm_gmtoff / 60))

        login_data = {
            'username': self.username,
            'password': self.password,
            'utcoffset': utcoffset,
            'todaysdate': ''  # Unknown purpose, but present as hidden form.
        }

        auth_post = await self.session.post(ct.URL_LOGIN2, data=login_data)

        if 'failedlogin' in auth_post.url:
            self.log.warning('Login Failed. Please check credentials')
            raise UserWarning(
                'The login POST was redirected to /failedlogin, indicating an'
                ' authentication failure. If credentials are correct, manually'
                ' check that a captcha is not required at members.iracing.com'
            )
        else:
            self.log.info('Login successful')

    # Wrapper for all functions that builds the final self.session.get()

    async def build_request(self, url, params, retry=True):
        """ Builds the final GET request from url and params
        """

        self.log.info('Making get request to url: ' +
                      url + f' with params: {params}')

        response = await self.session.get(url, params=params)

        self.log.info(f'iRacing response: {response.__dict__}')

        # This happens when we are not logged in or the cookie has expired
        if 'not authorized' in response.text and retry:
            self.log.info('Retrying authenticate and then repeating request')
            await self.authenticate()
            return await self.build_request(url, params, False)
        elif 'not authorized' in response.text and not retry:
            self.log.error('Authentication retry failed')
            raise RuntimeError(
                'Authentication failed. Make sure username and password'
                'are correct and that the iRacing servers are not down'
            )

        return response

    async def active_op_counts(self, custID, maxCount=250):
        url = ct.URL_ACTIVEOP_COUNT
        payload = {
            'custid': custID,
            'maxcount': maxCount,
            'include_empty': 'n',  # Flag is y/n
            'excludeLite': 0
        }
        return await self.build_request(url, payload)

    async def all_subsessions(self, subSessID):
        payload = {'subsessionid': subSessID}
        url = ct.URL_ALL_SUBSESSIONS
        return await self.build_request(url, payload)

    async def car_class_by_id(self, carClassID):
        payload = {'carclassid': carClassID}
        url = ct.URL_CAREER_STATS
        return await self.build_request(url, payload)

    async def career_stats(self, custID):
        """Returns driver career stats
        """
        payload = {'custid': custID}
        url = ct.URL_CAREER_STATS
        response = await self.build_request(url, payload)

        if not response.json():
            return []

        return list(map(lambda x: CareerStats(x), response.json()))

    async def current_seasons(
            self,
            only_active=True,
            series_short_name=True,
            cat_id=True,
            season_id=True,
            year=False,
            quarter=False,
            series_id=False,
            active=False,
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
        """Returns data about all seasons."""
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
        return await self.build_request(url, payload)

    # TODO Use *kwargs with dictionary for default values? Very long list.

    async def driver_stats(self,
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
        payload = {
            'search': str(search),
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
        """Returns a list of private sessions that the driver
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
        """Returns stat summary for the drivers last 10 races
        """
        payload = {'custid': custID}
        url = ct.URL_LASTRACE_STATS
        response = await self.build_request(url, payload)

        if not response.json():
            return []

        return list(map(lambda x: LastRaceStats(x), response.json()))

    async def last_series(self, custID):
        """Returns a summary of stats about a drivers last 3 series.
        """
        payload = {'custid': custID}
        url = ct.URL_LAST_SERIES
        return await self.build_request(url, payload)

    async def member_cars_driven(self, custID):
        """Returns which cars a driver has driven as carID.
        """
        payload = {'custid': custID}
        url = ct.URL_CARS_DRIVEN
        return await self.build_request(url, payload)

    async def member_division(self, seasonID, custID):
        """Returns the drivers division from a seasonid
        """
        payload = {'seasonid': seasonID,
                   'custid': custID, 'pointstype': 'race'}
        url = ct.URL_MEM_DIVISION
        return await self.build_request(url, payload)

    async def member_sub_id_from_session(self, sessNum, custID):
        """Returns which SubSession ID that a member was
        in from a given Session ID.
        """
        payload = {'custid': custID, 'sessionID': sessNum}
        url = ct.URL_MEM_SUBSESSID
        return await self.build_request(url, payload)

    # Might not be useful. Must be logged in and not affected by custID.

    async def my_racers(self, friends=1, studied=1, blacklisted=1):
        payload = {
            'friends': friends,
            'studied': studied,
            'blacklisted': blacklisted
        }
        url = ct.URL_MY_RACERS
        return await self.build_request(url, payload)

    async def next_event(self, seriesID, event=ct.EventType.race):
        """Returns information for the upcoming session with given
        seriesID, evtType, and date.
        """
        payload = {
            'seriesID': seriesID,
            'evtType': event,
            'date': ct.now_unix_ms
        }
        url = ct.URL_NEXT_EVENT
        return await self.build_request(url, payload)

    async def personal_bests(self, carID, custID):
        """Returns the drivers best laptimes
        """
        payload = {'custid': custID, 'carid': carID}
        url = ct.URL_PERSONAL_BESTS
        return await self.build_request(url, payload)

    # TODO Dictionary list of all filters possible

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

    async def race_laps_all(self, subSessID, carClassID=-1):
        payload = {'subsessionid': subSessID, 'carclassid': carClassID}
        url = ct.URL_LAPS_ALL
        return await self.build_request(url, payload)

    async def race_laps_driver(self, subSessID, simSessID, custID):
        payload = {
            'subsessionid': subSessID,
            'simsessnum': simSessID,
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
            'category1': category1,
            'category2': category2,
            'category3': category3,
            'category4': category4,
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
        """Returns the seasonID for a given sessionID
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
        payload = {'seasonid': seasonID, 'raceweek': raceWeek}
        url = ct.URL_SERIES_RACERESULTS
        return await self.build_request(url, payload)

    async def session_times(self, seasonID):
        payload = {'season': seasonID}
        url = ct.URL_SESSION_TIMES
        return await self.build_request(url, payload)

    async def get_irating(self, category, custID):
        chart_type = ct.ChartType.irating
        response = await self.stats_chart(category, custID, chart_type)
        irating_list = list(map(lambda x: IRating(x), response.json()))
        return ChartData(category, ct.ChartType.irating, irating_list)

    async def get_ttrating(self, category, custID):
        chart_type = ct.ChartType.ttrating
        response = await self.stats_chart(category, custID, chart_type)
        ttrating_list = list(map(lambda x: TTRating(x), response.json()))
        return ChartData(category, chart_type, ttrating_list)

    async def get_license_class(self, category, custID):
        chart_type = ct.ChartType.license_class
        response = await self.stats_chart(category, custID, chart_type)
        license_class_list = list(
            map(lambda x: LicenseClass(x), response.json()))
        return ChartData(category, chart_type, license_class_list)

    async def stats_chart(self, category, custID, chartType):
        payload = {
            'custId': custID,
            'catId': category,
            'chartType': chartType
        }
        url = ct.URL_STATS_CHART
        return await self.build_request(url, payload)

    async def sub_sess_results(self, subSessID, custID):
        payload = {
            'subsessionID': subSessID,
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
        payload = {
            'raceWeekNum': race_week,
            'seasonid': season_id,
            'carClassId': car_id,
            'carId': car_id
        }
        url = ct.URL_SUBS_RESULTS
        return await self.build_request(url, payload)

    async def ticker_sessions(self):
        payload = {}
        url = ct.URL_TICKER_SESSIONS
        return await self.build_request(url, payload)

    # TODO Does not return JSON format. Find how to convert.

    async def total_registered_all(self):
        payload = {}
        url = ct.URL_TOTALREGISTERED
        return await self.build_request(url, payload)

    async def world_records(self, year, quarter, carID, trackID, custID):
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
        payload = {'custid': custID}
        url = ct.URL_YEARLY_STATS
        response = await self.build_request(url, payload)

        if not response.json():
            return []

        return list(map(lambda x: YearlyStats(x), response.json()))

    # Returns a list of the keys from the dictionary where the values are truthy
    @staticmethod
    def key_list_from_dict(dictionary):
        key_list = []
        for key, value in dictionary:
            if value:
                key_list.append(key)

        return key_list
