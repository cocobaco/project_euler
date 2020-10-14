# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:41:43 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 6: sum square difference

from time import time


def solution(num):
    sum_of_sq = 0
    summ = 0
    for n in range(num+1):
        sum_of_sq += n**2
        summ += n
    sq_of_sum = summ ** 2
    ans = sq_of_sum - sum_of_sq
                    
    return ans
    

def report(num):
    print(f'sum square difference of the first {num} numbers is {solution(num)}')
    
    
def main():
    tic = time()
    
    report(10)
    # 2640
    
    # projecteuler number:
    report(100)
    # 25164150
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()