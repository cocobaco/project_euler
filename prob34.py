# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:18:40 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 34: digit factorials

from time import time
from math import factorial
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('default')


def sum_factorials(num):
    num_digits = list(map(int, list(str(num))))
    sum_fact = sum(factorial(n) for n in num_digits)
    return sum_fact
    
    
def solution(num_max, plot=True):
    
    x = np.arange(10, num_max + 1)
    y = [sum_factorials(xi) for xi in x]
    
    if plot:
        plt.figure()
        plt.scatter(x, y, marker='.', s=10)
        plt.plot([0, max(y)], [0, max(y)], '--r', label='x=y')
        plt.xlabel('num')
        plt.ylabel('sum factorial of digits')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend()
        
        plt.show()

    nums_equal = x[x==y]
    
#    for num in range(10, num_max+1):
#        sum_fact = sum_factorials(num)
##        print(num, sum_fact)
#        if num == sum_fact:
#            nums_equal.append(num)
    print(nums_equal)
    ans = sum(nums_equal)
    return ans


def plot_sum_fact(num_max):
    x = np.arange(10, num_max)
    y = [sum_factorials(xi) for xi in x]
    
    plt.figure()
    plt.scatter(x, y, marker='.', s=10)
    plt.plot([0, max(y)], [0, max(y)], '--r', label='x=y')
    plt.xlabel('num')
    plt.ylabel('sum factorial of digits')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    
    plt.show()


def report(num_max, plot=True):
    print((f'sum of all numbers (up to {num_max}) which are equal to the sum '
           f'of the factorial of their digits is {solution(num_max, plot=plot)}'))


def main():
    tic = time()
    
    # projecteuler number:
    report(100000, plot=True)
    # 40730
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()