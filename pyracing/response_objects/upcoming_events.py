

class NextEvent:
    def __init__(self, dict):
        self.start_time = dict['start_time']
        self.seasonid = dict['seasonid']
        self.sessionid = dict['sessionid']
        self.drivercount = dict['drivercount']


# Needs to have fix applied to data before
class TotalRegistered:
    def __init__(self, dict):
        self.season_id = dict['seasonid']
        self.registered = dict['registered']


class ActiveOPCount:
    def __init__(self, dict):
        self.weather_temp_units = dict['weather_temp_units']
        self.weather_wind_dir = dict['weather_wind_dir']
        self.weather_temp_value = dict['weather_temp_value']
        self.min_team_drivers = dict['min_team_drivers']
        self.sessionid = dict['sessionid']
        self.pits = dict['pits']
        self.driver_change_param1 = dict['driver_change_param1']
        self.driver_change_param2 = dict['driver_change_param2']
        self.driversRegistered = dict['driversRegistered']
        self.allowEntry = dict['allowEntry']
        self.seriesname = dict['seriesname']
        self.rubberlevelpractice = dict['rubberlevelpractice']
        self.weather_fog_density = dict['weather_fog_density']
        self.rubberlevelwarmup = dict['rubberlevelwarmup']
        self.rubberlevelrace = dict['rubberlevelrace']
        self.race_panel_img = dict['race_panel_img']
        self.seriesid = dict['seriesid']
        self.timeOfDay = dict['timeOfDay']
        self.simulatedstarttime = dict['simulatedstarttime']
        self.totalgroups = dict['totalgroups']
        self.seasonid = dict['seasonid']
        self.trackid = dict['trackid']
        self.carsLeft = dict['carsLeft']
        self.weather_type = dict['weather_type']
        self.farmid = dict['farmid']
        self.weather_skies = dict['weather_skies']
        self.catid = dict['catid']
        self.driver_change_rule = dict['driver_change_rule']
        self.weather_var_ongoing = dict['weather_var_ongoing']
        self.groupcount = dict['groupcount']
        self.subsessionid = dict['subsessionid']
        self.earth_rotation_speedup = dict['earth_rotation_speedup']
        self.leavemarbles = dict['leavemarbles']
        self.trackname = dict['trackname']
        self.pitsInUse = dict['pitsInUse']
        self.totalcount = dict['totalcount']
        self.trackconfigname = dict['trackconfigname']
        self.weather_rh = dict['weather_rh']
        self.rubberlevelqualify = dict['rubberlevelqualify']
        self.weather_var_initial = dict['weather_var_initial']
        self.seriesabbrv = dict['seriesabbrv']
        self.driversConnected = dict['driversConnected']
        self.max_team_drivers = dict['max_team_drivers']
        self.weather_wind_speed_value = dict['weather_wind_speed_value']
        self.registeredcount = dict['registeredcount']
        self.time = dict['time']
        self.driver_changes = dict['driver_changes']
        self.pitsTotal = dict['pitsTotal']
        self.weather_wind_speed_units = dict['weather_wind_speed_units']


# I'm giving it my best guess here. This one has lots of nesting.
class RaceGuide:
    def __init__(self, dict):
        self.catID = dict['catID']
        self.image = dict['image']
        self.seasonSchedules = dict['seasonSchedules']
        self.seriesName = dict['seriesName']
        self.eligible = dict['eligible']
        self.seriesID = dict['seriesID']
        self.mpr = dict['mpr']

    class Schedules:
        def __init__(self, dict):
            self.seasonStartDate = dict['seasonStartDate']
            self.multiClass = dict['multiClass']
            self.seasonID = dict['seasonID']
            self.licenseGroup = dict['licenseGroup']
            self.fixedSetup = dict['fixedSetup']
            self.carClasses = dict['carClasses']
            self.races = dict['races']
            self.openPracticeDrivers = dict['openPracticeDrivers']
            self.openPracticeSessions = dict['openPracticeSessions']

        class Races:
            def __init__(self, dict):
                self.preRegCount = dict['preRegCount']
                self.weatherType = dict['weatherType']
                self.weatherRelativeHumidity = dict['weatherRelativeHumidity']
                self.weatherWindSpeedValue = dict['weatherWindSpeedValue']
                self.trackID = dict['trackID']

                # raceWeekCars returns a dictionary of {weeks} >
                # each week has a dictionary of {car_id} >
                # each car has a dictionary of {car attributes}
                self.raceWeekCars = dict['raceWeekCars']
                self.sessionTypeID = dict['sessionTypeID']
                self.sessionID = dict['sessionID']
                self.trackName = dict['trackName']
                self.weatherTempUnits = dict['weatherTempUnits']
                self.weatherTempValue = dict['weatherTempValue']
                self.standingStart = dict['standingStart']
                self.evttype = dict['evttype']
                self.regCount = dict['regCount']
                self.startTime = dict['startTime']
                self.trackRaceGuideImg = dict['trackRaceGuideImg']
                self.earth_rotation_speedup = dict['earth_rotation_speedup']
                self.raceTimeLimitMinutes = dict['raceTimeLimitMinutes']
                self.specialeventtype = dict['specialeventtype']
                self.trackConfigName = dict['trackConfigName']
                self.weatherVarOngoing = dict['weatherVarOngoing']
                self.weatherSkies = dict['weatherSkies']
                self.raceLapLimit = dict['raceLapLimit']
                self.weatherWindDir = dict['weatherWindDir']
                self.raceWeekNum = dict['raceWeekNum']

                # rubberSettings contains a dictionary of {rubber attributes}
                self.rubberSettings = dict['rubberSettings']
                self.weatherFogDensity = dict['weatherFogDensity']
                self.simulatedstarttime = dict['simulatedstarttime']
                self.weatherVarInitial = dict['weatherVarInitial']
                self.endTime = dict['endTime']
                self.weatherWindSpeedUnits = dict['weatherWindSpeedUnits']
                self.timeOfDay = dict['timeOfDay']


class NextSessionTimes:
    def __init__(self, dict):
        self.maxtodisplay = dict['1']
        self.weatherwindspeedunits = dict['2']
        self.trackid = dict['3']
        self.weatherwindspeedvalue = dict['4']
        self.weatherskies = dict['5']
        self.starttime = dict['6']
        self.sessionid = dict['7']
        self.weathervarinitial = dict['8']
        self.weatherrh = dict['9']
        self.eventtypeid = dict['10']
        self.weatherwinddir = dict['11']
        self.groupcount = dict['12']
        self.rubberlevelpractice = dict['13']
        self.earth_rotation_speedup = dict['14']
        self.leavemarbles = dict['15']
        self.numregistered = dict['16']
        self.totalcount = dict['17']
        self.reloadtime = dict['18']
        self.weathertempunits = dict['19']
        self.rubberlevelwarmup = dict['20']
        self.weathertempvalue = dict['21']
        self.specialeventtype = dict['22']
        self.rubberlevelrace = dict['23']
        self.rubberlevelqualify = dict['24']
        self.weathervarongoing = dict['25']
        self.raceWeekCars = dict['26']
        self.timeOfDay = dict['27']
        self.weathertype = dict['28']
        self.simulatedstarttime = dict['29']
        self.totalgroups = dict['30']
        self.seasonid = dict['31']
        self.raceweek = dict['32']
        self.weatherfogdensity = dict['33']