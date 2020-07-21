from ..helpers import parse_encode


class CareerStats:
    def __init__(self, dict):
        self.category = parse_encode(dict['category'])
        self.incidents_avg = round(dict['avgIncPerRace'], 2)
        self.laps = dict['totalLaps']
        self.laps_led = dict['lapsLed']
        self.laps_led_pcnt = round(dict['lapsLedPerc'], 2)
        self.points_avg = round(dict['avgPtsPerRace'], 2)
        self.points_club = dict['totalclubpoints']
        self.poles = dict['poles']
        self.pos_finish_avg = round(dict['avgFinish'], 2)
        self.pos_start_avg = round(dict['avgStart'], 2)
        self.starts = dict['starts']
        self.top_5_pcnt = round(dict['top5Perc'], 2)
        self.top_5s = dict['top5']
        self.win_pcnt = round(dict['winPerc'], 2)
        self.wins = dict['wins']


class YearlyStats:
    def __init__(self, dict):
        self.category = parse_encode(dict['category'])
        self.incidents_avg = round(dict['avgIncPerRace'], 2)
        self.laps = dict['totalLaps']
        self.laps_led = dict['lapsLed']
        self.laps_led_pcnt = round(dict['lapsLedPerc'], 2)
        self.points_avg = round(dict['avgPtsPerRace'], 2)
        self.points_club = dict['clubpoints']
        self.poles = dict['poles']
        self.pos_finish_avg = round(dict['avgFinish'], 2)
        self.pos_start_avg = round(dict['avgStart'], 2)
        self.starts = dict['starts']
        self.top_5_pcnt = round(dict['top5Perc'], 2)
        self.top_5s = dict['top5']
        self.win_pcnt = round(dict['winPerc'], 2)
        self.wins = dict['wins']
        self.year = dict['year']


class LastRacesStats:
    def __init__(self, dict):
        self.date = dict['date']
        self.incidents = dict['incidents']
        self.laps_led = dict['lapsLed']
        self.points_champ = dict['champPoints']
        self.points_club = dict['clubPoints']
        self.pos_finish = dict['finishPos']
        self.pos_start = dict['startPos']
        self.season_id = dict['seasonID']
        self.series_id = dict['seriesID']
        self.strength_of_field = dict['sof']
        self.subsession_id = dict['subsessionID']
        self.time = dict['time']
        self.track = parse_encode(dict['trackName'])
        self.winner_cust_id = dict['winnerID']
        self.winner_laps_led = dict['winnerLL']
        self.winner_name = dict['winnerName']


class LastSeries:
    def __init__(self, dict):
        self.car_class_id = dict['carClass']
        self.division = dict['division']
        self.incidents = dict['incidents']
        self.laps = dict['laps']
        self.laps_led = dict['lapsLead']
        self.points_champ = dict['champPoints']
        self.points_club = dict['clubPoints']
        self.pos_finish_avg = dict['avgFinish']
        self.pos_start_avg = dict['avgStart']
        self.season_id = dict['seasonID']
        self.season_name = parse_encode(dict['seasonName'])
        self.season_name_short = parse_encode(dict['seasonShortName'])
        self.series = parse_encode(dict['series'])
        self.series_id = dict['seriesID']
        self.series_name_short = parse_encode(dict['seriesShortName'])
        self.series_rank = dict['position']
        self.starts = dict['starts']
        self.top_5s = dict['top5']
        self.weeks = dict['weeks']


class PersonalBests:
    def __init__(self, dict):
        self.event_type = dict['eventtypename']
        self.lap_best = parse_encode(dict['bestlaptimeformatted'])
        self.track_config = parse_encode(dict['trackconfigname'])
        self.track_id = dict['trackid']
        self.track_name = parse_encode(dict['trackname'])
