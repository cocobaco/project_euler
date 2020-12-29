# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:56:10 2020

@author: PC1
"""

# ONGOING


# project euler: https://projecteuler.net
# problem 52: permuted multiples

from time import time
from collections import Counter

from prob35 import num_to_digitlist


def get_2x_to_6x(x):
    mults =[1, 2, 3, 4, 5, 6]
    ans = [m * x for m in mults]
    return ans


def check_permute(list1):
    for i, num1 in enumerate(list1[:-1]):
        for num2 in list1[i+1:]:
            num1_count = Counter(num_to_digitlist(num1))
            num2_count = Counter(num_to_digitlist(num2))
            if num1_count != num2_count:
                return False
    return True



def solution():
    x = 1
    while True:
        list1 = get_2x_to_6x(x)
        if check_permute(list1):
            return x
        x += 1



def report():
    print(
            ('the smallest positive integer, x, such that 2x, 3x, 4x, 5x, '
            f'and 6x, contain the same digits is {solution()}')
        )


def main():
    tic = time()
    
    # projecteuler number:
    report()
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()