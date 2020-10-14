# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 16:12:11 2020

@author: Admin
"""

# project euler: https://projecteuler.net
# problem 4: largest palindrome product

from time import time


def reverse_num(num):
    num_str = str(num)
    num_str_rev = num_str[-1::-1]
    num_rev = int(num_str_rev)
    return num_rev


def solution(n):
    min_num = 10 ** (n-1)
    max_num = int(10**n - 1)
    max_prod, num1_max, num2_max = 0, min_num, min_num
    
    range_check = range(min_num, max_num+1)
    
    for num1 in range_check:
        for num2 in range_check:
            prod = num1 * num2
            if reverse_num(prod) == prod:  # palindrome check
                if prod > max_prod:
                    max_prod = prod  # update max_prod
                    num1_max = num1
                    num2_max = num2
                    
    return max_prod, num1_max, num2_max
    
'''
99 * 99
98 * 99
98 * 98
97 * 98
'''

def report(n):
    prod, num1, num2 = solution(n)
    print(f'largest palindrome made from two {n}-digit numbers is {prod} ({num1} x {num2})')
    
    
def main():
    tic = time()
    
    report(2)
    # 9009
    
    # projecteuler number:
    report(3)
    # 906609
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()