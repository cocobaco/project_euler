# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:01:26 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 36: double-base palindromes

from time import time
    
from prob4 import reverse_num
from prob35 import digitlist_to_num


def convert_base(num_base10, base_to):
    # find max_pow
    imax = 0
    while base_to ** imax <= num_base10:
        # print(base_to ** imax, num_base10)
        imax += 1
    
    imax -= 1
        
    # print('max power in base {}: {}'.format(base_to, imax))

    new_digitlist = []
    for i in range(imax, -1, -1):
        # print('finding power', imax)
        digit = num_base10 // (base_to ** i)

        if digit != 0:
            num_base10 = num_base10 - (digit) * (base_to ** i)
        
        new_digitlist.append(digit)

    new_num = digitlist_to_num(new_digitlist)

    return new_num


def solution(n_max):
    summ = 0
    palins = []
    
    for num in range(1, n_max):
        # check base-10 palindrome
        if reverse_num(num) == num:
            num_base2 = convert_base(num, 2)
            # check base-2 palindrome
            if reverse_num(num_base2) == num_base2:
                palins.append(num)
                summ += num
    print(palins)
    
    return summ


def report(n_max):
    print((f'sum of numbers below {n_max} that are palindromic in '
           f'base 10 and base 2 is {solution(n_max)}'))


def main():
    tic = time()
    
    report(1000)
    
    # projecteuler number:
    report(1000000)
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()