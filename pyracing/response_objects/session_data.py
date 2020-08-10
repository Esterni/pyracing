from pyracing.helpers import parse_encode


class SubSessionData:
    def __init__(self, data):
        self.cat_id = data['catid']
        self.caution_laps = data['ncautionlaps']
        self.caution_type = data['cautiontype']
        self.cautions = data['ncautions']
        self.corners_total = data['cornersperlap']
        self.driver_change_param_1 = data['driver_change_param1']
        self.driver_change_param_2 = data['driver_change_param2']
        self.driver_change_rule = data['driver_change_rule']
        self.driver_changes = data['driver_changes']
        self.event_type = data['evttype']
        self.fog_density = data['weather_fog_density']
        self.humidity = data['weather_rh']
        self.lap_avg = data['eventavglap']
        self.laps_completed = data['eventlapscomplete']
        self.laps_for_qual_avg = data['nlapsforqualavg']
        self.laps_for_solo_avg = data['nlapsforsoloavg']
        self.lead_changes = data['nleadchanges']
        self.league_id = data['leagueid']
        self.league_season_id = data['league_season_id']
        self.leave_marbles = data['leavemarbles']
        self.max_weeks = data['maxweeks']
        self.points_type = data['pointstype']
        self.private_session_id = data['privatesessionid']
        self.race_week = data['race_week_num']
        self.reserve_status = data['rserv_status']
        self.rubber_practice = data['rubberlevel_practice']
        self.rubber_qualify = data['rubberlevel_qualify']
        self.rubber_race = data['rubberlevel_race']
        self.rubber_warmup = data['rubberlevel_warmup']
        self.season_id = data['seasonid']
        self.season_name = parse_encode(data['season_name'])
        self.season_name_short = parse_encode(data['season_shortname'])
        self.season_quarter = data['season_quarter']
        self.season_year = data['season_year']
        self.series_id = data['seriesid']
        self.series_name = parse_encode(data['series_name'])
        self.series_name_short = parse_encode(data['series_shortname'])
        self.session_id = data['sessionid']
        self.session_name = parse_encode(data['sessionname'])
        self.sim_ses_type = data['simsestype']
        self.skies = data['weather_skies']
        self.special_event_type = data['specialeventtype']
        self.special_event_type_text = data['specialeventtypetext']
        self.strength_of_field = data['eventstrengthoffield']
        self.subsession_id = data['subsessionid']
        self.team_drivers_max = data['max_team_drivers']
        self.team_drivers_min = data['min_team_drivers']
        self.temp_unit = data['weather_temp_units']
        self.temp_value = data['weather_temp_value']
        self.time_of_day = data['timeofday']
        self.time_start = parse_encode(data['start_time'])
        self.time_start_sim = parse_encode(data['simulatedstarttime'])
        self.track = parse_encode(data['track_name'])
        self.track_config = parse_encode(data['track_config_name'])
        self.track_id = data['trackid']
        self.weather_initial = data['weather_var_initial']
        self.weather_ongoing = data['weather_var_ongoing']
        self.weather_type = data['weather_type']
        self.wind_direction = data['weather_wind_dir']
        self.wind_speed_unit = data['weather_wind_speed_units']
        self.wind_speed_value = data['weather_wind_speed_value']

        self.drivers = [self.Driver(x) for x in data['rows']]

    class Driver:
        def __init__(self, data):
            self.car_class_id = data['carclassid']
            self.car_class_name = parse_encode(data['ccName'])
            self.car_class_name_short = parse_encode(data['ccNameShort'])
            self.car_color_1 = data['car_color1']
            self.car_color_2 = data['car_color2']
            self.car_color_3 = data['car_color3']
            self.car_id = data['carid']
            self.car_num = data['carnum']
            self.car_num_font = data['carnumberfont']
            self.car_num_slant = data['carnumberslant']
            self.car_number_color_1 = data['car_number_color1']
            self.car_number_color_2 = data['car_number_color2']
            self.car_number_color_3 = data['car_number_color3']
            self.car_pattern = data['car_pattern']
            self.car_sponser_1 = data['carsponsor1']
            self.car_sponser_2 = data['carsponsor2']
            self.club_id = data['clubid']
            self.club_name = parse_encode(data['clubname'])
            self.club_name_short = parse_encode(data['clubshortname'])
            self.club_points = data['clubpoints']
            self.cpi_new = data['newcpi']
            self.cpi_old = data['oldcpi']
            self.cust_id = data['custid']
            self.damage_model = data['damage_model']
            self.display_name = parse_encode(data['displayname'])
            self.division = data['division']
            self.division_name = parse_encode(data['divisionname'])
            self.drop_race = data['dropracepoints']
            self.event_type_name = parse_encode(data['evttypename'])
            self.group_id = data['groupid']
            self.heat_info_id = data['heatinfoid']
            self.helm_color_1 = data['helm_color1']
            self.helm_color_2 = data['helm_color2']
            self.helm_color_3 = data['helm_color3']
            self.helm_pattern = data['helm_pattern']
            self.host_id = data['hostid']
            self.incidents = data['incidents']
            self.interval = data['interval']
            self.interval_class = data['classinterval']
            self.irating_new = data['newirating']
            self.irating_old = data['oldirating']
            self.lap_avg = data['avglap']
            self.lap_best = data['bestlaptime']
            self.lap_best_n = data['bestlapnum']
            self.lap_qual_best = data['bestquallaptime']
            self.lap_qual_best_at = data['bestquallapat']
            self.lap_qual_best_n = data['bestquallapnum']
            self.lap_qual_best_time = data['quallaptime']
            self.laps_best_n_num = data['bestnlapsnum']
            self.laps_best_n_time = data['bestnlapstime']
            self.laps_comp = data['lapscomplete']
            self.laps_led = data['lapslead']
            self.laps_opt_comp = data['optlapscomplete']
            self.league_points = data['league_points']
            self.license_category = parse_encode(data['licensecategory'])
            self.license_change_oval = data['license_change_oval']
            self.license_change_road = data['license_change_road']
            self.license_class = data['licensegroup']
            self.license_level_new = data['newlicenselevel']
            self.license_level_old = data['oldlicenselevel']
            self.multiplier = data['multiplier']
            self.official = data['officialsession']
            self.pct_fuel_fill_max = data['max_pct_fuel_fill']
            self.points_champ = data['champpoints']
            self.points_champ_agg = data['aggchamppoints']
            self.pos = data['pos']
            self.pos_finish = data['finishpos']
            self.pos_finish_class = data['finishposinclass']
            self.pos_start = data['startpos']
            self.reason_out = parse_encode(data['reasonout'])
            self.reason_out_id = data['reasonoutid']
            self.restrict_results = parse_encode(data['restrictresults'])
            self.sim_ses_name = parse_encode(data['simsesname'])
            self.sim_ses_num = data['simsesnum']
            self.sim_ses_type_name = parse_encode(data['simsestypename'])
            self.sub_level_new = data['newsublevel']
            self.sub_level_old = data['oldsublevel']
            self.suit_color_1 = data['suit_color1']
            self.suit_color_2 = data['suit_color2']
            self.suit_color_3 = data['suit_color3']
            self.suit_pattern = data['suit_pattern']
            self.time_session_start = data['sessionstarttime']
            self.track_cat_id = data['track_catid']
            self.track_category = parse_encode(data['track_category'])
            self.ttrating_new = data['newttrating']
            self.ttrating_old = data['oldttrating']
            self.vehicle_key_id = data['vehiclekeyid']
            self.weight_penalty_kg = data['weight_penalty_kg']
            self.wheel_chrome = data['wheel_chrome']
            self.wheel_color = parse_encode(data['wheel_color'])


