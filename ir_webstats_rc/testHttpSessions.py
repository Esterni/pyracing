import ir_webstats_rc.constants as ct
from ir_webstats_rc.util import pprint

import requests
import pickle
import os
import json
import time

# Retrieve credentials from OS Environment Variables.
username = os.getenv('IRACING_USERNAME')
password = os.getenv('IRACING_PASSWORD')

# Create a global instance of Session() from the requests module.
login_session = requests.Session()

# Loads cookies from file. Defaults to filename 'cookie.'
grabCookie = load_cookies()


def save_cookies(session, filename='cookie'):
    '''Saves all cookies from a session object to file
    utilizing the pickle module for serialization
    '''

    with open(filename, 'wb') as f:
        pickle.dump(session.cookies, f)
        f.close()
    return True


def load_cookies(filename='cookie'):
    with open(filename, 'rb') as f:
        content = pickle.load(f)
        f.close()
        return content


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


def activeOPCounts():
    response = login_session.get(ct.URL_ACTIVEOP_COUNT, cookies=grabCookie)

    return response.json()


def careerStats():
    response = login_session.get(ct.URL_CAREER_STATS, cookies=grabCookie)

    return response.json()


def currentSeasons():
    response = login_session.get(ct.URL_CURRENT_SEASONS, cookies=grabCookie)

    return response.json()


def driverStats():
    response = login_session.get(ct.URL_DRIVER_STATS, cookies=grabCookie)

    return response.json()


def hostedResults():
    response = login_session.get(ct.URL_HOSTED_RESULTS, cookies=grabCookie)

    return response.json


def lastRaceStats():
    response = login_session.get(ct.URL_LASTRACE_STATS, cookies=grabCookie)

    return response.json()


def lastSeries():
    response = login_session.get(ct.URL_LAST_SERIES, cookies=grabCookie)

    return response.json()


def memberCarsDriven():
    response = login_session.get(ct.URL_CARS_DRIVEN, cookies=grabCookie)

    return response.json()


def memberSubSession():
    response = login_session.get(ct.URL_MEM_SUBSESSID, cookies=grabCookie)

    return response.json()


def nextEvent():
    response = login_session.get(ct.URL_NEXT_EVENT, cookies=grabCookie)

    return response.json()


def personalBestTimes():
    response = login_session.get(ct.URL_PERSONAL_BESTS, cookies=grabCookie)

    return response.json()


def raceGuide():
    response = login_session.get(ct.URL_RACEGUIDE, cookies=grabCookie)

    return response.json()


def raceLapsAll():
    response = login_session.get(ct.URL_LAPS_ALL, cookies=grabCookie)

    return response.json()


def raceLapsDriver():
    response = login_session.get(ct.URL_LAPS_SINGLE, cookies=grabCookie)

    return response.json()


def results():
    response = login_session.get(ct.URL_RESULTS, cookies=grabCookie)

    return response.json()


def seasonStandings():
    response = login_session.get(ct.URL_SEASON_STANDINGS, cookies=grabCookie)

    return response.json()


def seriesRaceResults():
    response = login_session.get(ct.URL_SERIES_RACERESULTS, cookies=grabCookie)

    return response.json()


def sessionTimes():
    response = login_session.get(ct.URL_SESSION_TIMES, cookies=grabCookie)

    return response.json()


def statsChart():
    response = login_session.get(ct.URL_STATS_CHART, cookies=grabCookie)

    return response.json()


def subSessResults():
    response = login_session.get(ct.URL_SUBS_RESULTS, cookies=grabCookie)

    return response.json()


def totalRegisteredAll():
    response = login_session.get(ct.URL_TOTALREGISTERED, cookies=grabCookie)

    return response.json()


def worldRecords():
    response = login_session.get(ct.URL_WORLD_RECORDS, cookies=grabCookie)

    return response.json()


def yearlyStats():
    response = login_session.get(ct.URL_YEARLY_STATS, cookies=grabCookie)

    return response.json()



