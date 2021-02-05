#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:40:30 2021

@author: rop
"""

'''
Powerful digit counts


Problem 63

The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 
9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

# project euler: https://projecteuler.net
# problem 63: powerful digit counts


from time import time
    

def range_ndigits(n):
    lo = 10 ** (n-1)
    hi = 10 ** n - 1
    return lo, hi


def solution():
    n = 1
    cnt = 0
    while True:
        cnt_n = 0
        lo, hi = range_ndigits(n)
        x = 1
        while True:
            x_n = x ** n
            # print(n, x_n)
            if x_n in range(lo, hi+1):
                cnt_n += 1
            if x_n > hi:
                break
            x += 1
        print(n, cnt_n)
        if cnt_n == 0:
            break
        cnt += cnt_n
        n += 1
    return cnt


def report():
    print((f'there are {solution()} n-digit positive integers which are also '
           'nth power'))


def main():
    tic = time()
    

    # projecteuler number:
    report()
    # 49
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()