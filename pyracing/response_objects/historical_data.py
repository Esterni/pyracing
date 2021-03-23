from pyracing.helpers import parse_encode


class EventResults:
    def __init__(self, data):
        self.car_class_id = data['carclassid']
        self.car_id = data['carid']
        self.category_id = data['catid']
        self.cust_id = data['custid']
        self.date_start = parse_encode(data['start_date'])
        self.display_name = parse_encode(data['displayname'])
        self.event_type = data['evttype']
        self.group_name = parse_encode(data['groupname'])
        self.helm_color_1 = data['helm_color1']
        self.helm_color_2 = data['helm_color2']
        self.helm_color_3 = data['helm_color3']
        self.helm_license_level = data['helm_licenselevel']
        self.helm_pattern = data['helm_pattern']
        self.incidents = data['incidents']
        self.lap_best = parse_encode(data['bestlaptime'])
        self.lap_best_subsession = parse_encode(data['subsession_bestlaptime'])
        self.lap_qual_best = parse_encode(data['bestquallaptime'])
        self.license_group = data['licensegroup']
        self.official_session = data['officialsession']
        self.points_champ = data['champpoints']
        self.points_champ_sort = data['champpointssort']
        self.points_club = data['clubpoints']
        self.points_club_sort = data['clubpointssort']
        self.points_drop_race = data['dropracepoints']
        self.pos_finish = data['finishing_position']
        self.pos_start = data['starting_position']
        self.race_week = data['race_week_num']
        self.rank_session = data['sesrank']
        self.row_number = data['rn']
        self.season_id = data['seasonid']
        self.season_quarter = data['season_quarter']
        self.season_year = data['season_year']
        self.series_id = data['seriesid']
        self.session_id = data['sessionid']
        self.strength_of_field = data['strengthoffield']
        self.subsession_id = data['subsessionid']
        self.time_finished = data['finishedat']
        self.time_start = parse_encode(data['start_time'])
        self.time_start_raw = data['raw_start_time']
        self.track_id = data['trackid']
        self.winner_display_name = parse_encode(data['winnerdisplayname'])
        self.winner_helm_color_1 = data['winnerhelmcolor1']
        self.winner_helm_color_2 = data['winnerhelmcolor2']
        self.winner_helm_color_3 = data['winnerhelmcolor3']
        self.winner_helm_pattern = data['winnerhelmpattern']
        self.winner_license_level = data['winnerlicenselevel']
        self.winners_group_id = data['winnersgroupid']
        # Another instance of not in dict
        # self.rowcount = dict['rowcount']


class SeasonStandings:
    def __init__(self, data):
        self.club_id = data['clubid']
        self.club_name = parse_encode(data['clubname'])
        self.country = parse_encode(data['country'])
        self.country_code = data['countrycode']
        self.country_name = parse_encode(data['displaycountry'])
        self.cust_id = data['custid']
        self.display_name = parse_encode(data['displayname'])
        self.division = data['division']
        self.dropped = data['dropped']
        self.helm_color_1 = data['helmcolor1']
        self.helm_color_2 = data['helmcolor2']
        self.helm_color_3 = data['helmcolor3']
        self.helm_pattern = data['helmpattern']
        self.incidents = data['incidents']
        self.irating = data['irating']
        self.laps = data['laps']
        self.laps_led = data['lapslead']
        self.license_level_max = data['maxlicenselevel']
        self.points = data['points']
        self.poles = data['poles']
        self.pos = data['pos']
        self.pos_finish_avg = data['avgfinish']
        self.pos_start_avg = data['avgstart']
        self.rank = data['rank']
        self.row = data['rn']
        self.starts = data['starts']
        self.sub_level = parse_encode(data['sublevel'])
        self.top_fives = data['topfive']
        self.week = data['week']
        self.wins = data['wins']

        # Used only on webpage to highlight the member in relaton to others
        # self.custrow = dict['custrow']
        # self.rowcount = dict['rowcount']


