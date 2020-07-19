from ..constants import parse_encode


class EventResults:
    def __init__(self, dict):
        self.best_qlap = parse_encode(dict['38'])
        self.subsession_best_lap = parse_encode(dict['6'])
        self.best_lap = dict['29']
        self.car_class_id = dict['32']
        self.car_id = dict['33']
        self.cat_id = dict['40']
        self.champ_points_sort = dict['43']
        self.champ_points = dict['16']
        self.club_points_sort = dict['47']
        self.club_points = dict['23']
        self.cust_id = parse_encode(dict['48'])
        self.display_name = dict['17']
        self.drop_race = dict['37']
        self.event_type = dict['10']
        self.finish_pos = dict['3']
        self.group_name = dict['19']
        self.helm_color1 = dict['1']
        self.helm_color2 = parse_encode(dict['14'])
        self.helm_color3 = parse_encode(dict['13'])
        self.helm_license_level = dict['24']
        self.helm_pattern = dict['46']
        self.incidents = dict['39']
        self.license_class = dict['35']
        self.official = dict['18']
        self.race_week = dict['8']
        self.raw_start_time = dict['11']
        self.row = dict['26']
        self.season_id = dict['34']
        self.season_quarter = dict['42']
        self.series_id = dict['22']
        self.session_id = dict['20']
        self.session_rank = dict['28']
        self.start_date = dict['9']
        self.start_pos = parse_encode(dict['44'])
        self.start_time = parse_encode(dict['21'])
        self.strength_of_field = dict['12']
        self.subsession_id = dict['45']
        self.time_finished = parse_encode(dict['7'])
        self.track_id = dict['41']
        self.winner_display_name = dict['30']
        self.winner_helm_color1 = parse_encode(dict['31'])
        self.winner_helm_color2 = parse_encode(dict['5'])
        self.winner_helm_color3 = dict['2']
        self.winner_helm_pattern = parse_encode(dict['4'])
        self.winner_license_level = dict['36']
        self.winner_group_id = dict['25']
        self.season_year = dict['27']
        # Another instance of not in dict
        # self.rowcount = dict['15']


class SeasonStandings:
    def __init__(self, dict):
        self.avg_finish_pos = dict['9']
        self.avg_start_pos = dict['8']
        self.club_id = dict['6']
        self.club_name = parse_encode(dict['23'])
        self.country = parse_encode(dict['1'])
        self.country_code = parse_encode(dict['4'])
        self.cust_id = dict['28']
        self.country_name = dict['32']
        self.display_name = parse_encode(dict['26'])
        self.division = dict['11']
        self.dropped = dict['5']
        self.helm_color1 = parse_encode(dict['25'])
        self.helm_color2 = parse_encode(dict['27'])
        self.helm_color3 = parse_encode(dict['22'])
        self.helm_pattern = dict['20']
        self.incidents = dict['13']
        self.irating = dict['3']
        self.laps = dict['7']
        self.laps_led = dict['24']
        self.max_license_level = dict['21']
        self.points = dict['10']
        self.poles_total = dict['19']
        self.pos = dict['30']
        self.rank = dict['14']
        self.row = dict['31']
        self.starts_total = dict['15']
        self.sub_level = parse_encode(dict['29'])
        self.top_five = dict['12']
        self.week = dict['2']
        self.win_total = dict['17']

        # Used only on webpage to highlight the member in relaton to others
        # self.custrow = dict['16']
        # self.rowcount = dict['18']


class DriverStats:
    def __init__(self, dict):
        self.avg_field_size = dict['13']
        self.avg_finish_pos = dict['9']
        self.avg_start_pos = dict['8']
        self.avg_incidents = dict['26']
        self.avg_points = dict['27']
        self.club_id = dict['5']
        self.club_name = parse_encode(dict['29'])
        self.club_points = dict['21']
        self.country_code = parse_encode(dict['4'])
        self.cust_id = dict['34']
        self.display_name = parse_encode(dict['32'])
        self.group_letter = parse_encode(dict['39'])
        self.group_name = parse_encode(dict['24'])
        self.helm_color1 = parse_encode(dict['31'])
        self.helm_color2 = parse_encode(dict['33'])
        self.helm_color3 = parse_encode(dict['28'])
        self.helm_face_type = dict['36']
        self.helm_helmet_type = dict['10']
        self.helm_pattern = dict['22']
        self.irating = dict['3']
        self.irating_rank = dict['2']
        self.laps = dict['7']
        self.laps_led = dict['30']
        self.license_class = parse_encode(dict['16'])
        self.license_class_rank = dict['19']
        self.license_class = dict['12']
        self.license_level = dict['23']
        self.points = dict['11']
        self.rank = dict['14']
        self.region = parse_encode(dict['38'])
        self.row = dict['37']
        self.starts_total = dict['15']
        self.sub_level = dict['35']
        self.top_25_percent = dict['1']
        self.ttrating = dict['25']
        self.ttrating_rank = dict['6']
        self.win_total = dict['18']
        # These are only used in front end webpage; Not in dict results
        # self.custrow = dict['17']
        # self.rowcount = dict['20']


