from ..constants import parse_iracing_string


class EventResults:
    def __init__(self, dict):
        self.helm_color1 = dict['1']
        self.winnerhelmcolor2 = dict['2']
        self.finishing_position = dict['3']
        self.winnerhelmcolor3 = parse_iracing_string(dict['4'])
        self.winnerhelmcolor1 = parse_iracing_string(dict['5'])
        self.bestquallaptime = parse_iracing_string(dict['6'])
        self.subsession_bestlaptime = parse_iracing_string(dict['7'])
        self.race_week_num = dict['8']
        self.sessionid = dict['9']
        self.finishedat = dict['10']
        self.raw_start_time = dict['11']
        self.starting_position = dict['12']
        self.helm_color3 = parse_iracing_string(dict['13'])
        self.helm_color2 = parse_iracing_string(dict['14'])
        self.clubpoints = dict['16']
        self.dropracepoints = dict['17']
        self.officialsession = dict['18']
        self.groupname = dict['19']
        self.seriesid = dict['20']
        self.start_time = parse_iracing_string(dict['21'])
        self.seasonid = dict['22']
        self.custid = dict['23']
        self.helm_licenselevel = dict['24']
        self.winnerlicenselevel = dict['25']
        self.rn = dict['26']
        self.winnersgroupid = dict['27']
        self.sesrank = dict['28']
        self.carclassid = dict['29']
        self.trackid = dict['30']
        self.winnerdisplayname = parse_iracing_string(dict['31'])
        self.carid = dict['32']
        self.catid = dict['33']
        self.season_quarter = dict['34']
        self.licensegroup = dict['35']
        self.winnerhelmpattern = dict['36']
        self.evttype = dict['37']
        self.bestlaptime = parse_iracing_string(dict['38'])
        self.incidents = dict['39']
        self.champpoints = dict['40']
        self.subsessionid = dict['41']
        self.season_year = dict['42']
        self.champpointssort = dict['43']
        self.start_date = parse_iracing_string(dict['44'])
        self.strengthoffield = dict['45']
        self.helm_pattern = dict['46']
        self.clubpointssort = dict['47']
        self.displayname = parse_iracing_string(dict['48'])
        # Another instance of not in dict
        # self.rowcount = dict['15']


class SeasonStandings:
    def __init__(self, dict):
        self.country = parse_iracing_string(dict['1'])
        self.week = dict['2']
        self.irating = dict['3']
        self.countrycode = parse_iracing_string(dict['4'])
        self.dropped = dict['5']
        self.clubid = dict['6']
        self.laps = dict['7']
        self.avgstart = dict['8']
        self.avgfinish = dict['9']
        self.points = dict['10']
        self.division = dict['11']
        self.topfive = dict['12']
        self.incidents = dict['13']
        self.rank = dict['14']
        self.starts = dict['15']
        self.wins = dict['17']
        self.poles = dict['19']
        self.helmpattern = dict['20']
        self.maxlicenselev = dict['21']
        self.helmcolor3 = parse_iracing_string(dict['22'])
        self.clubname = parse_iracing_string(dict['23'])
        self.lapslead = dict['24']
        self.helmcolor1 = parse_iracing_string(dict['25'])
        self.displayname = parse_iracing_string(dict['26'])
        self.helmcolor2 = parse_iracing_string(dict['27'])
        self.custid = dict['28']
        self.sublevel = parse_iracing_string(dict['29'])
        self.pos = dict['30']
        self.rn = dict['31']
        self.displaycountry = dict['32']

        # Used only on webpage to highlight the member in relaton to others
        # self.custrow = dict['16']
        # self.rowcount = dict['18']


