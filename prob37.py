# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:25:11 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 37: Truncatable primes


from time import time
from prob3 import is_prime
from prob35 import num_to_digitlist, digitlist_to_num


def check_truncatable(num):
    len_num = len(str(num))
    
    if (len_num < 2) or (not is_prime(num)):
        return False
    
    digitlist = num_to_digitlist(num)
    
    trun_left = []
    trun_right = []
        
    for i in range(1, len_num):
        trun_left.append(digitlist_to_num(digitlist[i:]))
        trun_right.append(digitlist_to_num(digitlist[:-i]))
    
    all_truns = set(trun_left + trun_right)
    print('all truns:', all_truns)
    
    for n in all_truns:
        if not is_prime(n):
            return False
    
    return True

  
def solution(n_primes):
    count = 0
    n_truncatable = []
    # first 2-digit prime: 11
    x = 11
    while True:
        if check_truncatable(x):
            count += 1
            n_truncatable.append(x)
        if count == n_primes:
            break
        x += 2
    
    print('truncatable primes:', n_truncatable)
    
    return sum(n_truncatable)


def report(n_primes):
    print((f'sum of primes ({n_primes}) that are both truncatable from '
           f'both sides is {solution(n_primes)}'))


def main():
    tic = time()

    # projecteuler number:
    report(11)
    # [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
    # 748317
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()