# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:26:55 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 5: smallest multiple

from time import time


tic = time()

    
def solution(n1, n2):
    ans = n2 * (n2-1)
    while True:
        # print(ans)
        for n in range(n1, n2+1):
            if ans % n != 0:
                ans += 1
                break
            if n == n2:
                return ans


def report(n1, n2):
    print(f'smallest multiple divisible by all numbers from {n1} to {n2} is {solution(n1, n2)}')


report(1, 10)

# projecteuler number:
report(1, 20)
# 232792560

toc = time()

print('time used:', toc - tic)