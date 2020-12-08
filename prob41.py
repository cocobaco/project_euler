# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 11:28:07 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 41: pandigital prime


from time import time
from itertools import permutations

from prob3 import is_prime
from prob32 import is_pandigital
from prob35 import num_to_digitlist, digitlist_to_num


def check_one_to_n(num):
    '''check whether num makes use of digits 1 to n exactly once'''
    num_list = num_to_digitlist(num)
    len_list = len(num_list)
    if set(num_list) == set(range(1, len_list+1)):
        return True
    else:
        return False


def permute_n_digits(n):
    permutes = permutations(range(1, n+1), n)
    return list(permutes)    



def solution():
    # n = 2143
    # n_max = 987654321
    # for x in range(n, n_max+1, 2):
        # if is_prime(x):
        #         if check_one_to_n(x):
        #             if is_pandigital(x):
        #                 print(x, 'is pandigital prime')
        #                 break
    # x = 987654321
    # while True:
    #     # print('checking', x)
    #     if check_one_to_n(x):
    #         print(x, 'is made of 1-n digits, each digit exactly once')
    #         if is_prime(x):
    #             print(x, 'is prime')
    #             if is_pandigital(x):
    #                 print(x, 'is pandigital prime')
    #                 break
    #     x -= 2
    
    max_panprime = 2143
    
    for n in range(9, 1, -1):
        permutes = permute_n_digits(n)
        nums = [digitlist_to_num(p) for p in permutes]
        for num in nums:
            if check_one_to_n(num):
                if is_prime(num) and is_pandigital(num):
                    if num > max_panprime:
                        max_panprime = num
        if max_panprime > 2143:
            break
            
    return max_panprime


def report():
    print(('largest n-digit pandigital prime is '
           f'{solution()}'))


def main():
    tic = time()
    
    # projecteuler number:
    report()
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()