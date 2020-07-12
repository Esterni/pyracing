Client()
==========

You can use this class to send requests to iRacing service and get valuable data like stats, race results, driver info, series info, etc. it requires valid login credentials (username and password) to access the service.

# Usage
```py
import pyracing
import pyracing.constants as ct
import asyncio

ir = pyracing.client.Client('username', 'password')
await ir.authenticate()

iRating = await ir.get_irating(ct.Category.road, custid)

current_irating = iRating.current()
```

# Data
## Which function for X data?
Each webpage "section" has an associated URL endpoint that is responsible for returning the data used in that section in (usually) JSON format. Here's a reference table:

|Page Displayed| Data Endpoint Used|
|---|---|
|[Race Guide](https://members.iracing.com/membersite/member/Home.do?page=guide) | race_guide() - /GetRaceGuide |
|   |   |
|   |   |


FILES
=====

- client.py : This is where the main class is defined.
- constants.py : Useful constants used in request fields sent to the service.

REQUIREMENTS
============

Python 3.8+ (with network access)
