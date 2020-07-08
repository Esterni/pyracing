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
session = requests.Session()

# TODO Should variables be defined globally or per function?
custID = 435144


def inital_login():

    # Calculate utcoffset from local time
    utcoffset = round(
        abs(time.localtime().tm_gmtoff / 60))

    # Retrieve credentials from OS Environment Variables.
    username = os.getenv('IRACING_USERNAME')
    password = os.getenv('IRACING_PASSWORD')

    login_data = {
        'username': username,
        'password': password,
        'utcoffset': utcoffset,
        'todaysdate': ''
    }

    session.post(ct.URL_LOGIN2, data=login_data)
    save_cookies(session)


def save_cookies(session, filename='cookie.tmp'):
    '''Saves all cookies from a session object to file
    utilizing the pickle module for serialization
    '''

    with open(filename, 'w+') as f:
        pickle.dump(session.cookies, f)
        f.close()
    return True


def load_cookies(filename='cookie.tmp'):
    '''Loads CookieJar object from file if 'cookie' contains data.
    If the file is empty, a new session is created instead.
    '''
    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            with open(filename, 'rb') as f:
                content = pickle.load(f)
                f.close()
                return content
        else:
            inital_login()

# TODO Add cookie check here?
# Wrapper for all functions that builds the final session.get()


def request(url_function):
    def wrapper():
        grab_cookie = load_cookies()
        url, payload = url_function()
        response = session.get(url, params=payload, cookies=grab_cookie)
        return response
    return wrapper


@request
def active_op_counts(custID=custID, maxCount=250):
    url = ct.URL_ACTIVEOP_COUNT
    payload = {
        'custid': custID,
        'maxcount': maxCount,
        'include_empty': 'n',  # Flag is y/n
        'excludeLite': 0
    }
    return url, payload


@request
def all_subsessions(subSessID):
    payload = {'subsessionid': subSessID}
    url = ct.URL_ALL_SUBSESSIONS
    return url, payload


@request
def car_class_by_id(carClassID):
    payload = {'carclassid': carClassID}
    url = ct.URL_CAREER_STATS
    return url, payload


@request
def career_stats(custID=custID):
    '''Returns driver career stats
    '''
    payload = {'custid': custID}
    url = ct.URL_CAREER_STATS
    return url, payload


@request
def current_seasons(onlyActive=1):
    '''Returns data about all seasons.
    '''
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
    return url, payload

# TODO Use *kwargs with dictionary for default values? Very long list.


@request
def driver_stats():
    payload = {}
    url = ct.URL_DRIVER_STATS
    return url, payload

# TODO Find query string parameters for this url


@request
def hosted_results():
    '''Currently non-functional
    '''
    payload = {}
    url = ct.URL_HOSTED_RESULTS
    return url, payload


@request
def last_race_stats(custID=custID):
    '''Returns stat summary for the drivers last 10 races
    '''
    payload = {'custid': custID}
    url = ct.URL_LASTRACE_STATS
    return url, payload


@request
def last_series(custID=custID):
    '''Returns a summary of stats about a drivers last 3 series.
    '''
    payload = {'custid': custID}
    url = ct.URL_LAST_SERIES
    return url, payload


@request
def member_cars_driven(custID=custID):
    '''Returns which cars a driver has driven as carID.
    '''
    payload = {'custid': custID}
    url = ct.URL_CARS_DRIVEN
    return url, payload


@request
def member_division(seasonID, custID=custID):
    '''Returns the drivers division from a seasonid
    '''
    payload = {'seasonid': seasonID, 'custid': custID, 'pointstype': 'race'}
    url = ct.URL_MEM_DIVISION
    return url, payload


@request
def member_sub_id_from_session(sessNum, custid=custID):
    '''Returns which SubSession ID that a member was
    in from a given Session ID.
    '''
    payload = {'custid': custID, 'sessionID': sessNum}
    url = ct.URL_MEM_SUBSESSID
    return url, payload

# Might not be useful. Must be logged in and not affected by custID.


@request
def my_racers(friends=1, studied=1, blacklisted=1):
    payload = {
        'friends': friends,
        'studied': studied,
        'blacklisted': blacklisted
    }
    url = ct.URL_MY_RACERS
    return url, payload


@request
def next_event(seriesID, event=ct.EVENT['race']):
    '''Returns information for the upcoming session with given
    seriesID, evtType, and date.
    '''
    payload = {
        'seriesID': seriesID,
        'evtType': event,
        'date': ct.now_unix_ms
    }
    url = ct.URL_NEXT_EVENT
    return url, payload


@request
def personal_bests(carID, custID=custID):
    '''Returns the drivers best laptimes'''

    payload = {'custid': custID, 'carid': carID}
    url = ct.URL_PERSONAL_BESTS
    return url, payload

# TODO Dictionary list of all filters possible


@request
def race_guide():

    payload = {}
    url = ct.URL_RACEGUIDE
    return url, payload


@request
def race_laps_all(subSessID, carClassID=-1):

    payload = {'subsessionid': subSessID, 'carclassid': carClassID}
    url = ct.URL_LAPS_ALL
    return url, payload


@request
def race_laps_driver(subSessID, simSessID, custID=custID):

    payload = {
        'subsessionid': subSessID,
        'simsessnum': simSessID,
        'groupid': custID
    }
    url = ct.URL_LAPS_SINGLE
    return url, payload

# TODO Dictionary list of available flags/filters. custid required


@request
def results(custID=custID):

    payload = {'custid': custID}
    url = ct.URL_RESULTS
    return url, payload


@request
def season_for_session(sessionID):
    '''Returns the seasonID for a given sessionID
    '''
    payload = {'sessionID': sessionID}
    url = ct.URL_SEASON_FOR_SESSION
    return url, payload


@request
def season_standings(
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
    return url, payload


@request
def series_race_results(seasonID, raceWeek=-1):

    payload = {'seasonid': seasonID, 'raceweek': raceWeek}
    url = ct.URL_SERIES_RACERESULTS
    return url, payload


@request
def session_times(seasonID):

    payload = {'season': seasonID}
    url = ct.URL_SESSION_TIMES
    return url, payload


@request
def stats_chart(category, custID=custID, chartType=1):

    payload = {
        'custId': custID,
        'catId': category,
        'chartType': chartType
    }
    url = ct.URL_STATS_CHART
    return url, payload


@request
def sub_sess_results(subSessID, custID=custID):

    payload = {
        'subsessionID': subSessID,
        'custid': custID
    }
    url = ct.URL_SUBS_RESULTS
    return url, payload


@request
def ticker_sessions():

    payload = {}
    url = ct.URL_TICKER_SESSIONS
    return url, payload

# TODO Does not return JSON format. Find how to convert.


@request
def total_registered_all():

    payload = {}
    url = ct.URL_TOTALREGISTERED
    return url, payload


@request
def world_records(year, quarter, carID, trackID, custID=custID):

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
    return url, payload


@request
def yearly_stats(custID=custID):

    payload = {'custid': custID}
    url = ct.URL_YEARLY_STATS
    return url, payload
