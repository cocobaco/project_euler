# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:14:06 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 16: Power digit sum

from time import time

def solution(n):
    temp = 2 ** n
    nums = [int(x) for x in list(str(temp))]
    summ = sum(nums)
    return summ


def report(n):
    print(f'sum of the digits of 2**{n} is {solution(n)}.')    

    
def main():
    tic = time()
    
    report(15)
    # 26
    
    # projecteuler number:
    report(1000)
    
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()