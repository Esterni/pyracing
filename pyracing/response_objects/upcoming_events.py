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
        self.allow_entry = data['allowEntry']
        self.cars_left = data['carsLeft']
        self.cat_id = data['catid']
        self.count_group = data['groupcount']
        self.count_registered = parse_encode(data['registeredcount'])
        self.count_total = data['totalcount']
        self.driver_change_param_1 = data['driver_change_param1']
        self.driver_change_param_2 = data['driver_change_param2']
        self.driver_change_rule = data['driver_change_rule']
        self.driver_changes = data['driver_changes']
        self.drivers_connected = data['driversConnected']
        self.drivers_registered = data['driversRegistered']
        self.earth_rotation_speedup = data['earth_rotation_speedup']
        self.farm_id = data['farmid']
        self.fog_density = data['weather_fog_density']
        self.humidity = data['weather_rh']
        self.leave_marbles = data['leavemarbles']
        self.pits = parse_encode(data['pits'])
        self.pits_in_use = data['pitsInUse']
        self.pits_total = data['pitsTotal']
        self.race_panel_img = parse_encode(data['race_panel_img'])
        self.rubber_practice = data['rubberlevelpractice']
        self.rubber_qualify = data['rubberlevelqualify']
        self.rubber_race = data['rubberlevelrace']
        self.rubber_warmup = data['rubberlevelwarmup']
        self.season_id = data['seasonid']
        self.series_abbrv = parse_encode(data['seriesabbrv'])
        self.series_id = data['seriesid']
        self.series_name = parse_encode(data['seriesname'])
        self.session_id = data['sessionid']
        self.skies = data['weather_skies']
        self.subsession_id = data['subsessionid']
        self.team_drivers_max = data['max_team_drivers']
        self.team_drivers_min = data['min_team_drivers']
        self.temp_unit = data['weather_temp_units']
        self.temp_value = data['weather_temp_value']
        self.time_of_day = data['timeOfDay']
        self.time_start = parse_encode(data['time'])
        self.time_start_sim = parse_encode(data['simulatedstarttime'])
        self.total_groups = data['totalgroups']
        self.track_config = parse_encode(data['trackconfigname'])
        self.track_id = data['trackid']
        self.track_name = parse_encode(data['trackname'])
        self.weather_initial = data['weather_var_initial']
        self.weather_ongoing = data['weather_var_ongoing']
        self.weather_type = data['weather_type']
        self.wind_direction = data['weather_wind_dir']
        self.wind_speed_unit = data['weather_wind_speed_units']
        self.wind_speed_value = data['weather_wind_speed_value']
        # Additional attributes
        # data['gripcompoundwarmup']
        # data['gripcompoundrace']
        # data['gripcompoundqualify']
        # data['gripcompoundpractice']


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
        self.earth_rotation_speedup = data['earth_rotation_speedup']
        self.event_type_id = data['eventtypeid']
        self.fog_density = data['weatherfogdensity']
        self.group_count = data['groupcount']
        self.humidity = data['weatherrh']
        self.leave_marbles = data['leavemarbles']
        self.max_to_display = data['maxtodisplay']
        self.race_week = data['raceweek']
        self.race_week_cars = data['raceWeekCars']
        self.reg_count = data['numregistered']
        self.rubber_practice = data['rubberlevelpractice']
        self.rubber_qualify = data['rubberlevelqualify']
        self.rubber_race = data['rubberlevelrace']
        self.rubber_warmup = data['rubberlevelwarmup']
        self.season_id = data['seasonid']
        self.session_id = data['sessionid']
        self.skies = data['weatherskies']
        self.special_event_type = data['specialeventtype']
        self.temp_unit = data['weathertempunits']
        self.temp_value = data['weathertempvalue']
        self.time_of_day = data['timeOfDay']
        self.time_start = datetime_from_iracing_timestamp(data['starttime'])
        self.time_start_sim = parse_encode(data['simulatedstarttime'])
        self.total_count = data['totalcount']
        self.total_groups = data['totalgroups']
        self.track_id = data['trackid']
        self.weather_initial = data['weathervarinitial']
        self.weather_ongoing = data['weathervarongoing']
        self.weather_type = data['weathertype']
        self.wind_direction = data['weatherwinddir']
        self.wind_speed_unit = data['weatherwindspeedunits']
        self.wind_speed_value = data['weatherwindspeedvalue']
        # Additional attributes
        # data['gripcompoundwarmup']
        # data['gripcompoundrace']
        # data['gripcompoundqualify']
        # data['gripcompoundpractice']
        # data['restrictviewing']
        # Used outside of d dict; Holds refresh time of data
        # self.reloadtime = dict['reloadtime']
