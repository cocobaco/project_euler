# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:23:49 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 46: Goldbach's other conjecture

from time import time
    
from prob3 import is_prime


def goldbach_check(num):
    '''find whether a, b exist such that num == a + 2 * (b ** 2)'''
    a_min = 3  # smallest odd prime
    b_min = 1  # smallest num to square
    a_max = num - 2 * b_min**2
    b_max = int(((num - a_min)/2) ** 0.5)
    # print(a_min, a_max, b_min, b_max)
    a_range = range(a_min, a_max+1)
    b_range = range(b_min, b_max+1)
    
    for a in a_range:
        if is_prime(a):
            for b in b_range:
                if a + 2 * (b ** 2) == num:
                    return True, a, b 
                
    return False, None, None
    

def solution():
    num = 9  # smallest odd composite number (non-prime numbers)
    
    while True:
        if is_prime(num):
            num += 2
            continue
        else:
            goldbach_true, a, b = goldbach_check(num)
            print(num, goldbach_true, a, b)
            if goldbach_true:
                num += 2
            else:
                break
        
    return num


def report():
    print(('smallest odd composite that cannot be written as '
           f'the sum of a prime and twice a square is {solution()}'))


def main():
    tic = time()
    
    # projecteuler number:
    report()
    # 5777

    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()