# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:05:46 2020

@author: PC1
"""
# project euler: https://projecteuler.net
# problem 43: sub-string divisibility

from time import time

from prob35 import digitlist_to_num
from prob41 import permute_n_digits


def check_substring_divis(num):
    num_str = str(num)
    
    divisors = [2, 3, 5, 7, 11, 13, 17]
    
    nums_sub = [int(num_str[i:i+3]) for i in range(1, 8)]
    
    for n, d in zip(nums_sub, divisors):
        # print(n, d, n % d)
        if n % d != 0:
            return False
        
    return True
        

def solution():
    permutes = permute_n_digits(9, nfirst=0)
    
    nums = [digitlist_to_num(p) for p in permutes]
    
    # filter out those starting with 0
    nums = [num for num in nums if len(str(num))==10]
    
    ans = 0
    for num in nums:
        if check_substring_divis(num):
            ans += num
    return ans


def report():
    print(('sum of all 0 to 9 pandigital numbers with sub-string divisiblity '
           f'is {solution()}'))


def main():
    tic = time()
    

    # projecteuler number:
    report()
    # 16695334890
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()