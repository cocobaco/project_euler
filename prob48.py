# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:36:32 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 48: Self powers

from time import time
from math import factorial

tic = time()

    
def solution(num):
    summ = 0
    for n in range(1, num+1):
        summ += n ** n
    summ_str = str(summ)
    ans = summ_str[-10:]
    return ans


def report(num):
    print(f'last ten digits in the series {num}^{num}! is {solution(num)}')


report(10)
# 0405071317

# projecteuler number:
report(1000)
# 9110846700

toc = time()

print('time used:', toc - tic)