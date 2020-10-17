# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:50:14 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 9: special pythagorean triplet

from time import time

def solution(num):
    
    for a in range(1, num-2):
        for b in range(1, num-2):
            if b != a:
                c = 1000 - a - b
                if c not in [a, b]:
                    if a**2 + b**2 == c**2:
                        ans = [a, b, c]
                        break
    prod = ans[0] * ans[1] * ans[2]
    return prod, ans


def report(num):
    print(f'product of pythagorean triplet whose sum is {num} is {solution(num)[0]}')
    print(f'triplet: {solution(num)[1]}')
    
    
def main():
    tic = time()
    
    # projecteuler number:
    report(1000)
    # 31875000
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()