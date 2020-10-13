# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:30:51 2020

@author: Admin
"""

# project euler: https://projecteuler.net
# problem 10: summation of primes

from time import time

from prob3 import is_prime


tic = time()

    
def solution(num):
    summ = 0
    for x in range(2, num):
        if is_prime(x):
            print(x)
            summ += x
    return summ


def report(num):
    print(f'sum of primes below {num} is {solution(num)}')


report(10)
report(50)

# projecteuler number:
report(int(2e6))
# 142913828922

toc = time()

print('time used:', toc - tic)