class WorldRecords:
    def __init__(self, dict):
        self.car_id = dict['9']
        self.category = parse_encode(dict['35'])
        self.cat_id = dict['10']
        self.club_id = dict['7']
        self.club_name = parse_encode(dict['27'])
        self.country_code = parse_encode(dict['6'])
        self.cust_id = dict['31']
        self.display_name = parse_encode(dict['29'])
        self.helm_color1 = parse_encode(dict['28'])
        self.helm_color2 = parse_encode(dict['30'])
        self.helm_color3 = parse_encode(dict['26'])
        self.helm_pattern = dict['22']
        self.irating = dict['4']
        self.license_class = parse_encode(dict['3'])
        self.license_class = dict['14']
        self.license_level = dict['23']
        self.practice = parse_encode(dict['2'])
        self.practice_start_time = dict['8']
        self.practice_subsession_id = dict['13']
        self.qualify = parse_encode(dict['15'])
        self.qualify_start_time = dict['21']
        self.qualify_subsession_id = ['36']
        self.race = parse_encode(dict['19'])
        self.race_start_time = dict['18']
        self.race_subsession_id = ['11']
        self.region = parse_encode(dict['34'])
        self.row = dict['33']
        self.season_quarter = parse_encode(dict['12'])
        self.season_year = parse_encode(dict['17'])
        self.sub_level = dict['32']
        self.timetrial = parse_encode(dict['37'])
        self.timetrial_start_time = dict['25']
        self.timetrial_subsession_id = ['1']
        self.track_id = dict['5']
        self.ttrating = dict['24']
        # Data not used in the 'r' dictionary. Only for webpage display.
        # self.custrow = dict['16']
        # self.rowcount = dict['20']


