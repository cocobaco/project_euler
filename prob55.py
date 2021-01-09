#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:16:05 2021

@author: rop
"""

# project euler: https://projecteuler.net
# problem 55: Lychrel numbers

from time import time
    
from prob4 import is_palindrom, reverse_num


def is_lychrel(n):
    for i in range(49):
        n_rev = reverse_num(n)
        # if len(str(n_rev)) != len(str(n)):
        #     continue
        added = n + n_rev
        if is_palindrom(added):
            return False
        n = added
    return True
    
    
def solution(num):
    summ = 0
    # for n in range(num):
    # use known lychrel number:
    for n in range(196, num):
        if is_lychrel(n):
            summ += 1
    return summ


def report(num):
    print(f'under {num}, there are {solution(num)} Lychrel numbers')


def main():
    tic = time()
    
    
    # projecteuler number:
    report(10000)
    # 249
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()