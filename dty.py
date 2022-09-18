#from datetime import datetime
import datetime


def days_in_month(year , month):
    if month == 12:
        return 31
    days =  (datetime.datetime(year , month+1 , 1)- datetime.datetime(year , month , 1)).days
    return days

def is_valid_date(year , month , day):
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:
        if 1<= month <= 12:
            if 1<= day <= days_in_month(year , month):
                return True

    
    return False
   

print(is_valid_date(2022 , 12 ,31))

def days_between(year1 , month1 , day1 , year2 , month2 , day2):
    if is_valid_date(year1 , month1 ,day1) and is_valid_date(year2 , month2 , day2):
        diff = (datetime.datetime(year2 , month2 , day2) - datetime.datetime(year1 , month1 , day1)).days
        if diff>=0:
            return diff
        else:
            return 0
    else:
        return 0
print(days_between(2014, 5, 5, 2014, 5, 6))

def age_in_days(year , month , day):
    if is_valid_date(year , month ,day):
        if datetime.datetime(year , month , day)<datetime.datetime.today():
            diff = (datetime.datetime.today() - datetime.datetime(year , month , day) ).days
            return diff
        else:
            return 0
    else:
        return 0

print(age_in_days(1997,10,30))





# print(days_in_month(2021 , 10))

#print((datetime(2022 , 10 , 1) - datetime(2022 , 9 , 1)).days)

# print(datetime.now())