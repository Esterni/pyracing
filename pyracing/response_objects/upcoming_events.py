from ..helpers import datetime_from_iracing_timestamp


class NextEvent:
    def __init__(self, dict):
        self.driver_count = dict['drivercount']
        self.season_id = dict['seasonid']
        self.session_id = dict['sessionid']
        self.time_start = datetime_from_iracing_timestamp(dict['start_time'])


# Needs to have fix applied to data before
class TotalRegistered:
    def __init__(self, dict):
        self.registered = dict['registered']
        self.season_id = dict['seasonid']


class ActiveOPCount:
    def __init__(self, dict):
        self.allow_entry = dict['10']
        self.cars_left = dict['23']
        self.cat_id = dict['27']
        self.count_group = dict['30']
        self.count_registered = dict['45']
        self.count_total = dict['36']
        self.driver_change_param_1 = dict['7']
        self.driver_change_param_2 = dict['8']
        self.driver_change_rule = dict['28']
        self.driver_changes = dict['47']
        self.drivers_connected = dict['42']
        self.drivers_registered = dict['9']
        self.earth_rotation_speedup = dict['32']
        self.farm_id = dict['25']
        self.fog_density = dict['13']
        self.humidity = dict['38']
        self.leave_marbles = dict['33']
        self.pits = dict['6']
        self.pits_in_use = dict['35']
        self.pits_total = dict['48']
        self.race_panel_img = dict['16']
        self.rubber_practice = dict['12']
        self.rubber_qualify = dict['39']
        self.rubber_race = dict['15']
        self.rubber_warmup = dict['14']
        self.season_id = dict['21']
        self.series_abbrv = dict['41']
        self.series_id = dict['17']
        self.series_name = dict['11']
        self.session_id = dict['5']
        self.skies = dict['26']
        self.subsession_id = dict['31']
        self.team_drivers_max = dict['43']
        self.team_drivers_min = dict['4']
        self.temp_unit = dict['1']
        self.temp_value = dict['3']
        self.time_of_day = dict['18']
        self.time_start = dict['46']
        self.time_start_sim = dict['19']
        self.total_groups = dict['20']
        self.track_config = dict['37']
        self.track_id = dict['22']
        self.track_name = dict['34']
        self.weather_initial = dict['40']
        self.weather_ongoing = dict['29']
        self.weather_type = dict['24']
        self.wind_direction = dict['2']
        self.wind_speed_unit = dict['49']
        self.wind_speed_value = dict['44']


class RaceGuide:
    def __init__(self, dict):
        self.cat_id = dict['catID']
        self.eligible = dict['eligible']
        self.image = dict['image']
        self.meets_participation_req = dict['mpr']
        self.season_schedule = [self.Schedule(x) for x in dict['seasonSchedules']]
        self.series_id = dict['seriesID']
        self.series_name = dict['seriesName']

    class Schedule:
        def __init__(self, dict):
            self.car_class_ids = dict['carClasses']
            self.fixed_setup = dict['fixedSetup']
            self.license_class = dict['licenseGroup']
            self.multi_class = dict['multiClass']
            self.open_practice_drivers = dict['openPracticeDrivers']
            self.open_practice_sessions = dict['openPracticeSessions']
            self.race = [self.Race(x) for x in dict['races']]
            self.season_id = dict['seasonID']
            self.season_start_date = dict['seasonStartDate']

        class Race:
            def __init__(self, dict):
                self.earth_rotation_speedup = dict['earth_rotation_speedup']
                self.event_type = dict['evttype']
                self.fog_density = dict['weatherFogDensity']
                self.humidity = dict['weatherRelativeHumidity']
                self.race_lap_limit = dict['raceLapLimit']
                self.race_time_limit_minutes = dict['raceTimeLimitMinutes']
                self.race_week = dict['raceWeekNum']
                self.reg_count = dict['regCount']
                self.reg_count_pre = dict['preRegCount']
                self.session_id = dict['sessionID']
                self.session_type_id = dict['sessionTypeID']
                self.skies = dict['weatherSkies']
                self.special_event_type = dict['specialeventtype']
                self.standing_start = dict['standingStart']
                self.temp_unit = dict['weatherTempUnits']
                self.temp_value = dict['weatherTempValue']
                self.time_end = dict['endTime']
                self.time_of_day = dict['timeOfDay']
                self.time_start = dict['startTime']
                self.time_start_sim = dict['simulatedstarttime']
                self.track = dict['trackName']
                self.track_config = dict['trackConfigName']
                self.track_id = dict['trackID']
                self.track_race_guide_img = dict['trackRaceGuideImg']
                self.weather_initial = dict['weatherVarInitial']
                self.weather_ongoing = dict['weatherVarOngoing']
                self.weather_type = dict['weatherType']
                self.wind_direction = dict['weatherWindDir']
                self.wind_speed_unit = dict['weatherWindSpeedUnits']
                self.wind_speed_value = dict['weatherWindSpeedValue']

                # raceWeekCars returns a dictionary of {weeks} >
                # each week has a dictionary of {car_id} >
                # each car has a dictionary of {car attributes}
                self.race_week_cars = dict['raceWeekCars']

                # rubberSettings contains a dictionary of {rubber attributes}
                self.rubber_settings = dict['rubberSettings']


class NextSessionTimes:
    def __init__(self, dict):
        self.earth_rotation_speedup = dict['14']
        self.event_type_id = dict['10']
        self.fog_density = dict['33']
        self.group_count = dict['12']
        self.humidity = dict['9']
        self.leave_marbles = dict['15']
        self.max_to_display = dict['1']
        self.race_week = dict['32']
        self.race_week_cars = dict['26']
        self.reg_count = dict['16']
        self.rubber_practice = dict['13']
        self.rubber_qualify = dict['24']
        self.rubber_race = dict['23']
        self.rubber_warmup = dict['20']
        self.season_id = dict['31']
        self.session_id = dict['7']
        self.skies = dict['5']
        self.special_event_type = dict['22']
        self.temp_unit = dict['19']
        self.temp_value = dict['21']
        self.time_of_day = dict['27']
        self.time_start = dict['6']
        self.time_start_sim = dict['29']
        self.total_count = dict['17']
        self.total_groups = dict['30']
        self.track_id = dict['3']
        self.weather_initial = dict['8']
        self.weather_ongoing = dict['25']
        self.weather_type = dict['28']
        self.wind_direction = dict['11']
        self.wind_speed_unit = dict['2']
        self.wind_speed_value = dict['4']
        # Used outside of d dict; Holds refresh time of data
        # self.reloadtime = dict['18']
