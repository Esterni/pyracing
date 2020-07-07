import ir_webstats_rc.NewClient.constants as ct

import requests
import pickle
import os
import json
import time


# This module authenticates, builds, and sends URL queries to iRacing URLs.
# Each function is set with only the variables required for the respective
# endpoint to return the desired data. Compared to the previous client.py,
# this module does not attempt to parse any of the data received. Instead,
# each function returns the response object from requests.Session() to
# provide more versatility from a function.

# Response objects include the .json() method, which is the same result
# that was found in util.py as parse(). Since new endpoints have been found,
# there is no longer a need for regex, drastically reducing the complexity
# of the code.

# Cookies are handled by the Session() object behind the scenes, only
# requiring them to be stored in a file if a session is closed.



# Retrieve credentials from OS Environment Variables.
username = os.getenv('IRACING_USERNAME')
password = os.getenv('IRACING_PASSWORD')

# Create a global instance of Session() from requests module.
login_session = requests.Session()

# TODO Should variables be defined globally or per function?
custID = None


def inital_login():

    # Calculate utcoffset from local time
    utcoffset = round(
        abs(time.localtime().tm_gmtoff / 60))

    loginData = {
        'username': username,
        'password': password,
        'utcoffset': utcoffset,
        'todaysdate': ''
        }

    login_session.post(ct.URL_LOGIN2, data=loginData)
    save_cookies(login_session)


def save_cookies(session, filename='cookie.tmp'):
    '''Saves all cookies from a session object to file
    utilizing the pickle module for serialization
    '''

    with open(filename, 'wb') as f:
        pickle.dump(session.cookies, f)
        f.close()
    return True


def load_cookies(filename='cookie.tmp'):
    '''Loads CookieJar object from file if 'cookie' contains data.
    If the file is empty, a new session is created instead.
    '''
    if os.path.getsize(filename) > 0:
        with open(filename, 'rb') as f:
            content = pickle.load(f)
            f.close()
            return content
    else:
        inital_login()

# TODO Add cookie check here?
# Wrapper for all functions that builds the final session.get()
def request(URL_Function):
    def wrapper():
        grabCookie = load_cookies()
        URL, payload = URL_Function()
        response = login_session.get(URL, params=payload, cookies=grabCookie)
        return response
    return wrapper


def activeOPCounts(custID=custID, maxCount=250):
    '''Returns active open practices. Data is in the form
    of {m:{map}, d:[{data},{data},{data}]}
    '''

    payload = {
        'custid': custID,
        'maxcount': 250,
        'include_empty': 'n',  # Flag is y/n
        'excludeLite': 0
        }

    r = login_session.get(
        ct.URL_ACTIVEOP_COUNT,
        cookies=grabCookie,
        params=payload
        )
    return r


def allSubsessions(subSessID):

    payload = {'subsessionid': subSessID}

    r = login_session.get(
        ct.URL_ALL_SUBSESSIONS,
        cookies=grabCookie,
        params=payload
        )

    return r


def carClassByID(carClassID):

    payload = {'carclassid': carClassID}

    r = login_session.get(
        ct.URL_CAREER_STATS,
        cookies=grabCookie,
        params=payload
        )

    return r


def careerStats(custID=custID):
    '''Returns driver career stats
    '''

    payload = {'custid': custID}

def currentSeasons(onlyActive=1):
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
    # Include inactive series if kwarg 'onlyActive' set to False
    if onlyActive == False:
        payload['onlyActive'] = 0

    r = login_session.get(
        ct.URL_CURRENT_SEASONS,
        cookies=grabCookie,
        params=payload
        )
    return r

# TODO Use *kwargs with dictionary for default values? Very long list.
def driverStats():

    payload = {}
    r = login_session.get(
        ct.URL_DRIVER_STATS,
        cookies=grabCookie,
        params=payload
        )
    return r

# TODO Find query string parameters for this URL
def hostedResults():
    '''Currently non-functional
    '''

    payload = {}

    r = login_session.get(
        ct.URL_HOSTED_RESULTS,
        cookies=grabCookie,
        params=payload
        )
    return r


def lastRaceStats(custID=custID):
    '''Returns stat summary for the drivers last 10 races
    '''

    payload = {'custid': custID}

    r = login_session.get(
        ct.URL_LASTRACE_STATS,
        cookies=grabCookie,
        params=payload
        )
    return r


def lastSeries(custID=custID):
    '''Returns a summary of stats about a drivers last 3 series.
    '''

    payload = {'custid': custID}

    r = login_session.get(
        ct.URL_LAST_SERIES,
        cookies=grabCookie,
        params=payload
        )
    return r


def memberCarsDriven(custID=custID):
    '''Returns which cars a driver has driven as carID.
    '''

    payload = {'custid': custID}

    r = login_session.get(
        ct.URL_CARS_DRIVEN,
        cookies=grabCookie,
        params=payload
        )
    return r


def memberDivision(seasonID, custID=custID):
    '''Returns the drivers division from a seasonid
    '''

    payload = {
        'seasonid': seasonID,
        'custid': custID,
        'pointstype': 'race'
        }

    r = login_session.get(
        ct.URL_MEM_DIVISION,
        cookies=grabCookie,
        params=payload
        )
    return r


