from datetime import date, timedelta

def meetup_day(year, month, weekday, option):

    weekdays = {'Monday' : 0, 'Tuesday' : 1, 'Wednesday' : 2, 'Thursday' : 3, 'Friday' : 4, 'Saturday' : 5, 'Sunday' : 6}
    daynum = weekdays[weekday]

    if option == '1st':
        return meetup_day_count(year, month, daynum, 1)
    
    if option == '2nd':
        return meetup_day_count(year, month, daynum, 2)

    if option == '3rd':
        return meetup_day_count(year, month, daynum, 3)

    if option == '4th':
        return meetup_day_count(year, month, daynum, 4)

    if option == 'last':
        return meetup_day_last(year, month, daynum)

    if option == 'teenth':
        return meetup_day_teenth(year, month, daynum)

    raise Exception('Invalid option')


def meetup_day_count(year, month, daynum, count):
    firstday = date(year, month, 1)
    dayoffset = daynum - firstday.weekday()
    if dayoffset < 0:
        offset = timedelta(count*7 + dayoffset)
    else:
        offset = timedelta((count-1)*7 + dayoffset)
    return firstday + offset

def meetup_day_last(year, month, daynum):
    lastday = date(year + month/12, (month+1) % 12, 1) - timedelta(1)
    dayoffset = daynum - lastday.weekday()
    if dayoffset <= 0:
        offset = timedelta(dayoffset)
    else:
        offset = timedelta(dayoffset - 7)
    return lastday + offset

def meetup_day_teenth(year, month, daynum):
    thirteenth = date(year, month, 13)
    dayoffset = daynum - thirteenth.weekday()
    if dayoffset >= 0:
        offset = timedelta(dayoffset)
    else:
        offset = timedelta(dayoffset + 7)
    return thirteenth + offset
