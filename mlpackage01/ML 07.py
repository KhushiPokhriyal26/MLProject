import datetime

mytime=datetime.datetime.now()

print ("now=", mytime)

print (mytime.year, mytime.month, mytime.day ,mytime.hour, mytime.minute, mytime.second, mytime.microsecond)

print(mytime.strftime("%B"))

print(mytime.strftime("%b"))