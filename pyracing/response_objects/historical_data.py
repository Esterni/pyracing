from ..constants import parse_encode


class EventResults:
    def __init__(self, dict):
        self.bestlaptime = parse_encode(dict['38'])
        self.bestquallaptime = parse_encode(dict['6'])
        self.carclassid = dict['29']
        self.carid = dict['32']
        self.catid = dict['33']
        self.champpoints = dict['40']
        self.champpointssort = dict['43']
        self.clubpoints = dict['16']
        self.clubpointssort = dict['47']
        self.custid = dict['23']
        self.displayname = parse_encode(dict['48'])
        self.dropracepoints = dict['17']
        self.evttype = dict['37']
        self.finishedat = dict['10']
        self.finishing_position = dict['3']
        self.groupname = dict['19']
        self.helm_color1 = dict['1']
        self.helm_color2 = parse_encode(dict['14'])
        self.helm_color3 = parse_encode(dict['13'])
        self.helm_licenselevel = dict['24']
        self.helm_pattern = dict['46']
        self.incidents = dict['39']
        self.licensegroup = dict['35']
        self.officialsession = dict['18']
        self.race_week_num = dict['8']
        self.raw_start_time = dict['11']
        self.rn = dict['26']
        self.season_quarter = dict['34']
        self.season_year = dict['42']
        self.seasonid = dict['22']
        self.seriesid = dict['20']
        self.sesrank = dict['28']
        self.sessionid = dict['9']
        self.start_date = parse_encode(dict['44'])
        self.start_time = parse_encode(dict['21'])
        self.starting_position = dict['12']
        self.strengthoffield = dict['45']
        self.subsession_bestlaptime = parse_encode(dict['7'])
        self.subsessionid = dict['41']
        self.trackid = dict['30']
        self.winnerdisplayname = parse_encode(dict['31'])
        self.winnerhelmcolor1 = parse_encode(dict['5'])
        self.winnerhelmcolor2 = dict['2']
        self.winnerhelmcolor3 = parse_encode(dict['4'])
        self.winnerhelmpattern = dict['36']
        self.winnerlicenselevel = dict['25']
        self.winnersgroupid = dict['27']
        # Another instance of not in dict
        # self.rowcount = dict['15']


class SeasonStandings:
    def __init__(self, dict):
        self.avgfinish = dict['9']
        self.avgstart = dict['8']
        self.clubid = dict['6']
        self.clubname = parse_encode(dict['23'])
        self.country = parse_encode(dict['1'])
        self.countrycode = parse_encode(dict['4'])
        self.custid = dict['28']
        self.displaycountry = dict['32']
        self.displayname = parse_encode(dict['26'])
        self.division = dict['11']
        self.dropped = dict['5']
        self.helmcolor1 = parse_encode(dict['25'])
        self.helmcolor2 = parse_encode(dict['27'])
        self.helmcolor3 = parse_encode(dict['22'])
        self.helmpattern = dict['20']
        self.incidents = dict['13']
        self.irating = dict['3']
        self.laps = dict['7']
        self.lapslead = dict['24']
        self.maxlicenselev = dict['21']
        self.points = dict['10']
        self.poles = dict['19']
        self.pos = dict['30']
        self.rank = dict['14']
        self.rn = dict['31']
        self.starts = dict['15']
        self.sublevel = parse_encode(dict['29'])
        self.topfive = dict['12']
        self.week = dict['2']
        self.wins = dict['17']

        # Used only on webpage to highlight the member in relaton to others
        # self.custrow = dict['16']
        # self.rowcount = dict['18']


