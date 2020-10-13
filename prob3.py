# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:05:08 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 3: largest prime factor

from time import time


def is_prime(x):
    if x != int(x):
        return False
    if x < 2:
        return False
    if x % 2 == 0:
        return False
    else:
        # range_to_check = list(range(3, int(x/2) + 1))  # list
        # range_to_check = iter(range(3, int(x/2) + 1))  # generator
        range_to_check = iter(range(3, int(x ** 0.5) + 1, 2))  # skip even nums
        for i in range_to_check:
            if x % i == 0:
                return False
        return True

    
def solution(num):
    
    # range_to_check = list(reversed(range(2, int(num/2))))
    # using generator instead of list due to memory error
    range_to_check = iter(reversed(range(2, int(num/2))))
    
    # print(range_to_check)
    # range_to_check.reverse()

    for x in range_to_check:
        if is_prime(x):
            # print(x, 'is prime. checking if it is a factor...')
            if (num % x == 0):
                return x    
            # else:
            #     print(f'{x} is prime but not a factor. checking the next number...')
    return None


def report(num):
    print(f'largest prime factor of {num} is {solution(num)}')
    
    
def main():
    tic = time()
    
    report(13195)
    report(1340257)

    
    # TAKING TOO LONG
    # projecteuler number:
    num = 600851475143 
    # report(num)
    # print(f'largest prime factor of {num} is {solution(num)}')
    
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()