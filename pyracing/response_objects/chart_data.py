from ..constants import ChartType, Category, License
from ..helpers import datetime_from_iracing_timestamp


class ChartData:
    def __init__(self, category, type, list):
        self.category = category  # oval, road, dirt_road, dirt_oval
        self.list = list  # A list of Iratings, TTRatings, or LicenseClasses
        self.type = type  # irating, ttrating, or license_class

    def current(self):
        return self.list[-1]

    def type_string(self):
        return ChartType(self.type).name

    def category_string(self):
        return Category(self.category).name


class IRating:
    def __init__(self, tuple):
        self.datetime = datetime_from_iracing_timestamp(tuple[0])
        self.value = tuple[1]


class TTRating:
    def __init__(self, tuple):
        self.datetime = datetime_from_iracing_timestamp(tuple[0])
        self.value = tuple[1]


# LicenseClass is in the format `4368` where the first digit represents the
# license class A through Rookie which can be seen in Constants.
# License and the next 3 digits are the actual rating, so the example '4368'
# would be B class with a 3.68 rating
class LicenseClass:
    def __init__(self, tuple):
        self.class_number = int(str(tuple[1])[0])
        self.datetime = datetime_from_iracing_timestamp(tuple[0])
        self.license_level = self.get_safety_rating(str(tuple[1]))

    def class_letter(self):
        return License(self.class_number).name

    @staticmethod
    def get_safety_rating(string):
        relevant_chars = string[1:]
        return relevant_chars[0] + '.' + relevant_chars[1:]
