#!/usr/bin/python
""" Example usage of iRWebStats """
from ir_webstats_rc import constants as ct
from ir_webstats_rc.client import iRWebStats
from ir_webstats_rc.util import clean


user = 'your username'  # iRacing username and password
password = 'your password'
irw = iRWebStats()
irw.login(user, password)
if not irw.logged:
    print (
        "Couldn't log in to iRacing Membersite. Please check your credentials")
    exit()

# Cars driven by user
r = irw.cars_driven()  # Returns cars id

print("\n--> 1. Cars driven by custid:%s \n" % (irw.custid))
print("\n".join([irw.CARS[c]['name'] for c in r]))

# Career stats
r = irw.career_stats()
print("\n--> 2. Career stats for custid:%s \n" % (irw.custid))
print(("Starts: %s, Wins: %s, Top 5: %s, Total Laps: %s," +
       " Laps Led: %s") % (r['starts'], r['wins'], r['top5'], r['totalLaps'],
                           r['lapsLed']))

# Driver search
print("\n--> 3. Driver search (Road racers with Average finish from 1 to 3)\n")
drivers, total_drv = irw.driver_search(
    race_type=ct.RACE_TYPE_ROAD, avg_finish=(1, 3), active=True, page=1)

print("Total drivers found: %s. Showing the first %s" % (total_drv,
                                                         len(drivers)))
print("\n".join(["%s - %s: %s" % (i + 1, clean(x['displayname']), x['irating'])
                for i, x in enumerate(drivers)]))