class DriverStats:
    def __init__(self, dict):
        self.top25pcnt = dict['1']
        self.irating_rank = dict['2']
        self.irating = dict['3']
        self.countrycode = parse_iracing_string(dict['4'])
        self.clubid = dict['5']
        self.ttrating_rank = dict['6']
        self.laps = dict['7']
        self.avestartingposition = dict['8']
        self.avefinishingposition = dict['9']
        self.helmhelmettype = dict['10']
        self.points = dict['11']
        self.licensegroup = dict['12']
        self.avefieldsize = dict['13']
        self.rank = dict['14']
        self.starts = dict['15']
        self.licenseclass = parse_iracing_string(dict['16'])
        # 17 only exists in the dict level up for highlighting custid
        # self.custrow = dict['17']
        self.wins = dict['18']
        self.licenseclass_rank = dict['19']
        # 20 only exists in the dict level up for identifying total rows
        # self.rowcount = dict['20']
        self.clubpoints = dict['21']
        self.helmpattern = dict['22']
        self.licenselevel = dict['23']
        self.groupname = parse_iracing_string(dict['24'])
        self.ttrating = dict['25']
        self.avgincidents = dict['26']
        self.avgpoints = dict['27']
        self.helmcolor3 = parse_iracing_string(dict['28'])
        self.clubname = parse_iracing_string(dict['29'])
        self.lapslead = dict['30']
        self.helmcolor1 = parse_iracing_string(dict['31'])
        self.displayname = parse_iracing_string(dict['32'])
        self.helmcolor2 = parse_iracing_string(dict['33'])
        self.custid = dict['34']
        self.sublevel = dict['35']
        self.helmfacetype = dict['36']
        self.rn = dict['37']
        self.region = parse_iracing_string(dict['38'])
        self.groupletter = parse_iracing_string(dict['39'])


class WorldRecords:
    def __init__(self, dict):
        self.timetrial_subsessionid = ['1']
        self.practice = parse_iracing_string(dict['2'])
        self.licenseclass = parse_iracing_string(dict['3'])
        self.irating = dict['4']
        self.trackid = dict['5']
        self.countrycode = parse_iracing_string(dict['6'])
        self.clubid = dict['7']
        self.practice_start_time = dict['8']
        self.carid = dict['9']
        self.catid = dict['10']
        self.race_subsessionid = ['11']
        self.season_quarter = parse_iracing_string(dict['12'])
        self.practice_subsessionid = dict['13']
        self.licensegroup = dict['14']
        self.qualify = parse_iracing_string(dict['15'])
        self.season_year = parse_iracing_string(dict['17'])
        self.race_start_time = dict['18']
        self.race = parse_iracing_string(dict['19'])
        self.qualify_start_time = dict['21']
        self.helmpattern = dict['22']
        self.licenselevel = dict['23']
        self.ttrating = dict['24']
        self.timetrial_start_time = dict['25']
        self.helmcolor3 = parse_iracing_string(dict['26'])
        self.clubname = parse_iracing_string(dict['27'])
        self.helmcolor1 = parse_iracing_string(dict['28'])
        self.displayname = parse_iracing_string(dict['29'])
        self.helmcolor2 = parse_iracing_string(dict['30'])
        self.custid = dict['31']
        self.sublevel = dict['32']
        self.rn = dict['33']
        self.region = parse_iracing_string(dict['34'])
        self.category = parse_iracing_string(dict['35'])
        self.qualify_subsessionid = ['36']
        self.timetrial = parse_iracing_string(dict['37'])
        # Data not used in the 'r' dictionary. Only for webpage display.
        # self.custrow = dict['16']
        # self.rowcount = dict['20']


