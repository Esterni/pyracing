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