class DriverStats:
    def __init__(self, dict):
        self.avefieldsize = dict['13']
        self.avefinishingposition = dict['9']
        self.avestartingposition = dict['8']
        self.avgincidents = dict['26']
        self.avgpoints = dict['27']
        self.clubid = dict['5']
        self.clubname = parse_encode(dict['29'])
        self.clubpoints = dict['21']
        self.countrycode = parse_encode(dict['4'])
        self.custid = dict['34']
        self.displayname = parse_encode(dict['32'])
        self.groupletter = parse_encode(dict['39'])
        self.groupname = parse_encode(dict['24'])
        self.helmcolor1 = parse_encode(dict['31'])
        self.helmcolor2 = parse_encode(dict['33'])
        self.helmcolor3 = parse_encode(dict['28'])
        self.helmfacetype = dict['36']
        self.helmhelmettype = dict['10']
        self.helmpattern = dict['22']
        self.irating = dict['3']
        self.irating_rank = dict['2']
        self.laps = dict['7']
        self.lapslead = dict['30']
        self.licenseclass = parse_encode(dict['16'])
        self.licenseclass_rank = dict['19']
        self.licensegroup = dict['12']
        self.licenselevel = dict['23']
        self.points = dict['11']
        self.rank = dict['14']
        self.region = parse_encode(dict['38'])
        self.rn = dict['37']
        self.starts = dict['15']
        self.sublevel = dict['35']
        self.top25pcnt = dict['1']
        self.ttrating = dict['25']
        self.ttrating_rank = dict['6']
        self.wins = dict['18']
        # These are only used in front end webpage; Not in dict results
        # self.custrow = dict['17']
        # self.rowcount = dict['20']


class WorldRecords:
    def __init__(self, dict):
        self.carid = dict['9']
        self.category = parse_encode(dict['35'])
        self.catid = dict['10']
        self.clubid = dict['7']
        self.clubname = parse_encode(dict['27'])
        self.countrycode = parse_encode(dict['6'])
        self.custid = dict['31']
        self.displayname = parse_encode(dict['29'])
        self.helmcolor1 = parse_encode(dict['28'])
        self.helmcolor2 = parse_encode(dict['30'])
        self.helmcolor3 = parse_encode(dict['26'])
        self.helmpattern = dict['22']
        self.irating = dict['4']
        self.licenseclass = parse_encode(dict['3'])
        self.licensegroup = dict['14']
        self.licenselevel = dict['23']
        self.practice = parse_encode(dict['2'])
        self.practice_start_time = dict['8']
        self.practice_subsessionid = dict['13']
        self.qualify = parse_encode(dict['15'])
        self.qualify_start_time = dict['21']
        self.qualify_subsessionid = ['36']
        self.race = parse_encode(dict['19'])
        self.race_start_time = dict['18']
        self.race_subsessionid = ['11']
        self.region = parse_encode(dict['34'])
        self.rn = dict['33']
        self.season_quarter = parse_encode(dict['12'])
        self.season_year = parse_encode(dict['17'])
        self.sublevel = dict['32']
        self.timetrial = parse_encode(dict['37'])
        self.timetrial_start_time = dict['25']
        self.timetrial_subsessionid = ['1']
        self.trackid = dict['5']
        self.ttrating = dict['24']
        # Data not used in the 'r' dictionary. Only for webpage display.
        # self.custrow = dict['16']
        # self.rowcount = dict['20']