class DriverStats:
    def __init__(self, data):
        self.club_id = data['clubid']
        self.club_name = parse_encode(data['clubname'])
        self.club_points = data['clubpoints']
        self.country_code = data['countrycode']
        self.cust_id = data['custid']
        self.display_name = parse_encode(data['displayname'])
        self.field_size_avg = data['avefieldsize']
        self.group_letter = data['groupletter']
        self.group_name = parse_encode(data['groupname'])
        self.helm_color_1 = data['helmcolor1']
        self.helm_color_2 = data['helmcolor2']
        self.helm_color_3 = data['helmcolor3']
        self.helm_face_type = data['helmfacetype']
        self.helm_helmet_type = data['helmhelmettype']
        self.helm_pattern = data['helmpattern']
        self.incidents_avg = data['avgincidents']
        self.irating = data['irating']
        self.irating_rank = data['irating_rank']
        self.laps = data['laps']
        self.laps_led = data['lapslead']
        self.license_class = parse_encode(data['licenseclass'])
        self.license_class_id = data['licensegroup']
        self.license_class_rank = data['licenseclass_rank']
        self.license_level = data['licenselevel']
        self.points = data['points']
        self.points_avg = data['avgpoints']
        self.pos_finish_avg = data['avefinishingposition']
        self.pos_start_avg = data['avestartingposition']
        self.rank = data['rank']
        self.region = parse_encode(data['region'])
        self.row = data['rn']
        self.starts = data['starts']
        self.sub_level = data['sublevel']
        self.top_25_percent = data['top25pcnt']
        self.ttrating = data['ttrating']
        self.ttrating_rank = data['ttrating_rank']
        self.wins = data['wins']
        # These are only used in front end webpage; Not in dict results
        # self.custrow = dict['custrow']
        # self.rowcount = dict['rowcount']


class WorldRecords:
    def __init__(self, data):
        self.car_id = data['carid']
        self.cat_id = data['catid']
        self.category = parse_encode(data['category'])
        self.club_id = data['clubid']
        self.club_name = parse_encode(data['clubname'])
        self.country_code = data['countrycode']
        self.cust_id = data['custid']
        self.display_name = parse_encode(data['displayname'])
        self.helm_color_1 = data['helmcolor1']
        self.helm_color_2 = data['helmcolor2']
        self.helm_color_3 = data['helmcolor3']
        self.helm_face_type = data['helmfacetype']
        self.helm_helmet_type = data['helmhelmettype']
        self.helm_pattern = data['helmpattern']
        self.irating = data['irating']
        self.license_class = parse_encode(data['licenseclass'])
        self.license_class_id = data['licensegroup']
        self.license_level = data['licenselevel']
        self.practice = parse_encode(data['practice'])
        self.practice_start_time = data['practice_start_time']
        self.practice_subsession_id = data['practice_subsessionid']
        self.qualify = parse_encode(data['qualify'])
        self.qualify_subsession_id = data['qualify_subsessionid']
        self.qualify_time_start = data['qualify_start_time']
        self.race = parse_encode(data['race'])
        self.race_start_time = data['race_start_time']
        self.race_subsession_id = data['race_subsessionid']
        self.region = parse_encode(data['region'])
        self.row = data['rn']
        self.season_quarter = data['season_quarter']
        self.season_year = data['season_year']
        self.sub_level = data['sublevel']
        self.timetrial = parse_encode(data['timetrial'])
        self.track_id = data['trackid']
        self.tt_start_time = data['timetrial_start_time']
        self.tt_subsession_id = data['timetrial_subsessionid']
        self.ttrating = data['ttrating']
        # Data not used in the 'r' dictionary. Only for webpage display.
        # self.custrow = dict['custrow']
        # self.rowcount = dict['rowcount']


