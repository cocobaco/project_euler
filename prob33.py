# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:42:48 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 33: Digit cancelling fractions

from time import time
import numpy as np


def check_digit_cancel(num, den):
    num_digits = list(map(int, list(str(num))))
    den_digits = list(map(int, list(str(den))))
    
    if (0 in num_digits) or (0 in den_digits):
        return False
    
    if len(set(num_digits)) != len(num_digits):
        return False
    if len(set(den_digits)) != len(den_digits):
        return False
    if (num_digits[0] not in den_digits) and (num_digits[1] not in den_digits):
        return False
    if num_digits[0] == den_digits[0]:
        num_reduced = num_digits[1]
        den_reduced = den_digits[1]
    elif num_digits[0] == den_digits[1]:
        num_reduced = num_digits[1]
        den_reduced = den_digits[0]
    elif num_digits[1] == den_digits[0]:
        num_reduced = num_digits[0]
        den_reduced = den_digits[1]
    elif num_digits[1] == den_digits[1]:
        num_reduced = num_digits[0]
        den_reduced = den_digits[0]
        
    res = num / den
    res_reduced = num_reduced / den_reduced
    
    if res == res_reduced:
        return True
    else:
        return False
    

def solution():
    num_range = range(10, 99)
    # den_range = range(10, 100)
    
    fracs = []
    
    for num in num_range:
        for den in range(num+1, 100):
            if check_digit_cancel(num, den):
                fracs.append([num, den])
    
    prod_num = np.prod([f[0] for f in fracs])
    prod_den = np.prod([f[1] for f in fracs])
    
    print(fracs)
    print(prod_num, '/', prod_den)
    
    if (prod_den % prod_num == 0):
        prod_den = prod_den / prod_num
        prod_num = 1
        
    print(prod_num, '/', prod_den)
    
    return prod_den 


def report(num):
    print(f'value of the denominator = {solution()}')


def main():
    tic = time()
    
    report(10)
    # 23
    
    # projecteuler number:
    report(1000)
    # 233168
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()