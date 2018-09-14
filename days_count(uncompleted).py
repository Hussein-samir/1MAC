# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonthsLeap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    mi = m1-1 #for months value on the list
    days = -1 #shifting days so we dont count the current day a common year from (jan 1 to dec 31) is 364 days
    while(mi < 12):
        if isLeapYear(y1): #leap years calculations go here
            while (d1 <= daysOfMonthsLeap[mi]):
                    days += 1
                    d1 += 1
        else :  #common years calculations go here
            while (d1 <= daysOfMonths[mi]):
                    days += 1
                    d1 += 1
        mi+= 1
        d1 = 1
    days += 1 #to make a common year 365 days

    return days

print daysBetweenDates(2001,12,31,0,0,0)