from pyracing.helpers import parse_encode


class CareerStats:
    def __init__(self, data):
        self.category = parse_encode(data['category'])
        self.incidents_avg = round(data['avgIncPerRace'], 2)
        self.laps = data['totalLaps']
        self.laps_led = data['lapsLed']
        self.laps_led_pcnt = round(data['lapsLedPerc'], 2)
        self.points_avg = round(data['avgPtsPerRace'], 2)
        self.points_club = data['totalclubpoints']
        self.poles = data['poles']
        self.pos_finish_avg = round(data['avgFinish'], 2)
        self.pos_start_avg = round(data['avgStart'], 2)
        self.starts = data['starts']
        self.top_5_pcnt = round(data['top5Perc'], 2)
        self.top_5s = data['top5']
        self.win_pcnt = round(data['winPerc'], 2)
        self.wins = data['wins']


class YearlyStats:
    def __init__(self, data):
        self.category = parse_encode(data['category'])
        self.incidents_avg = round(data['avgIncPerRace'], 2)
        self.laps = data['totalLaps']
        self.laps_led = data['lapsLed']
        self.laps_led_pcnt = round(data['lapsLedPerc'], 2)
        self.points_avg = round(data['avgPtsPerRace'], 2)
        self.points_club = data['clubpoints']
        self.poles = data['poles']
        self.pos_finish_avg = round(data['avgFinish'], 2)
        self.pos_start_avg = round(data['avgStart'], 2)
        self.starts = data['starts']
        self.top_5_pcnt = round(data['top5Perc'], 2)
        self.top_5s = data['top5']
        self.win_pcnt = round(data['winPerc'], 2)
        self.wins = data['wins']
        self.year = data['year']


class LastRacesStats:
    def __init__(self, data):
        self.date = data['date']
        self.incidents = data['incidents']
        self.laps_led = data['lapsLed']
        self.points_champ = data['champPoints']
        self.points_club = data['clubPoints']
        self.pos_finish = data['finishPos']
        self.pos_start = data['startPos']
        self.season_id = data['seasonID']
        self.series_id = data['seriesID']
        self.strength_of_field = data['sof']
        self.subsession_id = data['subsessionID']
        self.time = data['time']
        self.track = parse_encode(data['trackName'])
        self.winner_cust_id = data['winnerID']
        self.winner_laps_led = data['winnerLL']
        self.winner_name = parse_encode(data['winnerName'])


class LastSeries:
    def __init__(self, data):
        self.car_class_id = data['carClass']
        self.division = data['division']
        self.incidents = data['incidents']
        self.laps = data['laps']
        self.laps_led = data['lapsLead']
        self.points_champ = data['champPoints']
        self.points_club = data['clubPoints']
        self.pos_finish_avg = data['avgFinish']
        self.pos_start_avg = data['avgStart']
        self.season_id = data['seasonID']
        self.season_name = parse_encode(data['seasonName'])
        self.season_name_short = parse_encode(data['seasonShortName'])
        self.series = parse_encode(data['series'])
        self.series_id = data['seriesID']
        self.series_name_short = parse_encode(data['seriesShortName'])
        self.series_rank = data['position']
        self.starts = data['starts']
        self.top_5s = data['top5']
        self.weeks = data['weeks']


class PersonalBests:
    def __init__(self, data):
        self.event_type = data['eventtypename']
        self.lap_best = parse_encode(data['bestlaptimeformatted'])
        self.track_config = parse_encode(data['trackconfigname'])
        self.track_id = data['trackid']
        self.track_name = parse_encode(data['trackname'])