# Race laps for all drivers of a session
class RaceLapsAll:
    def __init__(self, data):
        self.details = self.Details(data['details'])
        self.drivers = [self.Driver(x) for x in data['startgrid']]
        self.laps = [self.Lap(x) for x in data['lapdata']]

    class Details:
        def __init__(self, data):
            self.date = data['eventDate']
            self.date_unix_utc_ms = data['eventDateUTCMilliSecs']
            self.driver_changes = data['driverChanges']
            self.event_type = data['eventType']
            self.event_type_name = parse_encode(data['eventTypeName'])
            self.laps_for_qual_avg = data['nLapsForQualAvg']
            self.laps_for_solo_avg = data['nLapsForSoloAvg']
            self.official = data['officialSession']
            self.private_session_id = data['privateSessionID']
            self.private_session_name = parse_encode(
                                        data['privateSessionName'])
            self.race_panel_img = parse_encode(data['race_panel_img'])
            self.race_week = data['raceWeek']
            self.season_id = data['seasonID']
            self.season_name = parse_encode(data['seasonName'])
            self.season_name_short = parse_encode(data['seasonShortName'])
            self.series_name = parse_encode(data['seriesName'])
            self.series_name_short = parse_encode(data['seriesShortName'])
            self.session_id = data['sessionId']
            self.subsession_id = data['subSessionId']
            self.track = parse_encode(data['trackName'])
            self.track_config = parse_encode(data['trackConfig'])
            self.track_id = data['trackid']

    class Driver:
        def __init__(self, data):
            self.car_num = data['carnum']
            self.cust_id = data['custid']
            self.display_name = parse_encode(data['displayName'])
            self.friend = data['friend']
            self.group_id = data['groupid']
            self.helmet_color_1 = data['helmetColor1']
            self.helmet_color_2 = data['helmetColor2']
            self.helmet_color_3 = data['helmetColor3']
            self.helmet_pattern = data['helmetPattern']
            self.incidents = data['numIncidents']
            self.lap_avg = data['avgLapTime']
            self.lap_best_num = data['fastestLapNum']
            self.lap_best_time = data['fastestLapTime']
            self.license_color = data['licenseColor']
            self.points_champ = data['points']
            self.pos_finish = data['finishPos']
            self.pos_start = data['startPos']
            self.watch = data['watch']

    class Lap:
        def __init__(self, data):
            self.car_num = data['carnum']
            self.cust_id = data['custid']
            self.flags = data['flags']
            self.lap_num = data['lapnum']
            self.time_ses = data['sesTime']


