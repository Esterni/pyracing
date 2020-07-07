import ir_webstats_rc.constants as ct

import requests
import pickle
import os
import json
import time


# This module authenticates, builds, and sends URL queries to iRacing.
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
custID = 435144

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

@request
def activeOPCounts(custID=custID, maxCount=250):
    URL = ct.URL_ACTIVEOP_COUNT
    payload = {
        'custid': custID,
        'maxcount': maxCount,
        'include_empty': 'n',  # Flag is y/n
        'excludeLite': 0
        }
    return URL, payload

@request
def allSubsessions(subSessID):
    payload = {'subsessionid': subSessID}
    URL = ct.URL_ALL_SUBSESSIONS
    return URL, payload

@request
def carClassByID(carClassID):
    payload = {'carclassid': carClassID}
    URL = ct.URL_CAREER_STATS
    return URL, payload

@request
def careerStats(custID=custID):
    '''Returns driver career stats
    '''
    payload = {'custid': custID}
    URL = ct.URL_CAREER_STATS
    return URL, payload

@request
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
    URL = ct.URL_CURRENT_SEASONS
    return URL, payload

# TODO Use *kwargs with dictionary for default values? Very long list.
@request
def driverStats():
    payload = {}
    URL = ct.URL_DRIVER_STATS
    return URL, payload

# TODO Find query string parameters for this URL
@request
def hostedResults():
    '''Currently non-functional
    '''
    payload = {}
    URL = ct.URL_HOSTED_RESULTS
    return URL, payload

@request
def lastRaceStats(custID=custID):
    '''Returns stat summary for the drivers last 10 races
    '''
    payload = {'custid': custID}
    URL = ct.URL_LASTRACE_STATS
    return URL, payload

@request
def lastSeries(custID=custID):
    '''Returns a summary of stats about a drivers last 3 series.
    '''
    payload = {'custid': custID}
    URL = ct.URL_LAST_SERIES
    return URL, payload

@request
def memberCarsDriven(custID=custID):
    '''Returns which cars a driver has driven as carID.
    '''
    payload = {'custid': custID}
    URL = ct.URL_CARS_DRIVEN
    return URL, payload

@request
def memberDivision(seasonID, custID=custID):
    '''Returns the drivers division from a seasonid
    '''
    payload = {'seasonid': seasonID, 'custid': custID, 'pointstype': 'race'}
    URL = ct.URL_MEM_DIVISION
    return URL, payload

@request
def memberSubIDFromSession(sessNum, custid=custID):
    '''Returns which SubSession ID that a member was
    in from a given Session ID.
    '''
    payload = {'custid': custID, 'sessionID': sessNum}
    URL = ct.URL_MEM_SUBSESSID
    return URL, payload

# Might not be useful. Must be logged in and not affected by custID.
@request
def myRacers(friends=1, studied=1, blacklisted=1):
    payload = {
        'friends': friends,
        'studied': studied,
        'blacklisted': blacklisted
        }
    URL = ct.URL_MY_RACERS
    return URL, payload

@request
def nextEvent(seriesID, event=ct.EVENT['race']):
    '''Returns information for the upcoming session with given
    seriesID, evtType, and date.
    '''
    payload = {
        'seriesID': seriesID,
        'evtType': event,
        'date': ct.now_unix_ms
        }
    URL = ct.URL_NEXT_EVENT
    return URL, payload

@request
def personalBestTimes(carID, custID=custID):
    '''Returns the drivers best laptimes'''

    payload = {'custid': custID, 'carid': carID}
    URL = ct.URL_PERSONAL_BESTS
    return URL, payload

# TODO Dictionary list of all filters possible
@request
def raceGuide():

    payload = {}
    URL = ct.URL_RACEGUIDE
    return URL, payload

@request
def raceLapsAll(subSessID, carClassID=-1):

    payload = {'subsessionid': subSessID, 'carclassid': carClassID}
    URL = ct.URL_LAPS_ALL
    return URL, payload

@request
def raceLapsDriver(subSessID, simSessID, custID=custID):

    payload = {
        'subsessionid': subSessID,
        'simsessnum': simSessID,
        'groupid': custID
        }
    URL = ct.URL_LAPS_SINGLE
    return URL, payload

# TODO Dictionary list of available flags/filters. custid required
@request
def results(custID=custID):

    payload = {'custid': custID}
    URL = ct.URL_RESULTS
    return URL, payload

@request
def seasonForSession(sessionID):
    '''Returns the seasonID for a given sessionID
    '''
    payload = {'sessionID': sessionID}
    URL = ct.URL_SEASON_FOR_SESSION
    return URL, payload

@request
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
    URL = ct.URL_SEASON_STANDINGS
    return URL, payload

@request
def seriesRaceResults(seasonID, raceWeek=-1):

    payload = {'seasonid': seasonID, 'raceweek': raceWeek}
    URL = ct.URL_SERIES_RACERESULTS
    return URL, payload

@request
def sessionTimes(seasonID):

    payload = {'season': seasonID}
    URL = ct.URL_SESSION_TIMES
    return URL, payload

@request
def statsChart(category, custID=custID, chartType=1):

    payload = {
        'custId': custID,
        'catId': category,
        'chartType': chartType
        }
    URL = ct.URL_STATS_CHART
    return URL, payload

@request
def subSessResults(subSessID, custID=custID):

    payload = {
        'subsessionID': subSessID,
        'custid': custID
        }
    URL = ct.URL_SUBS_RESULTS
    return URL, payload

@request
def tickerSessions():

    payload = {}
    URL = ct.URL_TICKER_SESSIONS
    return URL, payload

# TODO Does not return JSON format. Find how to convert.
@request
def totalRegisteredAll():

    payload = {}
    URL = ct.URL_TOTALREGISTERED
    return URL, payload

@request
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
    URL = ct.URL_WORLD_RECORDS
    return URL, payload

@request
def yearlyStats(custID=custID):

    payload = {'custid': custID}
    URL = ct.URL_YEARLY_STATS
    return URL, payload
