from pyracing.helpers import parse_encode


class EventResults:
    def __init__(self, data):
        self.car_class_id = data['29']
        self.car_id = data['32']
        self.category_id = data['33']
        self.cust_id = data['23']
        self.date_start = parse_encode(data['44'])
        self.display_name = parse_encode(data['48'])
        self.event_type = data['37']
        self.group_name = parse_encode(data['19'])
        self.helm_color_1 = data['1']
        self.helm_color_2 = data['14']
        self.helm_color_3 = data['13']
        self.helm_license_level = data['24']
        self.helm_pattern = data['46']
        self.incidents = data['39']
        self.lap_best = parse_encode(data['38'])
        self.lap_best_subsession = parse_encode(data['7'])
        self.lap_qual_best = parse_encode(data['6'])
        self.license_group = data['35']
        self.official_session = data['18']
        self.points_champ = data['40']
        self.points_champ_sort = data['43']
        self.points_club = data['16']
        self.points_club_sort = data['47']
        self.points_drop_race = data['17']
        self.pos_finish = data['3']
        self.pos_start = data['12']
        self.race_week = data['8']
        self.rank_session = data['28']
        self.row_number = data['26']
        self.season_id = data['22']
        self.season_quarter = data['34']
        self.season_year = data['42']
        self.series_id = data['20']
        self.session_id = data['9']
        self.strength_of_field = data['45']
        self.subsession_id = data['41']
        self.time_finished = data['10']
        self.time_start = parse_encode(data['21'])
        self.time_start_raw = data['11']
        self.track_id = data['30']
        self.winner_display_name = parse_encode(data['31'])
        self.winner_helm_color_1 = data['5']
        self.winner_helm_color_2 = data['2']
        self.winner_helm_color_3 = data['4']
        self.winner_helm_pattern = data['36']
        self.winner_license_level = data['25']
        self.winners_group_id = data['27']
        # Another instance of not in dict
        # self.rowcount = dict['15']


class SeasonStandings:
    def __init__(self, data):
        self.club_id = data['6']
        self.club_name = parse_encode(data['23'])
        self.country = parse_encode(data['1'])
        self.country_code = data['4']
        self.country_name = parse_encode(data['32'])
        self.cust_id = data['28']
        self.display_name = parse_encode(data['26'])
        self.division = data['11']
        self.dropped = data['5']
        self.helm_color_1 = data['25']
        self.helm_color_2 = data['27']
        self.helm_color_3 = data['22']
        self.helm_pattern = data['20']
        self.incidents = data['13']
        self.irating = data['3']
        self.laps = data['7']
        self.laps_led = data['24']
        self.license_level_max = data['21']
        self.points = data['10']
        self.poles = data['19']
        self.pos = data['30']
        self.pos_finish_avg = data['9']
        self.pos_start_avg = data['8']
        self.rank = data['14']
        self.row = data['31']
        self.starts = data['15']
        self.sub_level = parse_encode(data['29'])
        self.top_fives = data['12']
        self.week = data['2']
        self.wins = data['17']

        # Used only on webpage to highlight the member in relaton to others
        # self.custrow = dict['16']
        # self.rowcount = dict['18']


class DriverStats:
    def __init__(self, data):
        self.club_id = data['5']
        self.club_name = parse_encode(data['29'])
        self.club_points = data['21']
        self.country_code = data['4']
        self.cust_id = data['34']
        self.display_name = parse_encode(data['32'])
        self.field_size_avg = data['13']
        self.group_letter = data['39']
        self.group_name = parse_encode(data['24'])
        self.helm_color_1 = data['31']
        self.helm_color_2 = data['33']
        self.helm_color_3 = data['28']
        self.helm_face_type = data['36']
        self.helm_helmet_type = data['10']
        self.helm_pattern = data['22']
        self.incidents_avg = data['26']
        self.irating = data['3']
        self.irating_rank = data['2']
        self.laps = data['7']
        self.laps_led = data['30']
        self.license_class = parse_encode(data['16'])
        self.license_class_id = data['12']
        self.license_class_rank = data['19']
        self.license_level = data['23']
        self.points = data['11']
        self.points_avg = data['27']
        self.pos_finish_avg = data['9']
        self.pos_start_avg = data['8']
        self.rank = data['14']
        self.region = parse_encode(data['38'])
        self.row = data['37']
        self.starts = data['15']
        self.sub_level = data['35']
        self.top_25_percent = data['1']
        self.ttrating = data['25']
        self.ttrating_rank = data['6']
        self.wins = data['18']
        # These are only used in front end webpage; Not in dict results
        # self.custrow = dict['17']
        # self.rowcount = dict['20']


class WorldRecords:
    def __init__(self, data):
        self.car_id = data['10']
        self.cat_id = data['11']
        self.category = parse_encode(data['37'])
        self.club_id = data['7']
        self.club_name = parse_encode(data['28'])
        self.country_code = data['6']
        self.cust_id = data['32']
        self.display_name = parse_encode(data['30'])
        self.helm_color_1 = data['29']
        self.helm_color_2 = data['31']
        self.helm_color_3 = data['27']
        self.helm_face_type = data['34']
        self.helm_helmet_type = data['9']
        self.helm_pattern = data['23']
        self.irating = data['4']
        self.license_class = parse_encode(data['3'])
        self.license_class_id = data['15']
        self.license_level = data['24']
        self.practice = parse_encode(data['2'])
        self.practice_start_time = data['8']
        self.practice_subsession_id = data['14']
        self.qualify = parse_encode(data['16'])
        self.qualify_subsession_id = data['38']
        self.qualify_time_start = data['22']
        self.race = parse_encode(data['20'])
        self.race_start_time = data['19']
        self.race_subsession_id = data['12']
        self.region = parse_encode(data['36'])
        self.row = data['35']
        self.season_quarter = data['13']
        self.season_year = data['18']
        self.sub_level = data['33']
        self.timetrial = parse_encode(data['39'])
        self.track_id = data['5']
        self.tt_start_time = data['26']
        self.tt_subsession_id = data['1']
        self.ttrating = data['25']
        # Data not used in the 'r' dictionary. Only for webpage display.
        # self.custrow = dict['17']
        # self.rowcount = dict['21']


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
        self.car_class_id = data['2']
        self.official = data['6']
        self.session_id = data['4']
        self.size_of_field = data['7']
        self.strength_of_field = data['8']
        self.subsession_id = data['5']
        self.time_start = data['1']
        self.track_id = data['3']


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
