import calendar as c
def findaay(date):
    day,month,year=(int(i) for i in date.split(' '))
    daynumber= c.weekday(year,month,day)
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    return days[daynumber]
date=input("enter a date:")
print(findaay(date))
