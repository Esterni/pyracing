# Introduction

This package is an API wrapper/client for retrieving data from iRacing. We use the term "wrapper" loosely because iRacing does not yet have an officially documented API. However, we've done our best to build something that might resemble an actual API.

# Basic Usage
```python
from pyracing import Client

username = 'username'
password = 'password'
ir = Client(username, password)

# Authentication is automated and initiated on first request
seasons = await ir.current_seasons()

for season in seasons:
    if season.series_id == 231:
        for t in tracks:
            print(f'Week {t.race_week} will take place at {t.name} ({t.config})')
```
The result will be
```
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