def memberSubIDFromSession(sessNum, custid=custID):
    '''Returns which SubSession ID that a member was
    in from a given Session ID.
    '''

    payload = {
        'custid': custID,
        'sessionID': sessNum
        }

    r = login_session.get(
        ct.URL_MEM_SUBSESSID,
        cookies=grabCookie,
        params=payload
        )
    return r


# Might not be useful. Must be logged in and not affected by custID.
def myRacers(friends=1, studied=1, blacklisted=1):
    payload = {
        'friends': friends,
        'studied': studied,
        'blacklisted': blacklisted

    r = login_session.get(
        ct.URL_MY_RACERS,
        cookies=grabCookie,
        params=payload
        )
    return r


def nextEvent(seriesID, event=5):
    '''Returns information for the upcoming session with given
    seriesID, evtType, and date.
    '''

    payload = {
        'seriesID': seriesID,
        'evtType': event,
        'date': ct.now_unix_ms
    }

    r = login_session.get(
        ct.URL_NEXT_EVENT,
        cookies=grabCookie,
        params=payload
        )
    return r


def personalBestTimes(carID, custID=custID):
    '''Returns the drivers best laptimes'''

    payload = {
        'custid': custID,
        'carid': carID
        }

    r = login_session.get(
        ct.URL_PERSONAL_BESTS,
        cookies=grabCookie,
        params=payload
        )
    return r

# TODO Dictionary list of all filters possible
def raceGuide():

    payload = {}

    r = login_session.get(
        ct.URL_RACEGUIDE,
        cookies=grabCookie,
        params=payload
        )
    return r


def raceLapsAll(subSessID, carClassID=-1):

    payload = {
        'subsessionid': subSessID,
        'carclassid': carClassID
        }

    r = login_session.get(
        ct.URL_LAPS_ALL,
        cookies=grabCookie,
        params=payload
        )
    return r


def raceLapsDriver(subSessID, simSessID, custID=custID):

    payload = {
        'subsessionid': subSessID,
        'simsessnum': simSessID,
        'groupid': custID
        }

    r = login_session.get(
        ct.URL_LAPS_SINGLE,
        cookies=grabCookie,
        params=payload
        )
    return r

# TODO Dictionary list of available flags/filters. custid required
def results(custID=custID):

    payload = {
        'custid': custID
        }

    r = login_session.get(
        ct.URL_RESULTS,
        cookies=grabCookie,
        params=payload
        )
    return r


def seasonForSession(sessionID):
    '''Returns the seasonID for a given sessionID
    '''

    payload = {
        'sessionID': sessionID
    }

    r = login_session.get(
        ct.URL_SEASON_FOR_SESSION,
        cookies=grabCookie,
        params=payload
        )

    return r


def seasonStandings(
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

    r = login_session.get(
        ct.URL_SEASON_STANDINGS,
        cookies=grabCookie,
        params=payload
        )
    return r


def seriesRaceResults(seasonID, raceWeek=-1):

    payload = {
        'seasonid': seasonID,
        'raceweek': raceWeek
    }

    r = login_session.get(
        ct.URL_SERIES_RACERESULTS,
        cookies=grabCookie,
        params=payload
        )

    return r


def sessionTimes(seasonID):

    payload = {'season': seasonID}

    r = login_session.get(
        ct.URL_SESSION_TIMES,
        cookies=grabCookie,
        params=payload
        )
    return r


def statsChart(category, custID=custID, chartType=1):

    payload = {
        'custId': custID,
        'catId': category,
        'chartType': chartType
    }

    r = login_session.get(
        ct.URL_STATS_CHART,
        cookies=grabCookie,
        params=payload
        )
    return r


def subSessResults(subSessID, custID=custID):

    payload = {
        'subsessionID': subSessID,
        'custid': custID
    }

    r = login_session.get(
        ct.URL_SUBS_RESULTS,
        cookies=grabCookie,
        params=payload
        )
    return r


def tickerSessions():

    payload = {}

    r = login_session.get(
        ct.URL_TICKER_SESSIONS,
        cookies=grabCookie,
        params=payload
        )
    return r

# TODO Does not return JSON format. Find how to convert.
def totalRegisteredAll():

    # No payload (URL query) for this URL

    r = login_session.get(
        ct.URL_TOTALREGISTERED,
        cookies=grabCookie
        )
    return r.content


def worldRecords(year, quarter, carID, trackID, custID=custID):

    payload = {
        'seasonyear': year,
        'seasonquarter': quarter,
        'carid': carID,
        'trackid': trackID,
        'custid': custID,
        'format': 'json',
        'upperbound': 1
        }

    r = login_session.get(
        ct.URL_WORLD_RECORDS,
        cookies=grabCookie,
        params=payload
        )
    return r


def yearlyStats(custID=custID):

    payload = {'custid': custID}

    r = login_session.get(
        ct.URL_YEARLY_STATS,
        cookies=grabCookie,
        params=payload
        )
    return r
