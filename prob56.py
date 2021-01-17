# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:18:02 2021

@author: rop
"""

# project euler: https://projecteuler.net
# problem 56: powerful digit sum

from time import time

from prob35 import num_to_digitlist


def sum_digits(n):
    digitlist = num_to_digitlist(n)
    ans = sum(digitlist)
    return ans


def solution(num):
    s_ans, a_ans, b_ans = 0, 0, 0
    
    for a in range(2, num):
        for b in range(2, num):
            x = a ** b
            s = sum_digits(x)
            if s > s_ans:
                s_ans, a_ans, b_ans = s, a, b
    return s_ans, a_ans, b_ans


def report(num):
    s, a, b = solution(num)
    print((f'maximum digit sum of a^b for a, b < {num} '
           f'is {s} (a={a}, b={b})'))


def main():
    tic = time()
    

    # projecteuler number:
    report(100)
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()