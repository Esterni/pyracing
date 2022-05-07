import base64
import hashlib
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


def encode_password(username, password):
    """ Encodes the username/password combination as a Base64 string for
    submission in the password field on iRacing login forms. This is not what
    iRacing stores as the hashed password. It is merely to prevent the plain
    text version of a user's password from being transmitted to iRacing.
    """
    s256Hash = hashlib.sha256((password + username.lower()).encode('utf-8')).digest()
    base64Hash = base64.b64encode(s256Hash).decode('utf-8')

    return base64Hash


def now_five_min_floor():
    """ Takes the current time and rounds down to the nearest five minute mark
    """
    return int(math.floor(time() / 300) * 300) * 1000


def parse_encode(string):
    if not type(string) is str:
        return ''

    return urllib.parse.unquote(string).replace('+', ' ')
