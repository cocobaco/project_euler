#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:24:41 2021

@author: rop
"""

# project euler: https://projecteuler.net
# problem 57: Square root convergents


from time import time
    

def get_numer_denom(n):
    if n == 1:
        denom = 2
        numer = denom + 1
    elif n > 1:
        denom = 2
        numer = 2 * denom + 1
        for i in range(n, 0, -1):
            if i > 1:
                numer, denom = denom + 2 * numer, numer
            elif i == 1:
                numer, denom = denom + numer, numer
                
    return numer, denom
    

def solution(num):
    count = 0
    for n in range(1, num+1):
        numer, denom = get_numer_denom(n)
        if len(str(numer)) > len(str(denom)):
            count += 1
            
    return count


def report(num):
    print((f'In the first {num} expansions, there are '
           f'{solution(num)} fractions containing a numerator with more '
           'digits than the denominator.'))


def main():
    tic = time()
    
    report(10)
    # 1
    
    # projecteuler number:
    report(1000)
    # 153
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()