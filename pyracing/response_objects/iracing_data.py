from pyracing.helpers import parse_encode, datetime_from_iracing_timestamp


# Common denominator for Car attributes across all data.
class Car:
    def __init__(self, data):
        self.id = data['id']
        self.name = parse_encode(data['name'])


# Common denominator for CarClass attributes across all data.
class CarClass:
    def __init__(self, data):
        self.cust_id = data['custid']
        self.id = data['id']
        self.name_lower = parse_encode(data['lowername'])
        self.name = parse_encode(data['name'])
        self.rel_speed = data['relspeed']  # Speed ranking to other classes
        self.name_short = parse_encode(data['shortname'])
        # Creating subclass from nested list
        self.cars = [Car(x) for x in data['carsinclass']]


# I believe this maps what I would call a series, but
# iRacing calls this a season, so I want to be consistent
class Season:
    def __init__(self, data):
        self.active = data.get('active')
        self.cat_id = data.get('catid')
        self.category = data.get('category')
        self.date_end = datetime_from_iracing_timestamp(data.get('end'))
        self.date_start = datetime_from_iracing_timestamp(data.get('start'))
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
            self.id = data.get('id')
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
            self.name = parse_encode(data['name'])
            self.name_lower = parse_encode(data['lowername'])
            self.pkg_id = data['pkgid']
            self.sku = data['sku']

    class SeasonCarClass(CarClass):
        def __init__(self, data):
            super().__init__(data)
            self.tire_sets_dry_max = data['max_dry_tire_sets']


class MemberDivision:
    def __init__(self, data):
        self.division = data['division']
        self.division_projected = data['isProjected']


class Helmet:
    def __init__(self, data):
        self.c3 = data.get('c3')
        self.ll = data.get('ll')
        self.hp = data.get('hp')
        self.ht = data.get('ht')
        self.c1 = data.get('c1')
        self.ft = data.get('ft')
        self.c2 = data.get('c2')


class DriverStatus:
    def __init__(self, data):
        self.broadcast = data.get('broadcast')
        self.driver_changes = data.get('driverChanges')
        self.last_login = datetime_from_iracing_timestamp(
            data.get('lastLogin'))
        self.users_max = data.get('maxUsers')
        self.track_id = data.get('trackId')
        self.session_status = data.get('sessionStatus')
        self.session_type_id = data.get('sessionTypeId')
        self.private_session = data.get('privateSession')
        self.series_id = data.get('seriesId')
        self.reg_open = data.get('regOpen')
        self.cat_id = data.get('catId')
        self.event_type_id = data.get('eventTypeId')
        self.spotter_access = data.get('spotterAccess')
        self.last_seen = datetime_from_iracing_timestamp(
            data.get('lastSeen'))
        self.season_id = data.get('seasonId')
        self.helmet = Helmet(data['helmet'])
        self.private_session_id = data.get('privateSessionId')
        self.cust_id = data.get('custid')
        self.name = parse_encode(data.get('name'))
        self.trusted_as_spotter = data.get('trustedAsSpotter')
        self.start_time = data.get('startTime')
        self.user_role = data.get('userRole')
        self.subsession_status = data.get('subSessionStatus')