class PrivateResults:
    def __init__(self, data):
        self.car_class_id = data['carclassid']
        self.car_ids = parse_encode(data['carids'])
        self.cat_id = data['catid']
        self.created = data['created']
        self.drivers_max = data['maxdrivers']
        self.fast_tows_num = data['numfasttows']
        self.fixed_setup = data['fixed_setup']
        self.fog_density = data['weather_fog_density']
        self.full_course_cautions = data['fullcoursecautions']
        self.hardcore_level = data['hardcorelevel']
        self.host_cust_id = data['host_custid']
        self.host_display_name = parse_encode(data['host_displayname'])
        self.host_helmet_color_1 = data['host_helmet_color1']
        self.host_helmet_color_2 = data['host_helmet_color2']
        self.host_helmet_color_3 = data['host_helmet_color3']
        self.host_helmet_face_type = data['host_helmet_facetype']
        self.host_helmet_helmet_type = data['host_helmet_helmettype']
        self.host_helmet_pattern = data['host_helmet_pattern']
        self.host_license_level = data['host_licenselevel']
        self.humidity = data['weather_rh']
        self.incidents = data['incidents']
        self.ir_max = data['maxir']
        self.ir_min = data['minir']
        self.lap_best = data['bestlaptime']
        self.lic_level_max = data['maxliclevel']
        self.lic_level_min = data['minliclevel']
        self.lonequalify = data['lonequalify']
        self.multiclass = data['multiclass']
        self.pct_fuel_fills_max = parse_encode(data['max_pct_fuel_fills'])
        self.pos_finish = data['finishingposition']
        self.pos_finish_class = data['classfinishingposition']
        self.pos_start = data['startingposition']
        self.pos_start_class = data['classstartingposition']
        self.practice_length = data['practicelength']
        self.private = data['private']
        self.qual_laps = data['qualifylaps']
        self.qual_length = data['qualifylength']
        self.qual_setup_filenames = data['qualsetupfilenames']
        self.qual_setup_ids = data['qualsetupids']
        self.race_laps = data['racelaps']
        self.race_length = data['racelength']
        self.race_setup_filenames = data['racesetupfilenames']
        self.race_setup_ids = data['racesetupids']
        self.race_time_finished = data['racefinishedat']
        self.restarts = data['restarts']
        self.rolling_starts = data['rollingstarts']
        self.row = data['rn']
        self.session_fast_lap = data['sessionfastlap']
        self.session_id = data['sessionid']
        self.session_id_private = data['privatesessionid']
        self.session_name = parse_encode(data['sessionname'])
        self.skies = data['weather_skies']
        self.subsession_id = data['subsessionid']
        self.subsession_time_finished = data['subsessionfinishedat']
        self.temp_unit = data['weather_temp_units']
        self.temp_value = data['weather_temp_value']
        self.time_of_day = data['timeofday']
        self.time_start = data['start_time']
        self.track = parse_encode(data['track_name'])
        self.track_id = data['trackid']
        self.weather_type = data['weather_type']
        self.weight_penalties = data['weight_penalties']
        self.wind_direction = data['weather_wind_dir']
        self.wind_speed_unit = data['weather_wind_speed_units']
        self.wind_speed_value = data['weather_wind_speed_value']
        self.winner_display_name = parse_encode(data['winner_displayname'])
        self.winner_display_names = parse_encode(data['winner_displaynames'])
        self.winner_group_id = data['winnersgroupid']
        self.winner_helmet_color_1 = data['winner_helmet_color1']
        self.winner_helmet_color_2 = data['winner_helmet_color2']
        self.winner_helmet_color_3 = data['winner_helmet_color3']
        self.winner_helmet_pattern = data['winner_helmet_pattern']
        self.winner_license_level = data['winner_licenselevel']


class SeriesRaceResults:
    def __init__(self, data):
        self.car_class_id = data['carclassid']
        self.official = data['officialsession']
        self.session_id = data['sessionid']
        self.size_of_field = data['sizeoffield']
        self.strength_of_field = data['strengthoffield']
        self.subsession_id = data['subsessionid']
        self.time_start = data['start_time']
        self.track_id = data['trackid']


class Team:
    def __init__(self, data):
        self.cars = parse_encode(data['cars'])
        self.class_finish_pos_avg = data['avgclassfinishingposition']
        self.class_poles = data['classpoles']
        self.class_size_of_field_avg = data['avgclasssizeoffield']
        self.class_start_pos_avg = data['avgclassstartingposition']
        self.class_strength_of_field_avg = data['avgclassstrengthoffield']
        self.class_top_10_pcnt = data['classtop10pcnt']
        self.class_top_25_percent = data['classtop25pcnt']
        self.class_top_five = data['classtopfive']
        self.class_wins = data['classwins']
        self.color_1 = data['color1']
        self.color_2 = data['color2']
        self.color_3 = data['color3']
        self.cust_id = data['custid']
        self.event_finish_pos_avg = data['avgeventfinishingposition']
        self.event_poles = data['eventpoles']
        self.event_pos_start_avg = data['avgeventstartingposition']
        self.event_size_of_field_avg = data['avgeventsizeoffield']
        self.event_strength_of_field_avg = data['avgeventstrengthoffield']
        self.event_top_10_pcnt = data['eventtop10pcnt']
        self.event_top_25_pcnt = data['eventtop25pcnt']
        self.event_top_fives = data['eventtopfive']
        self.event_wins = data['eventwins']
        self.face_type = data['facetype']
        self.helmet_type = data['helmettype']
        self.incidents = data['incidents']
        self.laps_comp = data['lapscomplete']
        self.laps_led = data['lapslead']
        self.license_level = data['licenselevel']
        self.name = parse_encode(data['name'])
        self.pattern = data['pattern']
        self.team_id = data['teamid']
        self.team_ranking = data['team_ranking']
        self.week_dropped = data['weekdropped']
        self.week_points = data['weekpoints']
        self.week_starts = data['weekstarts']
