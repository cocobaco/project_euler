# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:32:48 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 20: Factorial digit sum

from time import time
from math import factorial

tic = time()

    
def solution(num):
    fact = factorial(num)
    fact_chars = list(str(fact))
    digits = list(map(int, fact_chars))
    ans = sum(digits)
    return ans


def report(num):
    print(f'sum of digits in the number {num}! is {solution(num)}')


report(10)
# 27

# projecteuler number:
report(100)
# 648

toc = time()

print('time used:', toc - tic)