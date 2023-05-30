'''
Q10. Of date and days
Write a func that takes 2 args:
date - string representing a date in the form of 'yy-mm-dd'
n - integer
Returns the string representation of date n days before 'date'
E.g. f('16-12-10', 11) should return '16-11-29'

'''

from datetime import datetime, timedelta

def get_date_before(date, n):
    
    date_obj = datetime.strptime(date, '%y-%m-%d')

    date_before = date_obj - timedelta(days=n)

    date_before_str = date_before.strftime('%y-%m-%d')

    return date_before_str

date = input("Enter start date: ")
n = int(input("Number of days: "))
result = get_date_before(date, n)
print(result)  