# Race laps for single driver of a session
class RaceLapsDriver:
    def __init__(self, data):
        self.drivers = [self.Driver(x) for x in data['drivers']]
        self.header = self.Header(data['header'])
        self.laps = [self.Lap(x) for x in data['lapData']]

    class Lap:
        def __init__(self, data):
            self.cust_id = data['custid']
            self.flags = data['flags']
            self.lap_num = data['lap_num']
            self.time_ses = data['ses_time']

    class Header:
        def __init__(self, data):
            self.car_color_1 = data['carColor1']
            self.car_color_2 = data['carColor2']
            self.car_color_3 = data['carColor3']
            self.car_id = data['carid']
            self.car_num = data['carNum']
            self.car_pattern = data['carPattern']
            self.date_unix_utc_ms = data['eventDateUTCMilliSecs']
            self.event_date = data['eventDate']
            self.event_type = data['eventtype']
            self.event_type_name = parse_encode(data['eventTypeName'])
            self.laps_for_qual = data['nlapsforqual']
            self.laps_for_solo = data['nlapsforsolo']
            self.season_name = parse_encode(data['seasonName'])
            self.season_name_short = parse_encode(data['seasonShortName'])
            self.series_name = parse_encode(data['seriesName'])
            self.series_name_short = parse_encode(data['seriesShortName'])
            self.session_id = data['sessionId']
            self.subsession_id = data['subSessionId']
            self.suit_color_1 = data['suitColor1']
            self.suit_color_2 = data['suitColor2']
            self.suit_color_3 = data['suitColor3']
            self.suit_pattern = data['suitPattern']
            self.team_name = parse_encode(data['teamName'])
            self.track_config = parse_encode(data['trackConfig'])
            self.track_id = data['trackID']
            self.track_name = parse_encode(data['trackName'])

    class Driver:
        def __init__(self, data):
            self.cust_id = data['custid']
            self.display_name = parse_encode(data['displayname'])
            self.helm_color_1 = data['helm_color1']
            self.helm_color_2 = data['helm_color2']
            self.helm_color_3 = data['helm_color3']
            self.helm_pattern = data['helm_pattern']
            self.lap_best = data['bestlaptime']
            self.lap_best_n = data['bestlapnum']
            self.lap_qual_best = data['bestquallaptime']
            self.lap_qual_best_at = data['bestquallapat']
            self.lap_qual_best_n = data['bestquallapnum']
            self.laps_n_best_num = data['bestnlapsnum']
            self.laps_n_best_time = data['bestnlapstime']
            self.license_level = data['licenselevel']
