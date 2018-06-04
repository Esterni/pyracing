#!/usr/bin/python
""" iRWebStats class. Check examples.py for example usage. """
__author__ = "Jeyson Molina"
__email__ = "jjmc82@gmail.com"
__version__ = "1.0"

import urllib
import urllib.parse
encode = urllib.parse.urlencode
from io import StringIO

import requests
import datetime
import csv
import time

from ir_webstats_rc import constants as ct
from ir_webstats_rc.util import *


class iRWebStats:

    """ Use this class to connect to iRacing website and request some stats
        from drivers, races and series. It needs to be logged in the
        iRacing membersite so valid login crendentials (user, password)
        are required. Most  data is returned in JSON format and
        converted to python dicts. """

    def __init__(self, verbose=True):
        self.last_cookie = ''
        self.logged = False
        self.custid = 0
        self.verbose = verbose
        self.TRACKS, self.CARS, self.DIVISION, self.CARCLASS, self.CLUB = {},\
            {}, {}, {}, {}

    def __save_cookie(self):
        """ Saves the current cookie to disk from a successful login to avoid
            future login procedures and save time. A cookie usually last
            at least a couple of hours """

        pprint("Saving cookie for future use", self.verbose)
        o = open('cookie.tmp', 'w')
        o.write(self.last_cookie)
        o.write('\n' + str(self.custid))
        o.close()

    def __load_cookie(self):
        """ Loads a previously saved cookie """
        try:
            o = open('cookie.tmp', 'r')
            self.last_cookie, self.custid = o.read().split('\n')
            o.close()
            return True
        except:
            return False

    def login(self, username='', password='', get_info=False):
        """ Log in to iRacing members site. If there is a valid cookie saved
            then it tries to use it to avoid a new login request. Returns
            True is the login was succesful and stores the customer id
            (custid) of the current login in self.custid. """

        if self.logged:
            return True
        data = {"username": username, "password": password, 'utcoffset': 300,
                'todaysdate': ''}
        try:
            pprint("Loggin in...", self.verbose)
            # Check if there's a previous cookie
            if (self.__load_cookie() and self.__check_cookie()):
                #  If previous cookie is valid
                pprint("Previous cookie valid", self.verbose)
                self.logged = True
                if get_info:
                  # Load iracing info
                  self.__get_irservice_info(self.__req(ct.URL_IRACING_HOME,
                                                       cookie=self.last_cookie))
                # TODO Should we cache this?
                return self.logged
            self.custid = ''
            r = self.__req(ct.URL_IRACING_LOGIN, grab_cookie=True)
            r = self.__req(ct.URL_IRACING_LOGIN2, data,
                           cookie=self.last_cookie, grab_cookie=True)

            if 'irsso_members' in self.last_cookie:
                ind = r.index('js_custid')
                custid = int(r[ind + 11: r.index(';', ind)])
                self.custid = custid
                pprint(("CUSTID", self.custid), self.verbose)
                self.logged = True
                self.__get_irservice_info(r)
                self.__save_cookie()
                pprint("Log in succesful", self.verbose)
            else:
                pprint("Invalid Login (user: %s). Please check your\
                        credentials" % (username), self.verbose)
                self.logged = False

        except Exception as e:
            pprint(("Error on Login Request", e), self.verbose)
            self.logged = False
        return self.logged

    def logout(self):
        self.logged = False  # TODO proper logout

    def __check_cookie(self):
        """ Checks the cookie by testing a request response"""

        r = parse(self.__req(ct.URL_DRIVER_COUNTS, cookie=self.last_cookie))
        if isinstance(r, dict):
            return True
        return False

    def __req(self, url, data=None, cookie=None, grab_cookie=False,
              useget=False):
        """ Creates and sends the HTTP requests to iRacing site """

        # Sleep/wait to avoid flooding the service with requests
        time.sleep(ct.WAIT_TIME)  # 0.3 seconds
        h = ct.HEADERS.copy()
        if cookie is not None:  # Send the cookie
            h['Cookie'] = cookie
        elif len(self.last_cookie):
            h['Cookie'] = self.last_cookie

        if (data is None) or useget:
            resp = requests.get(url, headers=h, params=data)
        else:
            h['Content-Type'] = 'application/x-www-form-urlencoded;\
                    charset=UTF-8'
            resp = requests.post(url, data=data, headers=h)
        if 'Set-Cookie' in resp.headers and grab_cookie:
            self.last_cookie = resp.headers['Set-Cookie']
            # Must get irsso_members from another header
            if 'cookie' in resp.request.headers:
                resp_req_cookie = resp.request.headers['cookie']
                self.last_cookie += ';' + resp_req_cookie
        html = resp.text
        return html

    def __get_irservice_info(self, resp):
        """ Gets general information from iracing service like current tracks,
            cars, series, etc. Check self.TRACKS, self.CARS, self.DIVISION
            , self.CARCLASS, self.CLUB. """

        pprint("Getting iRacing Service info (cars, tracks, etc.)",
               self.verbose)
        items = {"TRACKS":  "TrackListing", "CARS": "CarListing",
                 "CARCLASS":  "CarClassListing", "CLUBS": "ClubListing",
                 "SEASON": "SeasonListing", "DIVISION": "DivisionListing",
                 "YEARANDQUARTER": "YearAndQuarterListing"}
        for i in items:
            str2find = "var " + items[i] + " = extractJSON('"
            try:
                ind1 = resp.index(str2find)
                json_o = resp[ind1 + len(str2find): resp.index("');", ind1)]\
                    .replace('+', ' ')
                o = json.loads(json_o)
                if i not in ("SEASON", "YEARANDQUARTER"):
                    o = {ele['id']: ele for ele in o}
                setattr(self, i, o)  # i.e self.TRACKS = o

            except Exception as e:
                pprint("Error ocurred. Couldn't get {}".format(i), self.verbose)

    def _load_irservice_var(self, varname, resp, appear=1):
        str2find = "var " + varname + " = extractJSON('"
        ind1 = -1
        for _ in range(appear):
            ind1 = resp.index(str2find, ind1+1)
        json_o = resp[ind1 + len(str2find): resp.index("');", ind1)]\
            .replace('+', ' ')
        o = json.loads(json_o)
        if varname not in ("SeasonListing", "YEARANDQUARTER"):
            o = {ele['id']: ele for ele in o}
        return o

    @logged_in
    def iratingchart(self, custid=None, category=ct.IRATING_ROAD_CHART):
        """ Gets the irating data of a driver using its custom id (custid)
            that generates the chart located in the driver's profile. """

        r = self.__req(ct.URL_STATS_CHART % (custid, category),
                       cookie=self.last_cookie)
        return parse(r)

    @logged_in
    def driver_counts(self):
        """ Gets list of connected myracers and notifications. """
        r = self.__req(ct.URL_DRIVER_COUNTS, cookie=self.last_cookie)
        return parse(r)

    @logged_in
    def career_stats(self, custid=None):
        """ Gets career stats (top5, top 10, etc.) of driver (custid)."""
        r = self.__req(ct.URL_CAREER_STATS % (custid),
                       cookie=self.last_cookie)
        return parse(r)[0]

    @logged_in
    def yearly_stats(self, custid=None):
        """ Gets yearly stats (top5, top 10, etc.) of driver (custid)."""
        r = self.__req(ct.URL_YEARLY_STATS % (custid),
                       cookie=self.last_cookie)
        # tofile(r)
        return parse(r)

    @logged_in
    def cars_driven(self, custid=None):
        """ Gets list of cars driven by driver (custid)."""
        r = self.__req(ct.URL_CARS_DRIVEN % (custid),
                       cookie=self.last_cookie)
        # tofile(r)
        return parse(r)

    @logged_in
    def personal_best(self, custid=None, carid=0):
        """ Personal best times of driver (custid) using car
            (carid. check self.CARS) set in official events."""
        r = self.__req(ct.URL_PERSONAL_BEST % (carid, custid),
                       cookie=self.last_cookie)
        return parse(r)

    @logged_in
    def driverdata(self, drivername):
        """ Personal data of driver  using its name in the request
            (i.e drivername="Victor Beltran"). """

        r = self.__req(ct.URL_DRIVER_STATUS % (encode({
            'searchTerms': drivername})), cookie=self.last_cookie)
        # tofile(r)
        return parse(r)

    @logged_in
    def lastrace_stats(self, custid=None):
        """ Gets stats of last races (10 max?) of driver (custid)."""
        r = self.__req(ct.URL_LASTRACE_STATS % (custid),
                       cookie=self.last_cookie)
        return parse(r)

    @logged_in
    def driver_search(self, race_type=ct.RACE_TYPE_ROAD, location=ct.LOC_ALL,
                      license=(ct.LIC_ROOKIE, ct.ALL), irating=(0, ct.ALL),
                      ttrating=(0, ct.ALL), avg_start=(0, ct.ALL),
                      avg_finish=(0, ct.ALL), avg_points=(0, ct.ALL),
                      avg_incs=(0, ct.ALL), active=False,
                      sort=ct.SORT_IRATING, page=1, order=ct.ORDER_DESC):
        """Search drivers using several search fields. A tuple represent a
           range (i.e irating=(1000, 2000) gets drivers with irating
           between 1000 and 2000). Use ct.ALL used in the lower or
           upperbound of a range disables that limit. Returns a tuple
           (results, total_results) so if you want all results you should
           request different pages (using page) until you gather all
           total_results. Each page has 25 (ct.NUM_ENTRIES) results max."""

        lowerbound = ct.NUM_ENTRIES * (page - 1) + 1
        upperbound = lowerbound + ct.NUM_ENTRIES - 1
        search = 'null'
        friend = ct.ALL  # TODO
        studied = ct.ALL  # TODO
        recent = ct.ALL  # TODO

        active = int(active)
        # Data to POST
        data = {'custid': self.custid, 'search': search, 'friend': friend,
                'watched': studied, 'country': location, 'recent': recent,
                'category': race_type, 'classlow': license[0],
                'classhigh': license[1], 'iratinglow': irating[0],
                'iratinghigh': irating[1], 'ttratinglow': ttrating[0],
                'ttratinghigh': ttrating[1], 'avgstartlow': avg_start[0],
                'avgstarthigh': avg_start[1], 'avgfinishlow': avg_finish[0],
                'avgfinishhigh': avg_finish[1], 'avgpointslow': avg_points[0],
                'avgpointshigh': avg_points[1], 'avgincidentslow':
                avg_incs[0], 'avgincidentshigh': avg_incs[1],
                'lowerbound': lowerbound, 'upperbound': upperbound,
                'sort': sort, 'order': order, 'active': active}

        total_results, drivers = 0, {}

        try:
            r = self.__req(ct.URL_DRIVER_STATS, data=data,
                           cookie=self.last_cookie)
            res = parse(r)
            total_results = res['d'][list(res['m'].keys())[list(res['m'].values()).index('rowcount')]]
            custid_id = list(res['m'].keys())[list(res['m'].values()).index('rowcount')]
            header = res['m']
            f = res['d']['r'][0]
            if int(f[custid_id]) == int(self.custid):
                drivers = res['d']['r'][1:]
            else:
                drivers = res['d']['r']
            drivers = format_results(drivers, header)

        except Exception as e:
            pprint(("Error fetching driver search data. Error:", e),
                   self.verbose)

        return drivers, total_results

    def test(self, a, b=2, c=3):
        return a, b, c

    @logged_in
    def results_archive(self, custid=None, race_type=ct.RACE_TYPE_ROAD,
                        event_types=ct.ALL, official=ct.ALL,
                        license_level=ct.ALL, car=ct.ALL, track=ct.ALL,
                        series=ct.ALL, season=(2016, 3, ct.ALL),
                        date_range=ct.ALL, page=1, sort=ct.SORT_TIME,
                        order= ct.ORDER_DESC):
        """ Search race results using various fields. Returns a tuple
            (results, total_results) so if you want all results you should
            request different pages (using page). Each page has 25
            (ct.NUM_ENTRIES) results max."""

        format_ = 'json'
        lowerbound = ct.NUM_ENTRIES * (page - 1) + 1
        upperbound = lowerbound + ct.NUM_ENTRIES - 1
        #  TODO carclassid, seriesid in constants
        data = {'format': format_, 'custid': custid, 'seriesid': series,
                'carid': car, 'trackid': track, 'lowerbound': lowerbound,
                'upperbound': upperbound, 'sort': sort, 'order': order,
                'category': race_type, 'showtts': 0, 'showraces': 0,
                'showquals': 0, 'showops': 0, 'showofficial': 0,
                'showunofficial': 0, 'showrookie': 0, 'showclassa': 0,
                'showclassb': 0, 'showclassc': 0, 'showclassd': 0,
                'showpro': 0, 'showprowc': 0, }
        # Events
        ev_vars = {ct.EVENT_RACE: 'showraces', ct.EVENT_QUALY: 'showquals',
                   ct.EVENT_PRACTICE: 'showops', ct.EVENT_TTRIAL: 'showtts'}
        if event_types == ct.ALL:
            event_types = (ct.EVENT_RACE, ct.EVENT_QUALY, ct.EVENT_PRACTICE,
                           ct.EVENT_TTRIAL)

        for v in event_types:
            data[ev_vars[v]] = 1
        # Official, unofficial
        if official == ct.ALL:
            data['showofficial'] = 1
            data['showunoofficial'] = 1
        else:
            if ct.EVENT_UNOFFICIAL in official:
                data['showunofficial'] = 1
            if ct.EVENT_OFFICIAL in official:
                data['showofficial'] = 1

        # Season
        if date_range == ct.ALL:
            data['seasonyear'] = season[0]
            data['seasonquarter'] = season[1]
            if season[2] != ct.ALL:
                data['raceweek'] = season[2]
        else:
            # Date range
            tc = lambda s:\
                time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").
                            timetuple()) * 1000
            data['starttime_low'] = tc(date_range[0])  # multiplied by 1000
            data['starttime_high'] = tc(date_range[1])

        # License levels
        lic_vars = {ct.LIC_ROOKIE: 'showrookie', ct.LIC_A: 'showclassa',
                    ct.LIC_B: 'showclassb', ct.LIC_C: 'showclassc',
                    ct.LIC_D: 'showclassd', ct.LIC_PRO: 'showpro',
                    ct.LIC_PRO_WC: 'showprowc'}

        if license_level == ct.ALL:
            license_level = (ct.LIC_ROOKIE, ct.LIC_A, ct.LIC_B, ct.LIC_C,
                             ct.LIC_D, ct.LIC_PRO, ct.LIC_PRO_WC)
        for v in license_level:
            data[lic_vars[v]] = 1
        r = self.__req(ct.URL_RESULTS_ARCHIVE, data=data,
                       cookie=self.last_cookie)
        res = parse(r)
        total_results = res['d'][list(res['m'].keys())[list(res['m'].values()).index('rowcount')]]
        results = []
        if total_results > 0:
            results = res['d']['r']
            header = res['m']
            results = format_results(results, header)

        return results, total_results

    @logged_in
    def all_seasons(self):
        """ Get All season data available at Series Stats page
        """
        pprint("Getting iRacing Seasons with Stats")
        resp = self.__req(ct.URL_SEASON_STANDINGS2)
        return self._load_irservice_var("SeasonListing", resp)

    @logged_in
    def season_standings(self, season, carclass, club=ct.ALL, raceweek=ct.ALL,
                         division=ct.ALL, sort=ct.SORT_POINTS,
                         order=ct.ORDER_DESC, page=1):
        """ Search season standings using various fields. season, carclass
            and club are ids.  Returns a tuple (results, total_results) so
            if you want all results you should request different pages
            (using page)  until you gather all total_results. Each page has
            25 results max."""

        lowerbound = ct.NUM_ENTRIES * (page - 1) + 1
        upperbound = lowerbound + ct.NUM_ENTRIES - 1

        data = {'sort': sort, 'order': order, 'seasonid': season,
                'carclassid': carclass, 'clubid': club, 'raceweek': raceweek,
                'division': division, 'start': lowerbound, 'end': upperbound}
        r = self.__req(ct.URL_SEASON_STANDINGS, data=data)
        res = parse(r)
        total_results = res['d'][list(res['m'].keys())[list(res['m'].values()).index('rowcount')]]
        results = res['d']['r']
        header = res['m']
        results = format_results(results, header)

        return results, total_results

    @logged_in
    def hosted_results(self, session_host=None, session_name=None,
                       date_range=None, sort=ct .SORT_TIME,
                       order=ct.ORDER_DESC, page=1):
        """ Search hosted races results using various fields. Returns a tuple
            (results, total_results) so if you want all results you should
            request different pages (using page) until you gather all
            total_results. Each page has 25 (ct.NUM_ENTRIES) results max."""

        lowerbound = ct.NUM_ENTRIES * (page - 1) + 1
        upperbound = lowerbound + ct.NUM_ENTRIES - 1

        data = {'sort': sort, 'order': order, 'lowerbound': lowerbound,
                'upperbound': upperbound}
        if session_host is not None:
            data['sessionhost'] = session_host
        if session_name is not None:
            data['sessionname'] = session_name

        if date_range is not None:
            # Date range
            tc = lambda s:\
                time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").
                            timetuple()) * 1000
            data['starttime_lowerbound'] = tc(date_range[0])
            # multiplied by 1000
            data['starttime_upperbound'] = tc(date_range[1])

        r = self.__req(ct.URL_HOSTED_RESULTS, data=data)
        # tofile(r)
        res = parse(r)
        total_results = res['rowcount']
        results = res['rows']  # doesn't need format_results
        return results, total_results

    @logged_in
    def session_times(self, series_season, start, end):
        """ Gets Current and future sessions (qualy, practice, race)
            of series_season """
        r = self.__req(ct.URL_SESSION_TIMES, data={'start': start, 'end': end,
                       'season': series_season}, useget=True)
        return parse(r)

    @logged_in
    def season_race_sessions(self, season, raceweek):
        """ Gets races sessions for season in specified raceweek """

        r = self.__req(ct.URL_SERIES_RACERESULTS, data={'seasonid': season,
                       'raceweek': raceweek})  # TODO no bounds?
        res = parse(r)
        try:
            header = res['m']
            results = res['d']
            results = format_results(results, header)
            return results
        except TypeError:
            print(res)
            return None

    @logged_in
    def event_results(self, subsession, sessnum=0):
        """ Gets the event results (table of positions, times, etc.). The
            event is identified by a subsession id. """

        r = self.__req(ct.URL_GET_EVENTRESULTS % (subsession, sessnum)).encode('utf8').decode('utf-8')
        data = [x for x in csv.reader(StringIO(r), delimiter=',', quotechar='"')]
        header_res = []
        for header in data[3]:
            header_res.append("".join([c for c in header.lower() if ord(c) > 96 and ord(c) < 123]))
        header_ev = data[0]
        for i in range(4, len(data)):
            for j in range(len(data[i])):
                if data[i][j] == '':
                    data[i][j] = None
                elif data[i][j].isnumeric():
                    data[i][j] = int(data[i][j])
        event_info = dict(list(zip(header_ev, data[1])))
        results = [dict(list(zip(header_res, x))) for x in data[4:]]

        return event_info, results

    @logged_in
    def event_results2(self, subsession, custid):
        """ Get the event results from the web page rather than CSV.
        Required to get ttRating for time trials """

        r = self.__req(ct.URL_GET_EVENTRESULTS2 % (subsession, custid))

        resp = re.sub('\t+',' ',r)
        resp = re.sub('\r\r\n+',' ',resp)
        resp = re.sub('\s+',' ',resp)

        str2find = "var resultOBJ ="
        ind1 = resp.index(str2find)
        ind2 = resp.index("};", ind1) + 1
        resp = resp[ind1 + len(str2find): ind2].replace('+', ' ')

        ttitems = ("custid", "isOfficial", "carID", "avglaptime", "fastestlaptime", "fastestlaptimems", "fastestlapnum", "bestnlapstime", "bestnlapsnum", "lapscomplete", "incidents", "newttRating", "oldttRating", "sr_new", "sr_old", "reasonOutName")
        out = ""
        for ttitem in ttitems:
            ind1 = resp.index(ttitem)
            ind2 = resp.index(",", ind1) + 1
            out = out + resp[ind1: ind2]

        out = re.sub(r"{\s*(\w)", r'{"\1', out)
        out = re.sub(r",\s*(\w)", r',"\1', out)
        out = re.sub(r"(\w):", r'\1":', out)
        out = re.sub(r":\"(\d)\":", r':"\1:', out)
        out = re.sub(r"parseFloat\((\"\d\.\d\d\")\)", r'\1', out)

        out = out.strip().rstrip(',')
        out = "{\"" + out + "}"
        out = json.loads(out)

        return out

    def subsession_results(self, subsession):
        """ Get the results for a time trial event from the web page.
        """

        r = self.__req(ct.URL_GET_SUBSESSRESULTS % (subsession), useget=True)

        out = parse(r)['rows']

        return out

    def event_laps_single(self, subsession, custid, sessnum=0):
        """ Get the lap times for an event from the web page. 
        """

        r = self.__req(ct.URL_GET_LAPS_SINGLE % (subsession, custid, sessnum))
                         
        out = parse(r)

        return out

    def event_laps_all(self, subsession):
        """ Get the lap times for an event from the web page. 
        """

        r = self.__req(ct.URL_GET_LAPS_ALL % subsession)
                         
        out = parse(r)

        return out

    def best_lap(self, subsessionid, custid):
        """ Get the best lap time for a driver from an event. 
        """
        
        laptime = self.event_laps_single(subsessionid, custid)['drivers'][0]['bestlaptime']
        
        return laptime

    def world_record(self, seasonyear, seasonquarter, carid, trackid, custid):
        """ Get the world record lap time for certain car in a season. 
        """

        r = self.__req(ct.URL_GET_WORLDRECORD % (seasonyear, seasonquarter, carid, trackid, custid))
        res = parse(r)
        
        header = res['m']
        try:
            results = res['d']['r'][1]
            newr = dict()
            for k, v  in results.items():
                newr[header[k]] = v
                
            if newr['race'].find("%3A") > -1:
                t = datetime.datetime.strptime(newr['race'], "%M%%3A%S.%f")
                record = (t.minute * 60) + t.second + (t.microsecond / 1000000)
            else:
                record = float(newr['race'])
        except:
            record = None
        
        return record    
    
if __name__ == '__main__':
    irw = iRWebStats()
    user, passw = ('username', 'password')
    irw.login(user, passw)
    print("Cars Driven", irw.cars_driven())  # example usage
