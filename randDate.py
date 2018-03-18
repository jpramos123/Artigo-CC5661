import random
import time
from datetime   import timedelta, date, datetime

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDateHot():
    return strTimeProp("2018-01-01", "2018-06-30", '%Y-%m-%d', random.random())
    
def randomDateCold():
	return strTimeProp("2018-07-01", "2018-12-31", '%Y-%m-%d', random.random())

def randomDateP(start, delta):
	start_date = datetime.strptime(start, '%Y-%m-%d').date()
	return strTimeProp(start, str(start_date + timedelta(days=delta)), '%Y-%m-%d', random.random())
