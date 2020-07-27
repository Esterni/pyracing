# About

This package is an API wrapper/client for retrieving data from iRacing. We use the term "wrapper" loosely because iRacing does not yet have an officially documented API. However, we've done our best to build something that might resemble an actual API.

# Asynchronous Programming
If you're new to asynchronous programming; Welcome to the club! Seriously. As the author of this package, I learned async just for this. It might involve a few days of some intense brain fuzz, but it's absolutely within reason to learn, even for a hobby project. We've made our examples with you in mind. If you need more resources on the topic, we recommend this [overview guide from RealPython](https://realpython.com/async-io-python/#the-10000-foot-view-of-async-io). Also see the [contibuting page](contributing.md) for contacting us; we're happy to help!

!!! Info 
    Shoutout to contributor/maintainer, **Xander Riga**, for the initial design and implementation of the overall async funtionality for this project. 


# Basic Usage

??? Warning "Running an async function"
    === "Normal Execution"
        With a non-Windows OS, running the following example is very straightforward.
        ```python
        asyncio.run(main())
        ```
        The `asyncio.run()` function handles everything related to the event loop and will close itself after execution.
    === "Windows Execution"
        Due to an issue with how HTTP requests are handling within the event loop on windows, we can't use the default loop provided by windows and we must create our own.
        ```python
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        fut = loop.create_task(main())
        loop.run_until_complete(fut)
        ```
        - `loop = asyncio.new_event_loop()` Creates a new event_loop and sets it to `loop`  
        - `asyncio.set_event_loop(loop)` Sets event loop for asyncio to use for the duration of the script.   
        - `fut = loop.create_task(main())` Creates a 'future' object (The task to run `main()`)  
        - `loop.run_until_complete(fut)` Finally says "run the event loop until `fut` has completed.  

## Example code
```python
from pyracing import Client
import asyncio

username = 'iRacing username'
password = 'iRacing password'

# Authentication is automated and will be initiated on first request
ir = Client(username, password)

# Example async function with hardcoded results
async def main():

    list_of_season_objects = await ir.current_seasons()

    for season in list_of_season_objects:
        
        if season.series_id == 231:
            print(f'\nSchedule for {season.series_name_short}' 
                    f' ({season.season_year} S{season.season_quarter})')
            
            for t in season.tracks:
                print(f'    Week {t.race_week} will take place at {t.name} ({t.config})')
```

??? Info "Click Here For Code Breakdown"
    ```python
    from pyracing import Client
    ```
    The `Client` Class contains all that is necessary to begin accessing data from iRacing.
    ```python
    username = 'iRacing username'
    password = 'iRacing password'

    ir = Client(username, password)
    ```
    We create an instance of Client and assign it to `ir`.
    ```python
    # Authentication is automated and initiated on first request
    list_of_season_objects = await ir.current_seasons()
    ```
    This is the core of this package. The `current_seasons()` method, with no paramaters, will return all data for active seasons. Data is returned as a list of `season` objects; 1 object for each season returned. ([ see all attributes here](All-Data/current_seasons.md))  
    
    ??? Note "Using await"
        Because this is asynchronous code, you *must* `await` the method. It tells the event_loop to leave the function and come back to it later while it sends the request. For more on asynchronous programming, we recommend the [Complete Walkthrough from realpython.com](https://realpython.com/async-io-python/#where-does-async-io-fit-in)
    
    ```python
    for season in list_of_season_objects:
        if season.series_id == 231:
            print(f'\nSchedule for {season.series_name_short}' # Line continuation
                    f' ({season.season_year} S{season.season_quarter})')
    ```
    Now that we have all of the data, the rest is figuring out what you want to do with it. In our example, we go through each season object and find the one that matches series_id of 231. Once we've found it, we print out the `series_name_short` for the series along with the season_year and season_quarter. This gives us the first line in the example below.

    ```python
    for t in season.tracks:
                print(f'    Week {t.race_week} will take place at {t.name} ({t.config})')
    ```
    In this case, our `season` object has a child object; `season.tracks` contains a list of the `track` objects with it's own set of attributes. Here, for each track that exists in `season.tracks` we nicely format a response that gives us the attributes we want for each track. Each track has a `t.race_week` for when that track will be active in the season, `t.name` for the full name of the track, and `t.config` for the configuration that will be used. 



The result will be
```
Schedule for Advanced Mazda MX-5 Cup Series (2020 S3)
    Week 0 will take place at Road Atlanta (Full Course)
    Week 1 will take place at Circuit Gilles Villeneuve ()
    Week 2 will take place at Road America (Full Course)
    Week 3 will take place at Lime Rock Park (Grand Prix)
    Week 4 will take place at Barber Motorsports Park (Full Course)
    Week 5 will take place at Suzuka International Racing Course (Grand Prix)
    Week 6 will take place at Nürburgring Combined (Gesamtstrecke Short w/out Arena)
    Week 7 will take place at Brands Hatch Circuit (Grand Prix)
    Week 8 will take place at Autodromo Internazionale Enzo e Dino Ferrari (Grand Prix)
    Week 9 will take place at Watkins Glen International (Boot)
    Week 10 will take place at Sebring International Raceway (International)
    Week 11 will take place at Autodromo Nazionale Monza (Grand Prix)
    Week 12 will take place at Mount Panorama Circuit ()
```
