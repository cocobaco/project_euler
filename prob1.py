# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:36:05 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 1: multiples of 3 and 5

from time import time
    
def solution(num):
    summ = 0
    for x in range(3, num):
        if (x % 3)*(x % 5) == 0:
            summ += x
    return summ


def report(num):
    print((f'sum of numbers below {num} that are multiples of 3 or 5 '
           f'is {solution(num)}'))


def main():
    tic = time()
    
    report(10)
    # 23
    
    # projecteuler number:
    report(1000)
    # 233168
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()