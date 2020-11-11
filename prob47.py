# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:37:27 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 47: Distinct primes factors

from time import time

from prob3 import is_prime


def prime_factors(n):
    pf = []
    x = 2
    while x * x <= n:
        if n % x == 0:
            pf.append(x)
            n = n // x  
        else:
            x += 1
        # print(f'x={x}, n={n}')     
    if n > 1:
        pf.append(n)     
    return pf
        

def solution(n):
    nconsec = 0
    num = 2
    while nconsec < n:
        # prev_dpfs = set(prime_factors(num))
        
        dpfs = set(prime_factors(num))
        # print(num, dpfs, len(dpfs))
        # print(num, dpfs, prev_dpfs)
        if len(dpfs) != n:
            nconsec = 0
        else:
            nconsec += 1
        num += 1

            
    return num - n        
   


def report(n):
    print((f'first of the {n} consecutive numbers to have {n} distinct prime '
           f'factors each is {solution(n)}'))


def main():
    tic = time()
    
    report(2)
    # 14

    report(3)
    # 644
    
    # projecteuler number:
    report(4)
    # 134043
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()