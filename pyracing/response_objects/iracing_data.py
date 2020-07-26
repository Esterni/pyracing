from ..helpers import parse_encode, datetime_from_iracing_timestamp


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
        self.date_start = data.get('start')
        self.is_lite = data.get('islite')
        self.license_eligible = data.get('licenseEligible')
        self.race_week = data.get('raceweek')
        self.season_id = data.get('seasonid')
        self.season_quarter = data.get('quarter')
        self.season_year = data.get('year')
        self.series_id = data.get('seriesid')
        self.series_lic_group_id = data.get('serieslicgroupid')
        self.series_name_short = parse_encode(data.get('seriesshortname'))
        # Creating subclasses from nested lists
        self.car_classes = [self.SeasonCarClass(x) for
                            x in data.get('carclasses', [])]
        self.tracks = [self.Track(x) for x in data.get('tracks', [])]
        self.cars = [self.SeasonCar(x) for x in data.get('cars', [])]

    class Track:
        def __init__(self, data):
            self.name = parse_encode(data['name'])
            self.name_lower = parse_encode(data['lowername'])
            self.pkg_id = data['pkgid']
            self.priority = data['priority']
            self.race_week = data['raceweek']
            self.time_of_day = data['timeOfDay']
            self.config = parse_encode(data['config'])

    # The Season endpoint returns more data for a car than other places
    class SeasonCar(Car):
        def __init__(self, data):
            super().__init__(data)
            self.id = data['id']
            self.name = data['name']
            self.name_lower = parse_encode(data['lowername'])
            self.pkg_id = data['pkgid']
            self.sku = data['sku']

    class SeasonCarClass(CarClass):
        def __init__(self, data):
            super().__init__(data)
            self.tire_sets_dry_max = data['max_dry_tire_sets']


class MemberDivision:
    def __init__(self, dict):
        self.division = dict['division']
        self.division_projected = dict['isProjected']


class Helmet:
    def __init__(self, dict):
        self.c3 = dict.get('c3')
        self.ll = dict.get('ll')
        self.hp = dict.get('hp')
        self.ht = dict.get('ht')
        self.c1 = dict.get('c1')
        self.ft = dict.get('ft')
        self.c2 = dict.get('c2')


class DriverStatus:
    def __init__(self, dict):
        status = dict['status']

        self.name = status.get('name')
        self.last_login = datetime_from_iracing_timestamp(status.get('lastLogin'))
        self.last_seen = datetime_from_iracing_timestamp(status.get('lastSeen'))
        self.broadcast = status.get('broadcast')
        self.driver_changes = status.get('driverChanges')
        self.users_max = status.get('maxUsers')
        self.has_grid = status.get('hasGrid')
        self.private_session = status.get('privateSession')
        self.series_id = status.get('seriesId')
        self.reg_open = status.get('regOpen')
        self.spotter_access = status.get('spotterAccess')
        self.season_id = status.get('seasonId')
        self.helmet = Helmet(status['helmet'])
        self.in_grid = status.get('inGrid')
        self.start_time = status.get('startTime')
        self.subsession_status = status.get('subSessionStatus')
        self.track_id = status.get('trackId')
        self.session_status = status.get('sessionStatus')
        self.session_type_id = status.get('sessionTypeId')
        self.cat_id = status.get('catId')
        self.event_type_id = status.get('eventTypeId')
        self.private_session_id = status.get('privateSessionId')
        self.cust_id = status.get('custid')
        self.user_role = status.get('userRole')
