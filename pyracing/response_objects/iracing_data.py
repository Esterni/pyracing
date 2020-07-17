from ..constants import parse_encode


# Common denominator for Car attributes across all data.
class Car:
    def __init__(self, data):
        self.id = data['id']
        self.name = parse_encode(data['name'])


# Common denominator for CarClass attributes across all data.
class CarClass:
    def __init__(self, dict):
        self.custid = dict['custid']
        self.id = dict['id']
        self.lowername = dict['lowername']
        self.name = parse_encode(dict['name'])
        self.rel_speed = dict['relspeed']  # Speed ranking to other classes
        self.shortname = parse_encode(dict['shortname'])
        # Creating subclass from nested list
        self.cars = [Car(x) for x in dict['carsinclass']]


# I believe this maps what I would call a series, but
# iRacing calls this a season, so I want to be consistent
class Season:
    def __init__(self, data):
        self.active = data.get('active')
        self.cat_id = data.get('catid')
        self.category = data.get('category')
        self.end = data.get('end')
        self.is_lite = data.get('islite')
        self.license_eligible = data.get('licenseEligible')
        self.quarter = data.get('quarter')
        self.raceweek = data.get('raceweek')
        self.season_id = data.get('seasonid')
        self.series_id = data.get('seriesid')
        self.series_lic_group_id = data.get('serieslicgroupid')
        self.series_short_name = parse_encode(data.get('seriesshortname'))
        self.start = data.get('start')
        self.year = data.get('year')
        # Creating subclasses from nested lists
        self.car_classes = [self.SeasonCarClass(x) for
                            x in data.get('carclasses', [])]
        self.tracks = [self.Track(x) for x in data.get('tracks', [])]
        self.cars = [self.SeasonCar(x) for x in data.get('cars', [])]

    class Track:
        def __init__(self, data):
            self.config = data['config']
            self.lowername = parse_encode(data['lowername'])
            self.pkgid = data['pkgid']
            self.priority = data['priority']
            self.raceweek = data['raceweek']
            self.timeOfDay = data['timeOfDay']

    # The Season endpoint returns more data for a car than other places
    class SeasonCar(Car):
        def __init__(self, data):
            super().__init__(data)
            self.id = data['id']
            self.lowername = parse_encode(data['lowername'])
            self.name = data['name']
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
