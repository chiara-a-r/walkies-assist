#python script to get weather info and create 'Walk Archie' events on google calendar

import datetime
from astral import LocationInfo
from astral.sun import sun
city = LocationInfo("Sydney", "Australia", "Australia/Sydney", -33.87, 151.21)

s = sun(city.observer, date=datetime.date(2021, 1, 29), tzinfo = city.timezone)
print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
))