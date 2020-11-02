# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:05:21 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 25: 1000-digit Fibonacci number

from time import time


def fibo(n):
    ans = []
    a, b = 1, 1
    for i in range(1, n+1):
        ans.append(a)
        a, b = b, a+b
    return ans


def solution(n):
    num = 1
    fib = fibo(num)
    length = len(str(fib[-1]))
    # print(f'{length} digits')
    while length < n:
        num += 1
        fib = fibo(num)
        length = len(str(fib[-1]))
        # print(f'{length} digits')
    return num


def report(n):
    print(f'index of the first term in the fibonacci seq to contain {n} digits is {solution(n)}.')    

    
def main():
    tic = time()
    
    report(3)
    # 12
    
    # projecteuler number:
    report(1000)
    # 4782
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()