class PrivateResults:
    def __init__(self, dict):
        self.weather_temp_units = dict['weather_temp_units']
        self.weather_wind_dir = dict['weather_wind_dir']
        self.weather_temp_value = dict['weather_temp_value']
        self.privatesessionid = dict['privatesessionid']
        self.sessionid = dict['sessionid']
        self.practicelength = dict['practicelength']
        self.sessionname = dict['sessionname']
        self.winner_licenselevel = dict['winner_licenselevel']
        self.hardcorelevel = dict['hardcorelevel']
        self.carids = dict['carids']
        self.racesetupfilenames = dict['racesetupfilenames']
        self.host_helmet_color1 = dict['host_helmet_color1']
        self.host_helmet_color2 = dict['host_helmet_color2']
        self.weight_penalties = dict['weight_penalties']
        self.host_helmet_color3 = dict['host_helmet_color3']
        self.qualifylength = dict['qualifylength']
        self.maxir = dict['maxir']
        self.weather_fog_density = dict['weather_fog_density']
        self.startingposition = dict['startingposition']
        self.max_pct_fuel_fills = dict['max_pct_fuel_fills']
        self.host_licenselevel = dict['host_licenselevel']
        self.created = dict['created']
        self.host_custid = dict['host_custid']
        self.restarts = dict['restarts']
        self.start_time = dict['start_time']
        self.timeofday = dict['timeofday']
        self.racefinishedat = dict['racefinishedat']
        self.host_displayname = dict['host_displayname']
        self.numfasttows = dict['numfasttows']
        self.rn = dict['rn']
        self.winner_displayname = dict['winner_displayname']
        self.racelaps = dict['racelaps']
        self.winnersgroupid = dict['winnersgroupid']
        self.private = dict['private']
        self.carclassid = dict['carclassid']
        self.classfinishingposition = dict['classfinishingposition']
        self.trackid = dict['trackid']
        self.weather_type = dict['weather_type']
        self.minir = dict['minir']
        self.fixed_setup = dict['fixed_setup']
        self.qualifylaps = dict['qualifylaps']
        self.weather_skies = dict['weather_skies']
        self.rollingstarts = dict['rollingstarts']
        self.subsessionfinishedat = dict['subsessionfinishedat']
        self.catid = dict['catid']
        self.maxdrivers = dict['maxdrivers']
        self.fullcoursecautions = dict['fullcoursecautions']
        self.racesetupids = dict['racesetupids']
        self.qualsetupfilenames = dict['qualsetupfilenames']
        self.bestlaptime = dict['bestlaptime']
        self.finishingposition = dict['finishingposition']
        self.incidents = dict['incidents']
        self.subsessionid = dict['subsessionid']
        self.qualsetupids = dict['qualsetupids']
        self.track_name = dict['track_name']
        self.sessionfastlap = dict['sessionfastlap']
        self.winner_helmet_color2 = dict['winner_helmet_color2']
        self.winner_helmet_color1 = dict['winner_helmet_color1']
        self.winner_helmet_color3 = dict['winner_helmet_color3']
        self.maxliclevel = dict['maxliclevel']
        self.weather_rh = dict['weather_rh']
        self.racelength = dict['racelength']
        self.multiclass = dict['multiclass']
        self.lonequalify = dict['lonequalify']
        self.host_helmet_facetype = dict['host_helmet_facetype']
        self.weather_wind_speed_value = dict['weather_wind_speed_value']
        self.minliclevel = dict['minliclevel']
        self.winner_helmet_pattern = dict['winner_helmet_pattern']
        self.host_helmet_pattern = dict['host_helmet_pattern']
        self.weather_wind_speed_units = dict['weather_wind_speed_units']
        self.host_helmet_helmettype = dict['host_helmet_helmettype']
        self.classstartingposition = dict['classstartingposition']
        self.winner_displaynames = dict['winner_displaynames']


class SeriesRaceResults:
    def __init__(self, dict):
        self.start_time = dict['1']
        self.carclassid = dict['2']
        self.trackid = dict['3']
        self.sessionid = dict['4']
        self.subsessionid = dict['5']
        self.officialsession = dict['6']
        self.sizeoffield = dict['7']
        self.strengthoffield = dict['8']


class Team:
    def __init__(self, dict):
        self.weekstarts = dict['weekstarts']
        self.pattern = dict['pattern']
        self.color3 = dict['color3']
        self.lapscomplete = dict['lapscomplete']
        self.eventtop10pcnt = dict['eventtop10pcnt']
        self.color1 = dict['color1']
        self.color2 = dict['color2']
        self.teamid = dict['teamid']
        self.incidents = dict['incidents']
        self.team_ranking = dict['team_ranking']
        self.classpoles = dict['classpoles']
        self.eventwins = dict['eventwins']
        self.classtop10pcnt = dict['classtop10pcnt']
        self.weekdropped = dict['weekdropped']
        self.avgeventstrengthoffield = dict['avgeventstrengthoffield']
        self.helmettype = dict['helmettype']
        self.eventtopfive = dict['eventtopfive']
        self.licenselevel = dict['licenselevel']
        self.avgclasssizeoffield = dict['avgclasssizeoffield']
        self.avgeventstartingposition = dict['avgeventstartingposition']
        self.eventtop25pcnt = dict['eventtop25pcnt']
        self.avgclassstartingposition = dict['avgclassstartingposition']
        self.avgclassfinishingposition = dict['avgclassfinishingposition']
        self.classtopfive = dict['classtopfive']
        self.cars = dict['cars']
        self.classwins = dict['classwins']
        self.lapslead = dict['lapslead']
        self.weekpoints = dict['weekpoints']
        self.avgclassstrengthoffield = dict['avgclassstrengthoffield']
        self.avgeventfinishingposition = dict['avgeventfinishingposition']
        self.custid = dict['custid']
        self.name = dict['name']
        self.eventpoles = dict['eventpoles']
        self.avgeventsizeoffield = dict['avgeventsizeoffield']
        self.classtop25pcnt = dict['classtop25pcnt']
        self.facetype = dict['facetype']