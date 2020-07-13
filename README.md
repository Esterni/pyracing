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
Each webpage has an associated URL endpoint that is responsible for returning JSON data used for that page. The following is a list of iRacing webpages and their associated function.

##

|   Page Displayed                     |   Client.function
|   ---                                |   ---
|   My Series Results (/results.jsp)   |   results()
|   Series Stats (/statsseries.jsp)    |   season_standings()
|   Driver Stats (/DriverLookup.Do)    |   driver_stats()
|   World Records (/worldrecords.jsp)  |   world_records()



FILES
=====

- client.py : This is where the main class is defined.
- constants.py : Useful constants used in request fields sent to the service.

REQUIREMENTS
============

Python 3.8+ (with network access)
