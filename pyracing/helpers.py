import math
import urllib.parse
from time import time
from datetime import datetime


# iRacing has all of their timestamps in ms so we need to divide
def datetime_from_iracing_timestamp(timestamp):
    try:
        return datetime.utcfromtimestamp(int(timestamp) / 1000)
    except Exception:
        return None


def now_five_min_floor():
    """ Takes the current time and rounds down to the nearest five minute mark
    """
    return int(math.floor(time() / 300) * 300) * 1000


def parse_encode(string):
    if not type(string) is str:
        return ''

    return urllib.parse.unquote(string).replace('+', ' ')
