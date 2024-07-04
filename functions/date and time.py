#1- PROGRAM TO GET DATE:
from datetime import date
import day
from datetime import timedelta

print(day.findaay('12 3 2024'))
today=date.today()
print("today is :",today)

yesterday = today - timedelta(days=1)
print("yesterday was :",yesterday)

daybeforeyesterday=today - timedelta(days=2)
print("day before yesterday is:",daybeforeyesterday)


#2- PROGRAM TO GET THE CURRENT TIME USING FUNCTIONS:
import time 

curr_time = time.localtime() 
curr_clock = time.strftime("%H:%M:%S", curr_time) 

print(curr_clock) 

#3- PROGRAM TO GET CURRENT DATE AND TIME:
from datetime import datetime
curtime=datetime.now()
print( "THE CURRENT DATE AND TIME IS:",curtime)

#4- PROGRAM TO FORMATE THE DATE AND TIME WITH AM/PM:

from datetime import datetime as dt
date=dt.now()
formate_date=date.strftime("%B %d, %Y")
print(formate_date)

time=dt.now()
formate_time= time.strftime("%I:%M:%S %p")
timezonee=date.tzname()
print(formate_time) 
print("Timezone:",timezonee)