from pyracing.helpers import datetime_from_iracing_timestamp, parse_encode


class NextEvent:
    def __init__(self, data):
        self.driver_count = data['drivercount']
        self.season_id = data['seasonid']
        self.session_id = data['sessionid']
        self.time_start = datetime_from_iracing_timestamp(data['start_time'])


# Needs to have fix applied to data before
class TotalRegistered:
    def __init__(self, data):
        self.registered = data['registered']
        self.season_id = data['seasonid']


class OpenPractice:
    def __init__(self, data):
        self.allow_entry = data['10']
        self.cars_left = data['23']
        self.cat_id = data['27']
        self.count_group = data['30']
        self.count_registered = parse_encode(data['45'])
        self.count_total = data['36']
        self.driver_change_param_1 = data['7']
        self.driver_change_param_2 = data['8']
        self.driver_change_rule = data['28']
        self.driver_changes = data['47']
        self.drivers_connected = data['42']
        self.drivers_registered = data['9']
        self.earth_rotation_speedup = data['32']
        self.farm_id = data['25']
        self.fog_density = data['13']
        self.humidity = data['38']
        self.leave_marbles = data['33']
        self.pits = parse_encode(data['6'])
        self.pits_in_use = data['35']
        self.pits_total = data['48']
        self.race_panel_img = parse_encode(data['16'])
        self.rubber_practice = data['12']
        self.rubber_qualify = data['39']
        self.rubber_race = data['15']
        self.rubber_warmup = data['14']
        self.season_id = data['21']
        self.series_abbrv = parse_encode(data['41'])
        self.series_id = data['17']
        self.series_name = parse_encode(data['11'])
        self.session_id = data['5']
        self.skies = data['26']
        self.subsession_id = data['31']
        self.team_drivers_max = data['43']
        self.team_drivers_min = data['4']
        self.temp_unit = data['1']
        self.temp_value = data['3']
        self.time_of_day = data['18']
        self.time_start = parse_encode(data['46'])
        self.time_start_sim = parse_encode(data['19'])
        self.total_groups = data['20']
        self.track_config = parse_encode(data['37'])
        self.track_id = data['22']
        self.track_name = parse_encode(data['34'])
        self.weather_initial = data['40']
        self.weather_ongoing = data['29']
        self.weather_type = data['24']
        self.wind_direction = data['2']
        self.wind_speed_unit = data['49']
        self.wind_speed_value = data['44']


class RaceGuide:
    def __init__(self, data):
        self.cat_id = data['catID']
        self.eligible = data['eligible']
        self.image = parse_encode(data['image'])
        self.meets_participation_req = data['mpr']
        self.season_schedule = [self.Schedule(x) for
                                x in data['seasonSchedules']]
        self.series_id = data['seriesID']
        self.series_name = parse_encode(data['seriesName'])

    class Schedule:
        def __init__(self, data):
            self.car_class_ids = data['carClasses']
            self.fixed_setup = data['fixedSetup']
            self.license_class = data['licenseGroup']
            self.multi_class = data['multiClass']
            self.open_practice_drivers = data['openPracticeDrivers']
            self.open_practice_sessions = data['openPracticeSessions']
            self.race = [self.Race(x) for x in data['races']]
            self.season_id = data['seasonID']
            self.season_start_date = datetime_from_iracing_timestamp(
                data['seasonStartDate'])

        class Race:
            def __init__(self, data):
                self.earth_rotation_speedup = data['earth_rotation_speedup']
                self.event_type = data['evttype']
                self.fog_density = data['weatherFogDensity']
                self.humidity = data['weatherRelativeHumidity']
                self.race_lap_limit = data['raceLapLimit']
                self.race_time_limit_minutes = data['raceTimeLimitMinutes']
                self.race_week = data['raceWeekNum']
                self.reg_count = data['regCount']
                self.reg_count_pre = data['preRegCount']
                self.session_id = data['sessionID']
                self.session_type_id = data['sessionTypeID']
                self.skies = data['weatherSkies']
                self.special_event_type = data['specialeventtype']
                self.standing_start = data['standingStart']
                self.temp_unit = data['weatherTempUnits']
                self.temp_value = data['weatherTempValue']
                self.time_end = datetime_from_iracing_timestamp(
                    data['endTime'])
                self.time_of_day = data['timeOfDay']
                self.time_start = datetime_from_iracing_timestamp(
                    data['startTime'])
                self.time_start_sim = parse_encode(data['simulatedstarttime'])
                self.track = parse_encode(data['trackName'])
                self.track_config = parse_encode(data['trackConfigName'])
                self.track_id = data['trackID']
                self.track_race_guide_img = parse_encode(
                    data['trackRaceGuideImg'])
                self.weather_initial = data['weatherVarInitial']
                self.weather_ongoing = data['weatherVarOngoing']
                self.weather_type = data['weatherType']
                self.wind_direction = data['weatherWindDir']
                self.wind_speed_unit = data['weatherWindSpeedUnits']
                self.wind_speed_value = data['weatherWindSpeedValue']

                # raceWeekCars returns a dictionary of {weeks} >
                # each week has a dictionary of {car_id} >
                # each car has a dictionary of {car attributes}
                self.race_week_cars = data['raceWeekCars']

                # rubberSettings contains a dictionary of {rubber attributes}
                self.rubber_settings = data['rubberSettings']


class NextSessionTimes:
    def __init__(self, data):
        self.earth_rotation_speedup = data['14']
        self.event_type_id = data['10']
        self.fog_density = data['33']
        self.group_count = data['12']
        self.humidity = data['9']
        self.leave_marbles = data['15']
        self.max_to_display = data['1']
        self.race_week = data['32']
        self.race_week_cars = data['26']
        self.reg_count = data['16']
        self.rubber_practice = data['13']
        self.rubber_qualify = data['24']
        self.rubber_race = data['23']
        self.rubber_warmup = data['20']
        self.season_id = data['31']
        self.session_id = data['7']
        self.skies = data['5']
        self.special_event_type = data['22']
        self.temp_unit = data['19']
        self.temp_value = data['21']
        self.time_of_day = data['27']
        self.time_start = datetime_from_iracing_timestamp(data['6'])
        self.time_start_sim = parse_encode(data['29'])
        self.total_count = data['17']
        self.total_groups = data['30']
        self.track_id = data['3']
        self.weather_initial = data['8']
        self.weather_ongoing = data['25']
        self.weather_type = data['28']
        self.wind_direction = data['11']
        self.wind_speed_unit = data['2']
        self.wind_speed_value = data['4']
        # Used outside of d dict; Holds refresh time of data
        # self.reloadtime = dict['18']
