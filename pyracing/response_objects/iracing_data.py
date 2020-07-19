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
        self.date_end = data.get('end')
        self.is_lite = data.get('islite')
        self.license_eligible = data.get('licenseEligible')
        self.season_quarter = data.get('quarter')
        self.race_week = data.get('raceweek')
        self.season_id = data.get('seasonid')
        self.series_id = data.get('seriesid')
        self.series_lic_group_id = data.get('serieslicgroupid')
        self.series_name_short = parse_encode(data.get('seriesshortname'))
        self.date_start = data.get('start')
        self.season_year = data.get('year')
        # Creating subclasses from nested lists
        self.car_classes = [self.SeasonCarClass(x) for
                            x in data.get('carclasses', [])]
        self.tracks = [self.Track(x) for x in data.get('tracks', [])]
        self.cars = [self.SeasonCar(x) for x in data.get('cars', [])]

    class Track:
        def __init__(self, data):
            self.track_config = data['config']
            self.name_lower = parse_encode(data['lowername'])
            self.pkg_id = data['pkgid']
            self.priority = data['priority']
            self.race_week = data['raceweek']
            self.time_of_day = data['timeOfDay']

    # The Season endpoint returns more data for a car than other places
    class SeasonCar(Car):
        def __init__(self, data):
            super().__init__(data)
            self.id = data['id']
            self.name_lower = parse_encode(data['lowername'])
            self.name = data['name']
            self.pkg_id = data['pkgid']
            self.sku = data['sku']

    class SeasonCarClass(CarClass):
        def __init__(self, data):
            super().__init__(data)
            self.tire_sets_dry_max = data['max_dry_tire_sets']


class MemberDivision:
    def __init__(self, dict):
        self.division = dict['division']
        self.projected_division = dict['isProjected']
