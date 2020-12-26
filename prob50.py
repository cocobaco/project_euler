#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:37:23 2020

@author: rop
"""

# ONGOING

# project euler: https://projecteuler.net
# problem 50: consecutive prime sum

from time import time

from prob3 import is_prime


def get_next_prime(n):
    if n % 2 == 0:
        candidate = n + 1
    else:
        candidate = n + 2
    while not is_prime(candidate):
        candidate += 2
    return candidate


def get_sum_primes_under(nmax):
    # 2+3, 2+3+5+7, ...
    # 3+5+7, 3+5+7+11+13, ...
    summ_dict = {}
    a = 2
    while a < nmax:
        count = 1
        summ_terms = []
        b = get_next_prime(a)
         
        # first sum
        s = a + b
#        print(s)
        
        while s < nmax:
            count += 1
            if is_prime(s):
                summ_terms.append([s, count])
            b = get_next_prime(b)
            s += b
        summ_dict[a] = summ_terms
        a = get_next_prime(a)
            
    return summ_dict


def solution(nmax):
    summ_dict = get_sum_primes_under(nmax)
    all_terms = [x for x in summ_dict.values() if len(x) > 0]
#    print(all_terms)
    
    max_terms = []
    
    for lol in all_terms:
        counts = [li[1] for li in lol]
        idx_max = counts.index(max(counts))
        max_terms.append(lol[idx_max])
    
    counts = [li[1] for li in max_terms]
    idx_max = counts.index(max(counts))
    max_term = max_terms[idx_max]
        
#    print(max_term)
    
    return max_term[0]


def report(nmax):
    print((f'prime number under {nmax} that is built from most consec sum '
           f'of primes is {solution(nmax)}'))


def main():
    tic = time()
    
    report(100)
    # 41
    
    report(1000)
    # 953
    
    # projecteuler number:
    report(1000000)
    # 997651
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()