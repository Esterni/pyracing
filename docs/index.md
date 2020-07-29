# About

This package is an asynchronous API wrapper that handles everything necessary for retrieving data from iRacing. We use the term "wrapper" loosely because iRacing does not yet have an officially documented API for us to wrap; This is more like "we pieced things together into something that resembles an API wrapper" kind of wrapper.

!!! Info "Note From the Author"
    We understand that many users of this package may be looking at it from more of a hobby perspective and that asynchronous programming can be a little daunting. If you fall into that category, you'll be relieved to know (maybe?) that we've writting this documentation with you in mind. If you have ideas for improvements, please visiting the [contibuting page](contributing.md) to join the discussion. 

    We hope to provide an identical synchronous version in the future, but for now the design choice was made with discord bots in mind. If you'd like more resources on asyncio, we recommend the [overview guide of asyncio from RealPython](https://realpython.com/async-io-python/#the-10000-foot-view-of-async-io).

# Basic Usage

This example will print the season track schedule for the Advanced Mazda series. 

```python
from pyracing.client import Client
import asyncio

username = 'iRacing username'
password = 'iRacing password'

# Authentication is automated and will be initiated on first request
ir = Client(username, password)

# Example async function with hardcoded results
async def main():

    seasons_list = await ir.current_seasons()

    for season in seasons_list:
        if season.season_id == 2846:
            print(f'Schedule for {season.series_name_short}' 
                    f' ({season.season_year} S{season.season_quarter})')
            
            for t in season.tracks:
                print(f'\tWeek {t.race_week} will take place at {t.name} ({t.config})')
                
asyncio.run(main())
```





??? Example "The Result"
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
    list_of_season_objects = await ir.current_seasons()
    ```
    This is the core of retrieving data with pyracing. Here the `current_seasons()` method, with no parameters, returns data for all currently active seasons of iRacing. It returns a list of [Season objects](data-points/current_seasons.md)  
    
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


