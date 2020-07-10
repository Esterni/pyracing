from datetime import datetime
from ...constants import License


# LicenseClass is in the format `4368` where the first digit represents the license class A through Rookie
# which can be seen in Constants.License and the next 3 digits are the actual rating, so the example
# above would be B class with a 3.68 rating
class LicenseClass:
    def __init__(self, tuple):
        self.datetime = self.datetime_from_iracing_timestamp(tuple[0])
        self.class_number = int(str(tuple[1])[0])
        self.safety_rating = self.get_safety_rating(str(tuple[1]))

    def class_letter(self):
        return License().number_to_string(self.class_number)

    @staticmethod
    def get_safety_rating(string):
        relevant_chars = string[1:]
        return relevant_chars[0] + '.' + relevant_chars[1:]

    # iRacing has all of their timestamps in ms so we need to divide
    @staticmethod
    def datetime_from_iracing_timestamp(timestamp):
        return datetime.utcfromtimestamp(timestamp / 1000)
