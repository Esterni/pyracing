from ..constants import parse_encode


class CareerStats:
    def __init__(self, dict):
        self.avgFinish = round(dict['avgFinish'], 2)
        self.avgIncPerRace = round(dict['avgIncPerRace'], 2)
        self.avgPtsPerRace = round(dict['avgPtsPerRace'], 2)
        self.avgStart = round(dict['avgStart'], 2)
        self.category = parse_encode(dict['category'])
        self.lapsLed = dict['lapsLed']
        self.lapsLedPerc = round(dict['lapsLedPerc'], 2)
        self.poles = dict['poles']
        self.starts = dict['starts']
        self.top5 = dict['top5']
        self.top5Perc = round(dict['top5Perc'], 2)
        self.totalclubpoints = dict['totalclubpoints']
        self.totalLaps = dict['totalLaps']
        self.winPerc = round(dict['winPerc'], 2)
        self.wins = dict['wins']


class YearlyStats:
    def __init__(self, dict):
        self.avgFinish = round(dict['avgFinish'], 2)
        self.avgIncPerRace = round(dict['avgIncPerRace'], 2)
        self.avgPtsPerRace = round(dict['avgPtsPerRace'], 2)
        self.avgStart = round(dict['avgStart'], 2)
        self.category = parse_encode(dict['category'])
        self.clubpoints = dict['clubpoints']
        self.lapsLed = dict['lapsLed']
        self.lapsLedPerc = round(dict['lapsLedPerc'], 2)
        self.poles = dict['poles']
        self.starts = dict['starts']
        self.top5 = dict['top5']
        self.top5Perc = round(dict['top5Perc'], 2)
        self.totalLaps = dict['totalLaps']
        self.winPerc = round(dict['winPerc'], 2)
        self.wins = dict['wins']
        self.year = dict['year']


class LastRacesStats:
    def __init__(self, dict):
        self.champPoints = dict['champPoints']
        self.clubPoints = dict['clubPoints']
        self.date = dict['date']
        self.finishPos = dict['finishPos']
        self.incidents = dict['incidents']
        self.lapsLed = dict['lapsLed']
        self.seasonID = dict['seasonID']
        self.seriesID = dict['seriesID']
        self.sof = dict['sof']
        self.startPos = dict['startPos']
        self.subsessionID = dict['subsessionID']
        self.time = dict['time']
        self.trackName = parse_encode(dict['trackName'])
        self.winnerID = dict['winnerID']
        self.winnerLL = dict['winnerLL']
        self.winnerName = dict['winnerName']


class LastSeries:
    def __init__(self, dict):
        self.avgFinish = dict['avgFinish']
        self.avgStart = dict['avgStart']
        self.carClass = dict['carClass']
        self.clubPoints = dict['clubPoints']
        self.current_champ_points = dict['champPoints']
        self.division = dict['division']
        self.incidents = dict['incidents']
        self.laps = dict['laps']
        self.lapsLead = dict['lapsLead']
        self.position = dict['position']
        self.seasonID = dict['seasonID']
        self.seasonName = parse_encode(dict['seasonName'])
        self.seasonShortName = parse_encode(dict['seasonShortName'])
        self.series = parse_encode(dict['series'])
        self.seriesID = dict['seriesID']
        self.seriesShortName = parse_encode(dict['seriesShortName'])
        self.starts = dict['starts']
        self.top5 = dict['top5']
        self.weeks = dict['weeks']


class PersonalBests:
    def __init__(self, dict):
        self.best_lap = parse_encode(dict['bestlaptimeformatted'])
        self.event_type = dict['eventtypename']
        self.track_config = parse_encode(dict['trackconfigname'])
        self.track_id = dict['trackid']
        self.track_name = parse_encode(dict['trackname'])
