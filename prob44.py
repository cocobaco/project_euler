#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:53:31 2020

@author: rop
"""

# project euler: https://projecteuler.net
# problem 44: pentagon numbers

from time import time


def calc_n_pent(n):
    ans = int(n * (3*n - 1)/2)
    return ans


def is_pentagon(num):
    i = 1
    n_pent = calc_n_pent(i)
    
    while num > n_pent:
        i += 1
        n_pent = calc_n_pent(i)
        if n_pent == num:
            return True
        
    return False

    
def solution():
    
    diffs = []
    k = 2
    while len(diffs) == 0:
        # if k % 100 == 0:
        #     print(f'k={k}')
        for j in range(1, k):
            pj, pk = calc_n_pent(j), calc_n_pent(k)
    
            summ = pj + pk
            
            if is_pentagon(summ):
                print(f'sum of p{j} and p{k} is pentagonal')
                diff = abs(pk - pj)
    
                if is_pentagon(diff):
                    print(f'diff of p{j} and p{k} is pentagonal')
                    diffs.append(diff)     
        k += 1
        
    return min(diffs)


def report(num):
    print((f'minimum D is '
           f'is {solution()}'))


def main():
    tic = time()

    # projecteuler number:
    report()
    # 5482660
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()