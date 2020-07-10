from ...constants import ChartType, Category


class ChartData:
    def __init__(self, category, type, list):
        self.category = category  # oval, road, dirt_road, dirt_oval
        self.type = type  # irating, ttrating, or license_class
        self.list = list  # A list of Iratings, TTRatings, or LicenseClasses

    def current(self):
        return self.list[-1]

    def type_string(self):
        return ChartType.digit_to_string(self.type)

    def category_string(self):
        return Category.digit_to_string(self.category)
