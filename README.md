# About

This package is an API wrapper/client for retrieving data from iRacing. We use the term "wrapper" loosely because iRacing does not yet have an officially documented API. However, we've done our best to build something that might resemble an actual API.

Please feel free to open issues, offer suggestions, or fork and submit a pull request to help polish things up here. We only ask that you be willing to openly discuss things in a respectful manner. If you'd like to chat in Discord, I can be reached in the [iRacing Open Wheel Discord](https://discord.gg/UwnhM7w) (nearing 1000 members!). My username is Jacob Anderson7#4903. I'd be happy to hear from those interested in this project and if enough people reach out I'll make a section just for this project.

# Usage
```py
import pyracing
import pyracing.constants as ct

# Storing in system env is another option and use os.getenv() to retrieve them. 
username = 'username'
password = 'password'

ir = pyracing.client.Client('username', 'password')  # or any other method
await ir.authenticate()

iRating = await ir.get_irating(ct.Category.road, custid)

current_irating = iRating.current()
```


# Which function for X data?

Each webpage has an associated URL endpoint that is responsible for returning JSON data to be used in that page. While all pages utilize these endpoints for the data displayed, not all JSON endpoints have a webpage they are used in.

**Note**: While some of these endpoints reveal data that can't be found anywhere else, others return such little information that you might wonder why they exist at all. Our goal is only to provide easy access to them, not make sense of them.

Table of contents:

- [Historical Data](#historical-data)
  - [Results & Stats](#results--stats)
  - [Career Stats (Driver's Profile Page)](#career-stats-drivers-profile-page)
- [Single Session](#single-session)
- [Upcoming Sessions & Events](#upcoming-sessions--events)
- [Misc Functions](#misc-functions)

## Historical Data
This section covers all of the historical information in more of a summary format. To be more specific, these are for returning **lists** of series, races, drivers, and lap times rather than the in-depth information about each one. (Each one is associated with a page on the iRacing membersite)

## Results & Stats
|   iRacing                            |    pyracing
|   ---                                |    ---
|   My Series Results (/results.jsp)   |    results()
|   Series Stats (/statsseries.jsp)    |    season_standings()
|   Driver Stats (/DriverLookup.Do)    |    driver_stats()
|   World Records (/worldrecords.jsp)  |    world_records()

### Career Stats (Driver's Profile Page)


|   iRacing                            |   pyracing
|   ---                                |   ---
|   ChartData for iRating              |   get_irating()
|   ChartData for ttRating             |   get_ttrating()
|   ChartData for License Class        |   get_license_class()
|   Career Stats Table                 |   career_stats()
|   Yearly Stats Table                 |   yearly_stats()
|   Last 10 Races Table                |   last_race_stats()
|   Last 3 Series Table                |   last_series()
|   Personal Bests                     |   personal_bests()


---
---
### Data for Single Sessions
These endpoints do not share such a clear association with specific areas on the iRacing site, but we will try to describe where they are used.

#### all_subsessions()
Used in an event's "result" page to give you a dropdown to view the other splits of a session.

This function will return the other SubSessionIds of the other splits, if any exist.

#### sub_sess_results()

Returns detailed and comprehensive attributes of a session. This function will be of great interest as it is the only known location for the following when looking at a session after it has concluded:

- Number of corners in the track
- Specific CPI index for each driver
- Starting temperature for session
- Wind speed for session

#### current_seasons()
Returns all information about every series (yes, series). Each series has a base "series_id", but in order to differentiate a series from one season to the next, they each use a unique identifier, "season_id".

The default of this function is to return information for only the currently active series. Use the provided kwargs to toggle access to the historical "season_id"s.

#### hosted_results()

#### race_laps_all()

#### race_laps_driver()

-

#### next_event()

#### total_registered_all()

#### active_op_counts()

#### race_guide()


## Misc Functions

#### member_division()

#### member_sub_id_from_session()

#### season_for_session()

#### member_cars_driven()

#### car_class_by_id()


FILES
=====

- client.py : This is where the main class is defined.
- constants.py : Useful constants used in request fields sent to the service.

REQUIREMENTS
============

Python 3.8+ (with network access)
