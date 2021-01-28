#python script to get weather info and create 'Walk Archie' events on google calendar

#TODO - 6pm earliest walkies in afternoon, otherwise morning walk - 7-8am

from datetime import datetime, timedelta
import datetime
from astral import LocationInfo
from astral.sun import sun
city = LocationInfo("Sydney", "Australia", "Australia/Sydney", -33.87, 151.21)

s = sun(city.observer, date=datetime.date(2021, 1, 29), tzinfo = city.timezone)

walk_start = s["sunset"] - timedelta(hours=1)
walk_end = s["sunset"]

print("Start walkies: " + str(walk_start))
print("End walkies: " + str(walk_end))
#TODO - round to nearest 15 mins

