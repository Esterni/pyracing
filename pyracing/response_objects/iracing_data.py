from ..constants import parse_iracing_string


# I believe this maps what I would call a series, but
# iRacing calls this a season, so I want to be consistent
class Season:
    def __init__(self, data):
        self.serieslicgroupid = data.get('serieslicgroupid')
        self.year = data.get('year')
        self.start = data.get('start')
        self.active = data.get('active')
        self.islite = data.get('islite')
        self.seriesid = data.get('seriesid')
        self.licenseEligible = data.get('licenseEligible')
        self.catid = data.get('catid')
        self.seasonid = data.get('seasonid')
        self.seriesshortname = data.get('seriesshortname')
        self.end = data.get('end')
        self.category = data.get('category')
        self.raceweek = data.get('raceweek')
        self.quarter = data.get('quarter')

        class CarClass:
            def __init__(self, data):
                self.relspeed = data['relspeed']
                self.lowername = data['lowername']
                self.custid = data['custid']
                self.name = data['name']
                self.max_dry_tire_sets = data['max_dry_tire_sets']
                self.id = data['id']
                self.shortname = data['shortname']

                class Cars:
                    def __init__(self, data):
                        self.name = data['name']
                        self.id = data['id']

                self.carsinclass = [Cars(x) for x in data.get('carsinclass', [])]

        class Tracks:
            def __init__(self, data):
                self.lowername = data['lowername']
                self.name = data['name']
                self.id = data['id']
                self.pkgid = data['pkgid']
                self.priority = data['priority']
                self.raceweek = data['raceweek']
                self.config = data['config']
                self.timeOfDay = data['timeOfDay']

        # Yes, there is both a list of "carclasses" with a list of "cars" AND
        # a list "cars" but they each have different values...
        class Cars:
            def __init__(self, data):
                self.lowername = data['lowername']
                self.name = data['name']
                self.id = data['id']
                self.pkgid = data['pkgid']
                self.sku = data['sku']

        self.carclasses = [CarClass(x) for x in data.get('carclasses', [])]
        self.tracks = [Tracks(x) for x in data.get('tracks', [])]
        self.cars = [Cars(x) for x in data.get('cars', [])]


class CarClass:
    def __init__(self, dict):
        self.rel_speed = dict['relspeed']  # Speed ranking to other classes
        self.lower_name = dict['lowername']
        self.custid = dict['custid']
        self.class_full_name = dict['name']
        self.class_id = dict['id']
        self.class_shortname = dict['shortname']

        class Cars:
            def __init__(self, dict):
                self.car_name = dict['name']
                self.car_id = dict['id']

        self.cars = [Cars(x) for x in dict['carsinclass']]


# Useful for personal_bests(). Need to know CarIDs to query.
class CarsDriven:
    def __init__(self, car_list):
        self.list_of_cars = car_list


class MemberDivision:
    def __init__(self, dict):
        self.division = dict['division']
        self.projected_division = dict['isProjected']


class MemberSubID:
    def __init__(self, value):
        self.sub_id = value


class SeasonFromSession:
    def __init__(self, value):
        self.seasonID = int(value)


class AllSubSessions:
    def __init__(self, dict):
        self.subsession_id = dict['subsessionid']
