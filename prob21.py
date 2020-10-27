# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:43:48 2020

@author: Admin
"""

# project euler: https://projecteuler.net
# problem 21: Amicable numbers

from time import time
from math import sqrt

def sumdiv(n):
    divs = [1]
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divs.extend([i, n // i])
#    print(divs)
    ans = sum(divs)
    return ans

    
def solution(num):
    ans = 0
    pairs = []
    for a in range(1, num):
        b = sumdiv(a)
        if (b > 1) and (sumdiv(b) == a) and (a != b):
            if {a, b} not in pairs:
                pairs.append({a,b})
    print(pairs)
    ans = sum([sum(pair) for pair in pairs])
    return ans


def report(num):
    print(f'sum of all amicable numbers under {num} is {solution(num)}.')    

    
def main():
    tic = time()
    
#    report(15)
#    # 26
#    
    # projecteuler number:
    report(10000)
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()