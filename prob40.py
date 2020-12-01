# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:06:04 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 40: Champernowne's constant

from time import time


def get_dn(nth):
    num_str = ''
    i = 1
    while len(num_str) < nth:
        # print(i)
        num_str = ''.join([num_str, str(i)])
        i += 1
    
    # print(f'0.{num_str}')
    dn = int(num_str[nth-1])
    
    return dn


def solution():
    nths = [1, 10, 100, 1000, 10000, 100000, 1000000]
    
    prod = 1
    for nth in nths:
        dn = get_dn(nth)
        prod *= dn
        
    return prod


def report():
    print(('the product is '
           f'{solution()}'))


def main():
    tic = time()
    
    # projecteuler number:
    report()
    # 210
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()