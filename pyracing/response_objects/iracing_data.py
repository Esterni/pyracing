from ..constants import parse_iracing_string


# I believe this maps what I would call a series, but iRacing calls this a season, so I want to be consistent
class Season:
    def __init__(self, dict):
        self.season_id = dict['seasonid']
        self.cat_id = dict['catid']
        self.series_short_name = parse_iracing_string((dict['seriesshortname']))
        self.year = self.value_or_none(dict, 'year')
        self.quarter = self.value_or_none(dict, 'quarter')
        self.series_id = self.value_or_none(dict, 'seriesid')
        self.active = self.value_or_none(dict, 'active')
        self.license_eligible = self.value_or_none(dict, 'licenseeligible')
        self.is_lite = self.value_or_none(dict, 'islite')
        self.car_classes = self.value_or_none(dict, 'carclasses')
        self.tracks = self.value_or_none(dict, 'tracks')
        self.end = self.value_or_none(dict, 'end')
        self.cars = self.value_or_none(dict, 'cars')
        self.race_week = self.value_or_none(dict, 'raceweek')
        self.category = self.value_or_none(dict, 'category')
        self.series_lic_group_id = self.value_or_none(dict, 'serieslicgroupid')
        self.car_id = self.value_or_none(dict, 'carid')

    @staticmethod
    def value_or_none(dict, field_name):
        if field_name in dict:
            return dict[field_name]
        else:
            return None


class CarClass:
    def __init__(self, dict):
        self.rel_speed = dict['relspeed']  # Speed ranking to other classes
        self.lower_name = dict['lowername']
        self.custid = dict['custid']
        self.class_full_name = dict['name']

        # Inject into subclass CarsInClass?
        self.carsinclass = dict['carsinclass']
        self.class_id = dict['id']
        self.class_shortname = dict['shortname']

    class CarsInClass:
        def __init__(self, dict):
            self.car_name = dict['name']
            self.car_id = dict['id']


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
        self.seasonID = value


class AllSubSessions:
    def __init__(self, dict):
        self.subsession_id = dict['subsessionid']
