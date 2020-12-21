# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:43:14 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 49: prime permutations

from time import time
from itertools import permutations

from prob3 import is_prime
from prob35 import num_to_digitlist, digitlist_to_num


def permutes_of_num(num):
    digitlist = num_to_digitlist(num)
    permutes = list(permutations(digitlist))
    permute_nums = [digitlist_to_num(p) for p in permutes]
    return permute_nums


def solution():
    num, nhi = 1489, 9999
    
    while num < nhi:
        if is_prime(num):
            n1 = num
            permutes_n1 = permutes_of_num(n1)
            n2, n3 = n1 + 3330, n1 + 6660
            if (n2 in permutes_n1) and (n3 in permutes_n1):
                if is_prime(n2) and is_prime(n3):
                    ans = int(''.join(map(str, sorted([n1, n2, n3]))))
                    return ans
            # for n2 in [j for j in permutes_n1 if j != n1]:
            #     for n3 in [k for k in permutes_n1 if k != n1 and k != n2]:
            #         if (n2 in permutes_n1) and (n3 in permutes_n1):
            #             if is_prime(n2) and is_prime(n3):
            #                 ans = int(''.join(map(str, sorted([n1, n2, n3]))))
            #                 return ans
        num += 1
        
    return None


def report():
    print((f'the 12-digit number '
           f'is {solution()}'))


def main():
    tic = time()
    

    # projecteuler number:
    report()
    # 296962999629
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()