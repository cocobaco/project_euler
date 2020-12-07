# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:46:46 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 38: pandigital multiples


from time import time

from prob32 import is_pandigital
from prob35 import num_to_digitlist


def check_unique(num):
    num_list = num_to_digitlist(num)
    
    if len(num_list) == len(set(num_list)):
        return True
    else:
        False


def concat_products(n_int):
    i = 1
    prod = n_int
    while len(str(prod)) < 9:
        i += 1
        prod_next = n_int * i
        if not check_unique(prod_next):
            return None
        prod = int(str(prod) + str(prod_next))
        if not check_unique(prod):
            return None
        
    if len(str(prod)) == 9:
        return prod
    else:
        return None
    

def solution():
    max_pan = 123456789
    max_int = 9876
    for x in range(1, max_int+1):
        prod = concat_products(x)
        if prod is not None:
            if is_pandigital(prod):
                if prod > max_pan:
                    max_pan = prod
    return max_pan


def report():
    print(('largest 1-9 pandigital 9-digit number that can be formed as '
           f'the concatenated product of an integer with (1,2, .., n) is {solution()}'))


def main():
    tic = time()
    
    # projecteuler number:
    report()
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()