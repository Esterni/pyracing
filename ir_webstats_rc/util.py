import inspect
import json
from urllib.parse import unquote  # python3

from . import decorator

def tofile(data):
    a = open('output.html', 'w')
    a.write(data)
    a.close()


def format_results(results, header):
    newres = []
    for row in results:
        newr = {}
        for k, v in row.items():
            newr[header[k]] = v
        newres.append(newr)
    return newres


def __logged_in(func, *args, **kw):
    args2 = list(args)
    irweb = args2[0]
    if not irweb.logged:
        pprint("Error, client is not logged in to iRacing Platform so\
                operation couldn't be completed.", irweb.verbose)
        return None

    if 'custid' in inspect.getargspec(func).args:
        args2[1] = args2[1] if args2[1] is not None else irweb.custid

    return func(*args2, **kw)


def logged_in(func):
    return decorator.decorator(__logged_in, func)


def pprint(string, v=True):
    if v:
        print(' '.join(str(string).split()))


def parse(data):
    res = ''
    try:
        res = json.loads(data)  # iRacing responses are generally in JSON
    except:
        pass  # TODO raise error?

    return res


def clean(string):
    return unquote(string.replace('+', ' '))
