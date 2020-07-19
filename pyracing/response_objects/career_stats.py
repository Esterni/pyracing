from ..constants import parse_encode


class CareerStats:
    def __init__(self, dict):
        self.pos_finish_avg = round(dict['avgFinish'], 2)
        self.incidents_avg = round(dict['avgIncPerRace'], 2)
        self.points_avg = round(dict['avgPtsPerRace'], 2)
        self.pos_start_avg = round(dict['avgStart'], 2)
        self.category = parse_encode(dict['category'])
        self.laps_led_total = dict['lapsLed']
        self.laps_led_total_pcnt = round(dict['lapsLedPerc'], 2)
        self.poles = dict['poles']
        self.starts = dict['starts']
        self.top_5s = dict['top5']
        self.top_5_pcnt = round(dict['top5Perc'], 2)
        self.points_club = dict['totalclubpoints']
        self.laps = dict['totalLaps']
        self.win_pcnt = round(dict['winPerc'], 2)
        self.wins = dict['wins']


class YearlyStats:
    def __init__(self, dict):
        self.pos_finish_avg = round(dict['avgFinish'], 2)
        self.incidents_avg = round(dict['avgIncPerRace'], 2)
        self.points_avg = round(dict['avgPtsPerRace'], 2)
        self.pos_start_avg = round(dict['avgStart'], 2)
        self.category = parse_encode(dict['category'])
        self.points_club = dict['clubpoints']
        self.laps_led = dict['lapsLed']
        self.laps_led_pcnt = round(dict['lapsLedPerc'], 2)
        self.poles = dict['poles']
        self.starts = dict['starts']
        self.top_5s = dict['top5']
        self.top_5_pcnt = round(dict['top5Perc'], 2)
        self.laps = dict['totalLaps']
        self.win_pcnt = round(dict['winPerc'], 2)
        self.wins = dict['wins']
        self.year = dict['year']


class LastRacesStats:
    def __init__(self, dict):
        self.points_champ = dict['champPoints']
        self.points_club = dict['clubPoints']
        self.date = dict['date']
        self.pos_finish = dict['finishPos']
        self.incidents = dict['incidents']
        self.laps_led_total = dict['lapsLed']
        self.season_id = dict['seasonID']
        self.series_id = dict['seriesID']
        self.strength_of_field = dict['sof']
        self.pos_start = dict['startPos']
        self.subsession_id = dict['subsessionID']
        self.time = dict['time']
        self.track = parse_encode(dict['trackName'])
        self.winner_cust_id = dict['winnerID']
        self.winner_laps_led = dict['winnerLL']
        self.winner_name = dict['winnerName']


class LastSeries:
    def __init__(self, dict):
        self.pos_finish_avg = dict['avgFinish']
        self.pos_start_avg = dict['avgStart']
        self.car_class_id = dict['carClass']
        self.points_club = dict['clubPoints']
        self.points_champ = dict['champPoints']
        self.division = dict['division']
        self.incidents = dict['incidents']
        self.laps = dict['laps']
        self.laps_led = dict['lapsLead']
        self.series_rank = dict['position']
        self.season_id = dict['seasonID']
        self.season_name = parse_encode(dict['seasonName'])
        self.season_name_short = parse_encode(dict['seasonShortName'])
        self.series = parse_encode(dict['series'])
        self.series_id = dict['seriesID']
        self.series_name_short = parse_encode(dict['seriesShortName'])
        self.starts = dict['starts']
        self.top_5s = dict['top5']
        self.weeks = dict['weeks']


class PersonalBests:
    def __init__(self, dict):
        self.lap_best = parse_encode(dict['bestlaptimeformatted'])
        self.event_type = dict['eventtypename']
        self.track_config = parse_encode(dict['trackconfigname'])
        self.track_id = dict['trackid']
        self.track_name = parse_encode(dict['trackname'])
