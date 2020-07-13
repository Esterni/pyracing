class CareerStats:
    def __init__(self, dict):
        self.wins = dict['wins']
        self.winPerc = round(dict['winPerc'], 2)
        self.poles = dict['poles']
        self.totalclubpoints = dict['totalclubpoints']
        self.avgStart = round(dict['avgStart'], 2)
        self.avgFinish = round(dict['avgFinish'], 2)
        self.top5Perc = round(dict['top5Perc'], 2)
        self.totalLaps = dict['totalLaps']
        self.avgIncPerRace = round(dict['avgIncPerRace'], 2)
        self.avgPtsPerRace = round(dict['avgPtsPerRace'], 2)
        self.lapsLed = dict['lapsLed']
        self.top5 = dict['top5']
        self.lapsLedPerc = round(dict['lapsLedPerc'], 2)
        self.category = dict['category'].replace('+', ' ')
        self.starts = dict['starts']


class YearlyStats:
    def __init__(self, dict):
        self.wins = dict['wins']
        self.winPerc = round(dict['winPerc'], 2)
        self.year = dict['year']
        self.poles = dict['poles']
        self.clubpoints = dict['clubpoints']
        self.avgStart = round(dict['avgStart'], 2)
        self.avgFinish = round(dict['avgFinish'], 2)
        self.top5Perc = round(dict['top5Perc'], 2)
        self.totalLaps = dict['totalLaps']
        self.avgIncPerRace = round(dict['avgIncPerRace'], 2)
        self.avgPtsPerRace = round(dict['avgPtsPerRace'], 2)
        self.lapsLed = dict['lapsLed']
        self.top5 = dict['top5']
        self.lapsLedPerc = round(dict['lapsLedPerc'], 2)
        self.category = dict['category'].replace('+', ' ')
        self.starts = dict['starts']


class LastRaceStats:
    def __init__(self, dict):
        self.startPos = dict['startPos']
        self.lapsLed = dict['lapsLed']
        self.finishPos = dict['finishPos']
        self.incidents = dict['incidents']
        self.trackName = dict['trackName']\
            .replace('+', ' ')\
            .replace('%5B', '(')\
            .replace('%5D', ')')\
            .replace('%C3%BC', 'u')
        self.sof = dict['sof']
        self.date = dict['date']
        self.seriesID = dict['seriesID']
        self.time = dict['time']
        self.winnerName = dict['winnerName']
        self.winnerID = dict['winnerID']
        self.clubPoints = dict['clubPoints']
        self.champPoints = dict['champPoints']
        self.subsessionID = dict['subsessionID']
        self.seasonID = dict['seasonID']
        self.winnerLL = dict['winnerLL']


class LastSeries:
    def __init__(self, dict):
        self.champPoints
        self.weeks
        self.lapsLead
        self.laps
        self.avgStart
        self.avgFinish
        self.seriesID
        self.seasonShortName
        self.division
        self.seasonID
        self.series
        self.top5
        self.seasonName
        self.incidents
        self.clubPoints
        self.position
        self.starts
        self.seriesShortName
        self.carClass


class PersonalBests:
    def __init__(self, dict):
        self.trackconfigname
        self.eventtypename
        self.trackid
        self.bestlaptimeformatted
        self.trackname
