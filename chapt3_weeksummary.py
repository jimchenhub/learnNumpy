import numpy as np
from datetime import datetime

def datestr2num(s):
    return datetime.strptime(s, "%Y/%m/%d").date().weekday()

dates, open, high, low, close = np.loadtxt('data.csv', delimiter=',', usecols=(1, 3, 4, 5, 6), converters={1: datestr2num}, unpack=True)
close = close[:16]
dates = dates[:16]

first_monday = np.ravel(np.where(dates == 0))[0]
print "The first Monday day index is ", first_monday

last_friday = np.ravel(np.where(dates == 4))[-1]
print "The last Friday day index is ", last_friday
