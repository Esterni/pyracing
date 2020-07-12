Client()
==========

You can use this class to send requests to iRacing service and get valuable data like stats, race results, driver info, series info, etc. it requires valid login credentials (username and password) to access the service.

USAGE
=====

    from client import Client
    irw = Client()
    irw.login('username', 'password')
    print (irw.cars_driven())  # cars driven by user

Check examples.py for more examples

FILES
=====

- client.py : This is where the main class is defined.
- constants.py : Useful constants used in request fields sent to the service.

REQUIREMENTS
============

Python 3.8+ (with network access)
