from datetime import datetime


class TTRating:
    def __init__(self, tuple):
        self.datetime = self.datetime_from_iracing_timestamp(tuple[0])
        self.value = tuple[1]

    # iRacing for some reason has an extra 3 0s on the end of the timestamps
    @staticmethod
    def datetime_from_iracing_timestamp(timestamp):
        return datetime.utcfromtimestamp(float(str(timestamp)[:-3]))
