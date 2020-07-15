

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
        self.weather_temp_units = dict['1']
        self.weather_wind_dir = dict['2']
        self.weather_temp_value = dict['3']
        self.min_team_drivers = dict['4']
        self.sessionid = dict['5']
        self.pits = dict['6']
        self.driver_change_param1 = dict['7']
        self.driver_change_param2 = dict['8']
        self.driversRegistered = dict['9']
        self.allowEntry = dict['10']
        self.seriesname = dict['11']
        self.rubberlevelpractice = dict['12']
        self.weather_fog_density = dict['13']
        self.rubberlevelwarmup = dict['14']
        self.rubberlevelrace = dict['15']
        self.race_panel_img = dict['16']
        self.seriesid = dict['17']
        self.timeOfDay = dict['18']
        self.simulatedstarttime = dict['19']
        self.totalgroups = dict['20']
        self.seasonid = dict['21']
        self.trackid = dict['22']
        self.carsLeft = dict['23']
        self.weather_type = dict['24']
        self.farmid = dict['25']
        self.weather_skies = dict['26']
        self.catid = dict['27']
        self.driver_change_rule = dict['28']
        self.weather_var_ongoing = dict['29']
        self.groupcount = dict['30']
        self.subsessionid = dict['31']
        self.earth_rotation_speedup = dict['32']
        self.leavemarbles = dict['33']
        self.trackname = dict['34']
        self.pitsInUse = dict['35']
        self.totalcount = dict['36']
        self.trackconfigname = dict['37']
        self.weather_rh = dict['38']
        self.rubberlevelqualify = dict['39']
        self.weather_var_initial = dict['40']
        self.seriesabbrv = dict['41']
        self.driversConnected = dict['42']
        self.max_team_drivers = dict['43']
        self.weather_wind_speed_value = dict['44']
        self.registeredcount = dict['45']
        self.time = dict['46']
        self.driver_changes = dict['47']
        self.pitsTotal = dict['48']
        self.weather_wind_speed_units = dict['49']


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
        # Unsure where this is used, but it's outside of the 'd' dictionary
        # self.reloadtime = dict['18']
