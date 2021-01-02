#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:09:42 2021

@author: rop
"""

# project euler: https://projecteuler.net
# problem 53: combinatoric selections

from time import time
from math import factorial


def get_n_combi(n, r):
    ans = factorial(n) / (factorial(r) * factorial(n-r))
    return int(ans)


def solution(nmax, val):
    cnt = 0
    for n in range(1, nmax+1):
        for r in range(1, n+1):
            if get_n_combi(n, r) > val:
                cnt += 1
    return cnt


def report(nmax, val):
    print((f'values of combination(n,r) for 1<=n<={nmax} greater than {val} '
           f'is {solution(nmax, val)}'))


def main():
    tic = time()

    
    # projecteuler number:
    report(100, 1000000)
    # 4075
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()