class PrivateResults:
    def __init__(self, dict):
        self.best_lap = dict['bestlaptime']
        self.car_class_id = dict['carclassid']
        self.car_ids = dict['carids']
        self.cat_id = dict['catid']
        self.class_finish_pos = dict['classfinishingposition']
        self.class_start_pos = dict['classstartingposition']
        self.created = dict['created']
        self.finish_pos = dict['finishingposition']
        self.fixed_setup = dict['fixed_setup']
        self.full_course_cautions = dict['fullcoursecautions']
        self.hardcore_level = dict['hardcorelevel']
        self.host_cust_id = dict['host_custid']
        self.host_display_name = dict['host_displayname']
        self.host_helmet_color1 = dict['host_helmet_color1']
        self.host_helmet_color2 = dict['host_helmet_color2']
        self.host_helmet_color3 = dict['host_helmet_color3']
        self.host_helmet_face_type = dict['host_helmet_facetype']
        self.host_helmet_helmet_type = dict['host_helmet_helmettype']
        self.host_helmet_pattern = dict['host_helmet_pattern']
        self.host_license_level = dict['host_licenselevel']
        self.incidents = dict['incidents']
        self.lonequalify = dict['lonequalify']
        self.max_pct_fuel_fills = dict['max_pct_fuel_fills']
        self.max_drivers = dict['maxdrivers']
        self.max_ir = dict['maxir']
        self.max_lic_level = dict['maxliclevel']
        self.min_ir = dict['minir']
        self.min_lic_level = dict['minliclevel']
        self.multiclass = dict['multiclass']
        self.num_fast_tows = dict['numfasttows']
        self.practice_length = dict['practicelength']
        self.private = dict['private']
        self.private_session_id = dict['privatesessionid']
        self.qualify_laps = dict['qualifylaps']
        self.qualify_length = dict['qualifylength']
        self.qual_setup_filenames = dict['qualsetupfilenames']
        self.qual_setup_ids = dict['qualsetupids']
        self.race_finished_at = dict['racefinishedat']
        self.race_laps = dict['racelaps']
        self.race_length = dict['racelength']
        self.race_setup_filenames = dict['racesetupfilenames']
        self.race_setup_ids = dict['racesetupids']
        self.restarts = dict['restarts']
        self.row = dict['rn']
        self.rolling_starts = dict['rollingstarts']
        self.session_fast_lap = dict['sessionfastlap']
        self.session_id = dict['sessionid']
        self.session_name = dict['sessionname']
        self.start_time = dict['start_time']
        self.start_pos = dict['startingposition']
        self.subsession_finished_at = dict['subsessionfinishedat']
        self.subsession_id = dict['subsessionid']
        self.time_of_day = dict['timeofday']
        self.track = dict['track_name']
        self.track_id = dict['trackid']
        self.weather_fog_density = dict['weather_fog_density']
        self.humidity = dict['weather_rh']
        self.skies = dict['weather_skies']
        self.temp_unit = dict['weather_temp_units']
        self.temp_value = dict['weather_temp_value']
        self.weather = dict['weather_type']
        self.wind_direction = dict['weather_wind_dir']
        self.wind_speed_unit = dict['weather_wind_speed_units']
        self.wind_speed_value = dict['weather_wind_speed_value']
        self.weight_penalties = dict['weight_penalties']
        self.winner_display_name = dict['winner_displayname']
        self.winner_display_names = dict['winner_displaynames']
        self.winner_helmet_color1 = dict['winner_helmet_color1']
        self.winner_helmet_color2 = dict['winner_helmet_color2']
        self.winner_helmet_color3 = dict['winner_helmet_color3']
        self.winner_helmet_pattern = dict['winner_helmet_pattern']
        self.winner_license_level = dict['winner_licenselevel']
        self.winners_group_id = dict['winnersgroupid']


class SeriesRaceResults:
    def __init__(self, dict):
        self.car_class_id = dict['2']
        self.official = dict['6']
        self.session_id = dict['4']
        self.size_of_field = dict['7']
        self.start_time = dict['1']
        self.strength_of_field = dict['8']
        self.subsession_id = dict['5']
        self.track_id = dict['3']


class Team:
    def __init__(self, dict):
        self.avg_class_finish_pos = dict['avgclassfinishingposition']
        self.avg_classsize_of_field = dict['avgclasssizeoffield']
        self.avg_class_start_pos = dict['avgclassstartingposition']
        self.avg_class_strength_of_field = dict['avgclassstrengthoffield']
        self.avg_event_finish_pos = dict['avgeventfinishingposition']
        self.avg_event_size_of_field = dict['avgeventsizeoffield']
        self.avg_event_start_pos = dict['avgeventstartingposition']
        self.avg_event_strength_of_field = dict['avgeventstrengthoffield']
        self.cars = dict['cars']
        self.class_poles_total = dict['classpoles']
        self.class_top_10_pcnt = dict['classtop10pcnt']
        self.class_top_25_percent = dict['classtop25pcnt']
        self.class_top_five = dict['classtopfive']
        self.class_win_total = dict['classwins']
        self.color1 = dict['color1']
        self.color2 = dict['color2']
        self.color3 = dict['color3']
        self.cust_id = dict['custid']
        self.event_poles_total = dict['eventpoles']
        self.event_top_10_pcnt = dict['eventtop10pcnt']
        self.event_top_25_percent = dict['eventtop25pcnt']
        self.event_top_five = dict['eventtopfive']
        self.event_win_total = dict['eventwins']
        self.face_type = dict['facetype']
        self.helmet_type = dict['helmettype']
        self.incidents = dict['incidents']
        self.laps_comp = dict['lapscomplete']
        self.laps_led = dict['lapslead']
        self.license_level = dict['licenselevel']
        self.name = dict['name']
        self.pattern = dict['pattern']
        self.team_ranking = dict['team_ranking']
        self.team_id = dict['teamid']
        self.week_dropped = dict['weekdropped']
        self.week_points = dict['weekpoints']
        self.week_starts = dict['weekstarts']
