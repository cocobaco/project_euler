# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:55:57 2020

@author: Admin
"""

# ONGOING

# project euler: https://projecteuler.net
# problem 19: Counting Sundays

from time import time


def solution():
    days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days_month_normal = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
                         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days_month_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 
                         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    # find day of 1 Jan 1901
    # days_in_1900 = 365
    day_idx = 0  # Mon on 1 Jan 1900
    for i, month in enumerate(months):
        print(month)
        for date in range(1, days_month_normal[i+1]+1):
            if day_idx == 6:
#                print(f'{date} {month}: {days_of_week[day_idx]}')
                day_idx = 0
            else:
                day_idx += 1
            if (date == 31) and (month == 'Dec'):
                print('-' * 20)
                print(f'{date} {month}: {days_of_week[day_idx]}')
                
                
    # date range: 1 Jan 1901 to 31 Dec 2000
    sundays_on_1st = 0
    day_idx = 1  # Tue on 1 Jan 1901
    for year in range(1901, 2001):
        if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
            days_month = days_month_leap
        else:
            days_month = days_month_normal
    #    print(f'{year} has {sum(days_month.values())} days')
        for i, month in enumerate(months):
#            print(month)
            for date in range(1, days_month[i+1]+1):
                if (date == 1) and (day_idx == 6):
                    print(f'{date} {month} {year}: {days_of_week[day_idx]}')
                    sundays_on_1st += 1
                    day_idx = 0
                elif day_idx == 6:
                    day_idx = 0
                else:
                    day_idx += 1
    return sundays_on_1st


def report():
    print(solution(), 'Sundays on 1st of month during 20th century')
   

def main():
    tic = time()
    
    # projecteuler number:
    report()
    # 171
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()