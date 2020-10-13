# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:48:26 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 2: even fibonacci numbers

from time import time


# TOO MEMORY INTENSIVE
# def solution(num):
#     ans = 0
#     fibo = [1]
#     for n in range(1, num+1):
#         prev_num = fibo[n-1]
#         try:
#             prev_2num = fibo[n-2]
#         except:
#             prev_2num = 1
#         fibo_term = prev_num + prev_2num
#         fibo.append(fibo_term)
#         if fibo_term % 2 == 0:
#             ans += fibo_term
#     # print(fibo)
#     return ans


def solution(num):
    ans = 0
    fibo_term = 1
    fibo_prev = 1
    while fibo_term <= num:
        # print(fibo_term, fibo_prev)
        if fibo_term % 2 == 0:
            ans += fibo_term
        fibo_term, fibo_prev = fibo_term + fibo_prev, fibo_term
    return ans


def report(num):
    print(f'sum of even numbers in the Fibonacci sequence up to {num} is {solution(num)}')
    
    
def main():
    tic = time()
    
    report(10)

    # projecteuler number:
    report(4000000)
    # 4613732
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()