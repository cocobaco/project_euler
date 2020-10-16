# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:01:00 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 7: 10001st prime

from time import time
from prob3 import is_prime


def solution(nth):
    i = 0
    num = 1
    while i < nth:
        num += 1
        if is_prime(num):
            # print(num)
            i += 1
    return num
    

def report(nth):
    print(f'the {nth}-th prime number is {solution(nth)}')
    
    
def main():
    tic = time()
    
    report(6)
    # 13
    
    # projecteuler number:
    report(10001)
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()