from ..constants import parse_iracing_string


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
        self.category = parse_iracing_string(dict['category'])
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
        self.category = parse_iracing_string(dict['category'])
        self.starts = dict['starts']


class LastRacesStats:
    def __init__(self, dict):
        self.startPos = dict['startPos']
        self.lapsLed = dict['lapsLed']
        self.finishPos = dict['finishPos']
        self.incidents = dict['incidents']
        self.trackName = parse_iracing_string(dict['trackName'])
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
        self.current_champ_points = dict['champPoints']
        self.weeks = dict['weeks']
        self.lapsLead = dict['lapsLead']
        self.laps = dict['laps']
        self.avgStart = dict['avgStart']
        self.avgFinish = dict['avgFinish']
        self.seriesID = dict['seriesID']
        self.seasonShortName = parse_iracing_string(dict['seasonShortName'])
        self.division = dict['division']
        self.seasonID = dict['seasonID']
        self.series = parse_iracing_string(dict['series'])
        self.top5 = dict['top5']
        self.seasonName = parse_iracing_string(dict['seasonName'])
        self.incidents = dict['incidents']
        self.clubPoints = dict['clubPoints']
        self.position = dict['position']
        self.starts = dict['starts']
        self.seriesShortName = parse_iracing_string(dict['seriesShortName'])
        self.carClass = dict['carClass']


class PersonalBests:
    def __init__(self, dict):
        self.track_config = parse_iracing_string(dict['trackconfigname'])
        self.event_type = dict['eventtypename']
        self.track_id = dict['trackid']
        self.best_lap = parse_iracing_string(dict['bestlaptimeformatted'])
        self.track_name = parse_iracing_string(dict['trackname'])
