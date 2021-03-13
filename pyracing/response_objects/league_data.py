from pyracing.helpers import parse_encode


class SeasonStandings:
    def __init__(self, data):
        self.cars = [SeasonCar(x) for x in data['cars']]
        self.drivers = [SeasonDriver(x) for x in data['standings']['rows']]
        self.car_classes = [SeasonCarClass(x) for x in data['carclasses']]


class SeasonCar:
    def __init__(self, data):
        self.id = data['carid']
        self.name = parse_encode(data['car_name'])
        self.team_car = data.get('team_car')
        self.car_class_id = data.get('carclassid')
        # If you search for all cars, this will be Hosted All Cars
        self.short_name = parse_encode(data.get('shortname'))


class SeasonCarClass:
    def __init__(self, data):
        self.car_class_id = data['carclassid']
        self.name = parse_encode(data['name'])
        self.cars = [SeasonCar(x) for x in data.get('cars_in_class')]


class SeasonDriver:
    def __init__(self, data):
        self.wins = data['wins']
        self.base_points = data['base_points']
        self.total_points = data['total_points']
        self.position = data['pos']
        self.display_name = parse_encode(data['displayname'])
        self.cust_id = data.get('custid')
        self.avg_finish = data.get('avg_finish')
        self.avg_start = data.get('avg_start')
        self.driver_nickname = parse_encode(data.get('driver_nickname'))
        self.pattern = data.get('pattern')
        self.helmet_type = data.get('helmettype')
        self.license_level = data.get('licenselevel')
        self.total_adjustments = data.get('total_adjustments')
        self.color3 = data.get('color3')
        self.color2 = data.get('color2')
        self.color1 = data.get('color1')
        self.car_number = data.get('car_number')
        self.positive_adjustments = data.get('positive_adjustments')
        self.negative_adjustments = data.get('negative_adjustments')
        self.rn = data.get('rn')
        self.facetype = data.get('facetype')


class League:
    def __init__(self, data):
        self.league_id = data['leagueID']
        self.name = parse_encode(data['name'])
        self.created_date = data['createdDate']
        self.message = parse_encode(data['message'])
        self.url = parse_encode(data['url'])
        self.rules = parse_encode(data['rules'])
        self.about = parse_encode(data['about'])
        self.cust_id = data['custID']
        self.recruiting = data['recruiting']
        self.hidden = data.get('hidden')
        self.private_wall = data.get('privateWall')
        self.private_results = data.get('privateResults')
        self.private_schedule = data.get('privateSchedule')
        self.private_roster = data.get('privateRoster')


class LeagueSeason:
    def __init__(self, data):
        self.season_id = data['1']
        self.league_points_system_description = parse_encode(data['13'])
        self.league_points_system_name = parse_encode(data['2'])
        self.league_points_system_id = data['5']
        self.active = data['6']
        self.league_season_name = parse_encode(data['8'])
        self.league_id = data['10']
