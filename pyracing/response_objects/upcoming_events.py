

class NextEvent:
    def __init__(self, dict):
        self.drivercount = dict['drivercount']
        self.seasonid = dict['seasonid']
        self.sessionid = dict['sessionid']
        self.start_time = dict['start_time']


# Needs to have fix applied to data before
class TotalRegistered:
    def __init__(self, dict):
        self.registered = dict['registered']
        self.season_id = dict['seasonid']


class ActiveOPCount:
    def __init__(self, dict):
        self.allowEntry = dict['10']
        self.carsLeft = dict['23']
        self.catid = dict['27']
        self.driver_change_param1 = dict['7']
        self.driver_change_param2 = dict['8']
        self.driver_change_rule = dict['28']
        self.driver_changes = dict['47']
        self.driversConnected = dict['42']
        self.driversRegistered = dict['9']
        self.earth_rotation_speedup = dict['32']
        self.farmid = dict['25']
        self.groupcount = dict['30']
        self.leavemarbles = dict['33']
        self.max_team_drivers = dict['43']
        self.min_team_drivers = dict['4']
        self.pits = dict['6']
        self.pitsInUse = dict['35']
        self.pitsTotal = dict['48']
        self.race_panel_img = dict['16']
        self.registeredcount = dict['45']
        self.rubberlevelpractice = dict['12']
        self.rubberlevelqualify = dict['39']
        self.rubberlevelrace = dict['15']
        self.rubberlevelwarmup = dict['14']
        self.seasonid = dict['21']
        self.seriesabbrv = dict['41']
        self.seriesid = dict['17']
        self.seriesname = dict['11']
        self.sessionid = dict['5']
        self.simulatedstarttime = dict['19']
        self.subsessionid = dict['31']
        self.time = dict['46']
        self.timeOfDay = dict['18']
        self.totalcount = dict['36']
        self.totalgroups = dict['20']
        self.trackconfigname = dict['37']
        self.trackid = dict['22']
        self.trackname = dict['34']
        self.weather_fog_density = dict['13']
        self.weather_rh = dict['38']
        self.weather_skies = dict['26']
        self.weather_temp_units = dict['1']
        self.weather_temp_value = dict['3']
        self.weather_type = dict['24']
        self.weather_var_initial = dict['40']
        self.weather_var_ongoing = dict['29']
        self.weather_wind_dir = dict['2']
        self.weather_wind_speed_units = dict['49']
        self.weather_wind_speed_value = dict['44']


class RaceGuide:
    def __init__(self, dict):
        self.catID = dict['catID']
        self.eligible = dict['eligible']
        self.image = dict['image']
        self.mpr = dict['mpr']
        self.seriesID = dict['seriesID']
        self.seriesName = dict['seriesName']
        self.seasonSchedule = [self.Schedule(x) for x in dict['seasonSchedules']]

    class Schedule:
        def __init__(self, dict):
            self.carClasses = dict['carClasses']
            self.fixedSetup = dict['fixedSetup']
            self.licenseGroup = dict['licenseGroup']
            self.multiClass = dict['multiClass']
            self.openPracticeDrivers = dict['openPracticeDrivers']
            self.openPracticeSessions = dict['openPracticeSessions']
            self.seasonID = dict['seasonID']
            self.seasonStartDate = dict['seasonStartDate']
            self.race = [self.Race(x) for x in dict['races']]

        class Race:
            def __init__(self, dict):
                self.earth_rotation_speedup = dict['earth_rotation_speedup']
                self.endTime = dict['endTime']
                self.evttype = dict['evttype']
                self.preRegCount = dict['preRegCount']
                self.raceLapLimit = dict['raceLapLimit']
                self.raceTimeLimitMinutes = dict['raceTimeLimitMinutes']
                self.raceWeekNum = dict['raceWeekNum']
                self.regCount = dict['regCount']
                self.sessionID = dict['sessionID']
                self.sessionTypeID = dict['sessionTypeID']
                self.simulatedstarttime = dict['simulatedstarttime']
                self.specialeventtype = dict['specialeventtype']
                self.standingStart = dict['standingStart']
                self.startTime = dict['startTime']
                self.timeOfDay = dict['timeOfDay']
                self.trackConfigName = dict['trackConfigName']
                self.trackID = dict['trackID']
                self.trackName = dict['trackName']
                self.trackRaceGuideImg = dict['trackRaceGuideImg']
                self.weatherFogDensity = dict['weatherFogDensity']
                self.weatherRelativeHumidity = dict['weatherRelativeHumidity']
                self.weatherSkies = dict['weatherSkies']
                self.weatherTempUnits = dict['weatherTempUnits']
                self.weatherTempValue = dict['weatherTempValue']
                self.weatherType = dict['weatherType']
                self.weatherVarInitial = dict['weatherVarInitial']
                self.weatherVarOngoing = dict['weatherVarOngoing']
                self.weatherWindDir = dict['weatherWindDir']
                self.weatherWindSpeedUnits = dict['weatherWindSpeedUnits']
                self.weatherWindSpeedValue = dict['weatherWindSpeedValue']

                # raceWeekCars returns a dictionary of {weeks} >
                # each week has a dictionary of {car_id} >
                # each car has a dictionary of {car attributes}
                self.raceWeekCars = dict['raceWeekCars']

                # rubberSettings contains a dictionary of {rubber attributes}
                self.rubberSettings = dict['rubberSettings']


class NextSessionTimes:
    def __init__(self, dict):
        self.earth_rotation_speedup = dict['14']
        self.eventtypeid = dict['10']
        self.groupcount = dict['12']
        self.leavemarbles = dict['15']
        self.maxtodisplay = dict['1']
        self.numregistered = dict['16']
        self.raceweek = dict['32']
        self.raceWeekCars = dict['26']
        self.rubberlevelpractice = dict['13']
        self.rubberlevelqualify = dict['24']
        self.rubberlevelrace = dict['23']
        self.rubberlevelwarmup = dict['20']
        self.seasonid = dict['31']
        self.sessionid = dict['7']
        self.simulatedstarttime = dict['29']
        self.specialeventtype = dict['22']
        self.starttime = dict['6']
        self.timeOfDay = dict['27']
        self.totalcount = dict['17']
        self.totalgroups = dict['30']
        self.trackid = dict['3']
        self.weatherfogdensity = dict['33']
        self.weatherrh = dict['9']
        self.weatherskies = dict['5']
        self.weathertempunits = dict['19']
        self.weathertempvalue = dict['21']
        self.weathertype = dict['28']
        self.weathervarinitial = dict['8']
        self.weathervarongoing = dict['25']
        self.weatherwinddir = dict['11']
        self.weatherwindspeedunits = dict['2']
        self.weatherwindspeedvalue = dict['4']
        # Used outside of d dict; Holds refresh time of data
        # self.reloadtime = dict['18']
