from ..constants import parse_iracing_string


# Common denominator for Car attributes across all data.
class Car:
    def __init__(self, data):
        self.name = parse_iracing_string(data['name'])
        self.id = data['id']


# Common denominator for CarClass attributes across all data.
class CarClass:
    def __init__(self, dict):
        self.rel_speed = dict['relspeed']  # Speed ranking to other classes
        self.lowername = dict['lowername']
        self.custid = dict['custid']
        self.name = parse_iracing_string(dict['name'])
        self.id = dict['id']
        self.shortname = parse_iracing_string(dict['shortname'])
        # Creating subclass from nested list
        self.cars = [Car(x) for x in dict['carsinclass']]


# I believe this maps what I would call a series, but
# iRacing calls this a season, so I want to be consistent
class Season:
    def __init__(self, data):
        self.series_lic_group_id = data.get('serieslicgroupid')
        self.year = data.get('year')
        self.start = data.get('start')
        self.active = data.get('active')
        self.is_lite = data.get('islite')
        self.series_id = data.get('seriesid')
        self.license_eligible = data.get('licenseEligible')
        self.cat_id = data.get('catid')
        self.season_id = data.get('seasonid')
        self.series_short_name = parse_iracing_string(
            data.get('seriesshortname'))
        self.end = data.get('end')
        self.category = data.get('category')
        self.raceweek = data.get('raceweek')
        self.quarter = data.get('quarter')
        # Creating subclasses from nested lists
        self.car_classes = [self.SeasonCarClass(x) for
                            x in data.get('carclasses', [])]
        self.tracks = [self.Tracks(x) for x in data.get('tracks', [])]
        self.cars = [self.SeasonCar(x) for x in data.get('cars', [])]

    class Tracks:
        def __init__(self, data):
            self.lowername = parse_iracing_string(data['lowername'])
            self.pkgid = data['pkgid']
            self.priority = data['priority']
            self.raceweek = data['raceweek']
            self.config = data['config']
            self.timeOfDay = data['timeOfDay']

    # The Season endpoint returns more data for a car than other places
    class SeasonCar(Car):
        def __init__(self, data):
            super().__init__(data)
            self.lowername = parse_iracing_string(data['lowername'])
            self.name = data['name']
            self.id = data['id']
            self.pkg_id = data['pkgid']
            self.sku = data['sku']

    class SeasonCarClass(CarClass):
        def __init__(self, data):
            super().__init__(data)
            self.max_dry_tire_sets = data['max_dry_tire_sets']


class MemberDivision:
    def __init__(self, dict):
        self.division = dict['division']
        self.projected_division = dict['isProjected']
