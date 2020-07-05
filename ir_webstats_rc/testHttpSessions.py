import ir_webstats_rc.constants as ct
from ir_webstats_rc.util import pprint

import requests
import pickle
import os
import json
import time

login_session = requests.Session()


def save_cookies(session, filename='cookie.tmp'):
    with open(filename, 'wb') as f:
        pickle.dump(session.cookies, f)


def load_cookies(filename='cookie.tmp'):
    with open(filename, 'rb') as f:
        content = pickle.load(f)
        return content


grabCookie = load_cookies()

def inital_login():

    utcoffset = round(
        abs(time.localtime().tm_gmtoff / 60))

    loginData = {
        'username': ct.username,
        'password': ct.password,
        'utcoffset': utcoffset,
        'todaysdate': ''
        }

    login_session.post(ct.URL_IRACING_LOGIN2, data=loginData)
    save_cookies(login_session)

def lastRaceStats():
    r = login_session.get(ct.URL_LASTRACE_STATS, cookies=grabCookie)

    return r.text

'''
class iRWebStats:

    def __init__(self, verbose=True):
        self.last_cookie = ''
        self.custid = 0
        self.verbose = verbose
        self.TRACKS = {},
        self.CARS = {},
        self.DIVISION = {},
        self.CARCLASS = {},
        self.CLUB = {}

    def __save_cookie(self):

        o = open('cookie.tmp', 'w')
        o.write(self.last_cookie)
        o.write('\n' + str(self.custid))
        o.close()

    def __load_cookie(self):
        try:
            o = open('cookie.tmp', 'r')
            self.last_cookie, self.custid = o.read().split('\n')
            o.close()
            return True
        except Exception:
            print(Exception)
            return False

    def login(self):


        try:
            if self.__load_cookie():
                return True

            r = self.__req(
                ct.URL_IRACING_LOGIN,
                grab_cookie=True
                )

            print(r)

            r = self.__req(
                ct.URL_IRACING_LOGIN2,
                loginData,
                cookie=self.last_cookie,
                grab_cookie=True
                )

            print(r)

            if 'irsso_membersv2' in self.last_cookie:

                r = self.__req(
                    ct.URL_IRACING_HOME,
                    cookie=self.last_cookie
                    )
                r = r.text
                self.__save_cookie()
                return True

            else:
                return False

        except Exception as e:

            return e, False

    def __req(
        self,
        url,
        data=None,
        cookie=None,
        grab_cookie=False,
        useget=False
        ):

        header = ct.HEADERS.copy()

        if (data is None) or useget:
            resp = requests.get(
                url,
                headers=header,
                params=data
                )

        else:
            header['Content-Type'] = 'application/x-www-form-urlencoded;\
                                    charset=UTF-8'
            resp = requests.post(
                url,
                data=data,
                headers=header
                )

        if 'Set-Cookie' in resp.headers and grab_cookie:
            self.last_cookie = resp.headers['Set-Cookie']

            if 'cookie' in resp.request.headers:
                resp_req_cookie = resp.request.headers['cookie']

                self.last_cookie += ';' + resp_req_cookie

        return resp
'''