class PrivateResults:
    def __init__(self, dict):
        self.bestlaptime = dict['bestlaptime']
        self.carclassid = dict['carclassid']
        self.carids = dict['carids']
        self.catid = dict['catid']
        self.classfinishingposition = dict['classfinishingposition']
        self.classstartingposition = dict['classstartingposition']
        self.created = dict['created']
        self.finishingposition = dict['finishingposition']
        self.fixed_setup = dict['fixed_setup']
        self.fullcoursecautions = dict['fullcoursecautions']
        self.hardcorelevel = dict['hardcorelevel']
        self.host_custid = dict['host_custid']
        self.host_displayname = dict['host_displayname']
        self.host_helmet_color1 = dict['host_helmet_color1']
        self.host_helmet_color2 = dict['host_helmet_color2']
        self.host_helmet_color3 = dict['host_helmet_color3']
        self.host_helmet_facetype = dict['host_helmet_facetype']
        self.host_helmet_helmettype = dict['host_helmet_helmettype']
        self.host_helmet_pattern = dict['host_helmet_pattern']
        self.host_licenselevel = dict['host_licenselevel']
        self.incidents = dict['incidents']
        self.lonequalify = dict['lonequalify']
        self.max_pct_fuel_fills = dict['max_pct_fuel_fills']
        self.maxdrivers = dict['maxdrivers']
        self.maxir = dict['maxir']
        self.maxliclevel = dict['maxliclevel']
        self.minir = dict['minir']
        self.minliclevel = dict['minliclevel']
        self.multiclass = dict['multiclass']
        self.numfasttows = dict['numfasttows']
        self.practicelength = dict['practicelength']
        self.private = dict['private']
        self.privatesessionid = dict['privatesessionid']
        self.qualifylaps = dict['qualifylaps']
        self.qualifylength = dict['qualifylength']
        self.qualsetupfilenames = dict['qualsetupfilenames']
        self.qualsetupids = dict['qualsetupids']
        self.racefinishedat = dict['racefinishedat']
        self.racelaps = dict['racelaps']
        self.racelength = dict['racelength']
        self.racesetupfilenames = dict['racesetupfilenames']
        self.racesetupids = dict['racesetupids']
        self.restarts = dict['restarts']
        self.rn = dict['rn']
        self.rollingstarts = dict['rollingstarts']
        self.sessionfastlap = dict['sessionfastlap']
        self.sessionid = dict['sessionid']
        self.sessionname = dict['sessionname']
        self.start_time = dict['start_time']
        self.startingposition = dict['startingposition']
        self.subsessionfinishedat = dict['subsessionfinishedat']
        self.subsessionid = dict['subsessionid']
        self.timeofday = dict['timeofday']
        self.track_name = dict['track_name']
        self.trackid = dict['trackid']
        self.weather_fog_density = dict['weather_fog_density']
        self.weather_rh = dict['weather_rh']
        self.weather_skies = dict['weather_skies']
        self.weather_temp_units = dict['weather_temp_units']
        self.weather_temp_value = dict['weather_temp_value']
        self.weather_type = dict['weather_type']
        self.weather_wind_dir = dict['weather_wind_dir']
        self.weather_wind_speed_units = dict['weather_wind_speed_units']
        self.weather_wind_speed_value = dict['weather_wind_speed_value']
        self.weight_penalties = dict['weight_penalties']
        self.winner_displayname = dict['winner_displayname']
        self.winner_displaynames = dict['winner_displaynames']
        self.winner_helmet_color1 = dict['winner_helmet_color1']
        self.winner_helmet_color2 = dict['winner_helmet_color2']
        self.winner_helmet_color3 = dict['winner_helmet_color3']
        self.winner_helmet_pattern = dict['winner_helmet_pattern']
        self.winner_licenselevel = dict['winner_licenselevel']
        self.winnersgroupid = dict['winnersgroupid']


class SeriesRaceResults:
    def __init__(self, dict):
        self.carclassid = dict['2']
        self.officialsession = dict['6']
        self.sessionid = dict['4']
        self.sizeoffield = dict['7']
        self.start_time = dict['1']
        self.strengthoffield = dict['8']
        self.subsessionid = dict['5']
        self.trackid = dict['3']


class Team:
    def __init__(self, dict):
        self.avgclassfinishingposition = dict['avgclassfinishingposition']
        self.avgclasssizeoffield = dict['avgclasssizeoffield']
        self.avgclassstartingposition = dict['avgclassstartingposition']
        self.avgclassstrengthoffield = dict['avgclassstrengthoffield']
        self.avgeventfinishingposition = dict['avgeventfinishingposition']
        self.avgeventsizeoffield = dict['avgeventsizeoffield']
        self.avgeventstartingposition = dict['avgeventstartingposition']
        self.avgeventstrengthoffield = dict['avgeventstrengthoffield']
        self.cars = dict['cars']
        self.classpoles = dict['classpoles']
        self.classtop10pcnt = dict['classtop10pcnt']
        self.classtop25pcnt = dict['classtop25pcnt']
        self.classtopfive = dict['classtopfive']
        self.classwins = dict['classwins']
        self.color1 = dict['color1']
        self.color2 = dict['color2']
        self.color3 = dict['color3']
        self.custid = dict['custid']
        self.eventpoles = dict['eventpoles']
        self.eventtop10pcnt = dict['eventtop10pcnt']
        self.eventtop25pcnt = dict['eventtop25pcnt']
        self.eventtopfive = dict['eventtopfive']
        self.eventwins = dict['eventwins']
        self.facetype = dict['facetype']
        self.helmettype = dict['helmettype']
        self.incidents = dict['incidents']
        self.lapscomplete = dict['lapscomplete']
        self.lapslead = dict['lapslead']
        self.licenselevel = dict['licenselevel']
        self.name = dict['name']
        self.pattern = dict['pattern']
        self.team_ranking = dict['team_ranking']
        self.teamid = dict['teamid']
        self.weekdropped = dict['weekdropped']
        self.weekpoints = dict['weekpoints']
        self.weekstarts = dict['weekstarts']
