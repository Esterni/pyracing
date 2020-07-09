from . import constants as ct

import requests
import pickle
import os
import json
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

# Cookies are handled by the Session() object behind the scenes, only
# requiring them to be stored in a file if a session is closed.


# Create a global instance of Session() from requests module.


class Client:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.session = requests.Session()

    def initial_login(self):

        # Calculate utcoffset from local time
        utcoffset = round(
            abs(time.localtime().tm_gmtoff / 60))

        login_data = {
            'username': self.username,
            'password': self.password,
            'utcoffset': utcoffset,
            'todaysdate': ''
        }

        self.session.post(ct.URL_LOGIN2, data=login_data)
        self.save_cookies()

    def save_cookies(self, filename='cookie.tmp'):
        """Saves all cookies from a session object to file
        utilizing the pickle module for serialization
        """

        with open(filename, 'wb+') as f:
            pickle.dump(self.session.cookies, f)
            f.close()
        return True

    def load_cookies(self, filename='cookie.tmp'):
        """Loads CookieJar object from file if 'cookie' contains data.
        If the file is empty, a new session is created instead.
        """
        if os.path.exists(filename):
            if os.path.getsize(filename) > 0:
                with open(filename, 'rb') as f:
                    content = pickle.load(f)
                    f.close()
                    return content
            else:
                self.initial_login()

    # TODO Add cookie check here?
    # Wrapper for all functions that builds the final self.session.get()

    def get(self, url, params):
        return self.session.get(url, params=params, cookies=self.load_cookies())

    def active_op_counts(self, custID, maxCount=250):
        url = ct.URL_ACTIVEOP_COUNT
        payload = {
            'custid': custID,
            'maxcount': maxCount,
            'include_empty': 'n',  # Flag is y/n
            'excludeLite': 0
        }
        return self.get(url, payload)

    def all_subsessions(self, subSessID):
        payload = {'subsessionid': subSessID}
        url = ct.URL_ALL_SUBSESSIONS
        return self.get(url, payload)

    def car_class_by_id(self, carClassID):
        payload = {'carclassid': carClassID}
        url = ct.URL_CAREER_STATS
        return self.get(url, payload)

    def career_stats(self, custID):
        """Returns driver career stats
        """
        payload = {'custid': custID}
        url = ct.URL_CAREER_STATS
        return self.get(url, payload)

    def current_seasons(self, onlyActive=1):
        """Returns data about all seasons.
        """
        # List of possible fields. Set any to 1 to return that field.
        fieldDict = {
            'year': 0,
            'quarter': 0,
            'seriesshortname': 1,
            'seriesid': 0,
            'active': 0,
            'catid': 1,
            'licenseeligible': 0,
            'islite': 0,
            'carclasses': 0,
            'tracks': 0,
            'start': 0,
            'end': 0,
            'cars': 0,
            'raceweek': 0,
            'category': 0,
            'serieslicgroudid': 0,
            'carid': 0,  # Appears not to work?
            'seasonid': 1,
        }

        requestedFields = []
        # Iterate through possible fields, adding requested fields to list
        for key in fieldDict:
            if fieldDict[key] == 1:
                requestedFields.append(key)
            else:
                continue

        payload = {
            'onlyActive': onlyActive,
            'fields': (','.join(requestedFields))
        }
        url = ct.URL_CURRENT_SEASONS
        return self.get(url, payload)

    # TODO Use *kwargs with dictionary for default values? Very long list.

    def driver_stats(self):
        payload = {}
        url = ct.URL_DRIVER_STATS
        return self.get(url, payload)

    # TODO Find query string parameters for this url

    def hosted_results(self):
        """Currently non-functional
        """
        payload = {}
        url = ct.URL_HOSTED_RESULTS
        return self.get(url, payload)

    def last_race_stats(self, custID):
        """Returns stat summary for the drivers last 10 races
        """
        payload = {'custid': custID}
        url = ct.URL_LASTRACE_STATS
        return self.get(url, payload)

    def last_series(self, custID):
        """Returns a summary of stats about a drivers last 3 series.
        """
        payload = {'custid': custID}
        url = ct.URL_LAST_SERIES
        return self.get(url, payload)

    def member_cars_driven(self, custID):
        """Returns which cars a driver has driven as carID.
        """
        payload = {'custid': custID}
        url = ct.URL_CARS_DRIVEN
        return self.get(url, payload)

    def member_division(self, seasonID, custID):
        """Returns the drivers division from a seasonid
        """
        payload = {'seasonid': seasonID,
                   'custid': custID, 'pointstype': 'race'}
        url = ct.URL_MEM_DIVISION
        return self.get(url, payload)

    def member_sub_id_from_session(self, sessNum, custID):
        """Returns which SubSession ID that a member was
        in from a given Session ID.
        """
        payload = {'custid': custID, 'sessionID': sessNum}
        url = ct.URL_MEM_SUBSESSID
        return self.get(url, payload)

    # Might not be useful. Must be logged in and not affected by custID.

    def my_racers(self, friends=1, studied=1, blacklisted=1):
        payload = {
            'friends': friends,
            'studied': studied,
            'blacklisted': blacklisted
        }
        url = ct.URL_MY_RACERS
        return self.get(url, payload)

    def next_event(self, seriesID, event=ct.EVENT['race']):
        """Returns information for the upcoming session with given
        seriesID, evtType, and date.
        """
        payload = {
            'seriesID': seriesID,
            'evtType': event,
            'date': ct.now_unix_ms
        }
        url = ct.URL_NEXT_EVENT
        return self.get(url, payload)

    def personal_bests(self, carID, custID):
        """Returns the drivers best laptimes
        """

        payload = {'custid': custID, 'carid': carID}
        url = ct.URL_PERSONAL_BESTS
        return self.get(url, payload)

    # TODO Dictionary list of all filters possible

    def race_guide(self):

        payload = {}
        url = ct.URL_RACEGUIDE
        return self.get(url, payload)

    def race_laps_all(self, subSessID, carClassID=-1):

        payload = {'subsessionid': subSessID, 'carclassid': carClassID}
        url = ct.URL_LAPS_ALL
        return self.get(url, payload)

    def race_laps_driver(self, subSessID, simSessID, custID):

        payload = {
            'subsessionid': subSessID,
            'simsessnum': simSessID,
            'groupid': custID
        }
        url = ct.URL_LAPS_SINGLE
        return self.get(url, payload)

    # TODO Dictionary list of available flags/filters. custid required

    def results(self, custID):

        payload = {'custid': custID}
        url = ct.URL_RESULTS
        return self.get(url, payload)

    def season_for_session(self, sessionID):
        """Returns the seasonID for a given sessionID
        """
        payload = {'sessionID': sessionID}
        url = ct.URL_SEASON_FOR_SESSION
        return self.get(url, payload)

    def season_standings(
        self,
        seasonID,
        carClassID=-1,
        clubID=-1,
        raceWeek=-1,
        division=-1,
        start=1,
        end=25
    ):

        payload = {
            'seasonid': seasonID,
            'carclassid': carClassID,
            'clubid': clubID,
            'raceweek': raceWeek,
            'division': division,
            'start': start,
            'end': end,
            'sort': 'points',
            'order': 'desc'
        }
        url = ct.URL_SEASON_STANDINGS
        return self.get(url, payload)

    def series_race_results(self, seasonID, raceWeek=-1):

        payload = {'seasonid': seasonID, 'raceweek': raceWeek}
        url = ct.URL_SERIES_RACERESULTS
        return self.get(url, payload)

    def session_times(self, seasonID):

        payload = {'season': seasonID}
        url = ct.URL_SESSION_TIMES
        return self.get(url, payload)

    def stats_chart(self, category, custID, chartType=1):

        payload = {
            'custId': custID,
            'catId': category,
            'chartType': chartType
        }
        url = ct.URL_STATS_CHART
        return self.get(url, payload)

    def sub_sess_results(self, subSessID, custID):

        payload = {
            'subsessionID': subSessID,
            'custid': custID
        }
        url = ct.URL_SUBS_RESULTS
        return self.get(url, payload)

    def ticker_sessions(self):

        payload = {}
        url = ct.URL_TICKER_SESSIONS
        return self.get(url, payload)

    # TODO Does not return JSON format. Find how to convert.

    def total_registered_all(self):

        payload = {}
        url = ct.URL_TOTALREGISTERED
        return self.get(url, payload)

    def world_records(self, year, quarter, carID, trackID, custID):

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
        return self.get(url, payload)

    def yearly_stats(self, custID):

        payload = {'custid': custID}
        url = ct.URL_YEARLY_STATS
        return self.get(url, payload)
