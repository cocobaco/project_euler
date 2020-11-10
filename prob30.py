# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:45:39 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 30: Digit fifth powers

from time import time
    
def is_sum_digits(num, n_pow):
    num_str = str(num)
    num_str_list = list(num_str)
    
    digits = list(map(int, num_str_list))
    summ = 0
    for d in digits:
        summ += d ** n_pow
        
    if num == summ:
        return True
    else:
        return False


def solution(n_pow):
    summ = 0
    for x in range(10, 10**(n_pow+1)):
        if is_sum_digits(x, n_pow):
            print(x)
            summ += x
    return summ


def report(n_pow):
    print(('sum of numbers that can be written as the sum of the '
           f'{n_pow}-th powers of their digits is {solution(n_pow)}'))


def main():
    tic = time()
    
    report(4)
    # 19316
    
    # projecteuler number:
    report(5)
    # 443839
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()