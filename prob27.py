# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:23:05 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 27: quadratic primes


from time import time

from prob3 import is_prime

def quad(n, a, b):
    return n ** 2 + a * n + b


def solution(a_range, b_range):
    max_primes = 0
    a_ans, b_ans = 0, 0
    prod_ab = a_ans * b_ans
    
    for a in a_range:
        for b in b_range:
            n = 0
            prime_count = 0
            while True:
                y = quad(n, a, b)
                if is_prime(y):
                    prime_count += 1
                    n += 1
                else:
                    break
            if prime_count > max_primes:
                max_primes = prime_count
                a_ans, b_ans = a, b
    prod_ab = a_ans * b_ans
    print(f'a={a_ans}, b={b_ans} produce {max_primes} consecutive primes.')
    
    return prod_ab


def report(a_range, b_range):
    print((f'product of coefs a ({a_range}) and b({b_range}) that '
           'produces max number of primes for consecutive n is '
           f'{solution(a_range, b_range)}'))


def main():
    tic = time()
    
    for n in range(0, 39+1):
        y = quad(n, 1, 41)
        print(f'{y} --> prime: {is_prime(y)}')
    
    for n in range(0, 79+1):
        y = quad(n, -79, 1601)
        print(f'{y}. prime: {is_prime(y)}')

    report(range(0, 5), range(30, 50))

    # projecteuler number:
    a_range = range(-999, 1001)
    b_range = range(-999, 1001)
    report(a_range, b_range)
    # a = -61, b = 971 ==> 71 consec primes, a * b = -59231
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()