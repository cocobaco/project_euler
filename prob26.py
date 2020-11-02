# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:41:03 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 26: Reciprocal cycles

# ONGOING

from time import time
    
def solution(n):
    fracs = []
    for d in range(2, n):
        fracs.append(1/d)
        
    return fracs


def report(n):
    print(f'd < {n} for which 1/d gives the longest recurring cycle in its decimal fraction part is solution(n)')


def main():
    tic = time()
    
    report(11)
    # 7
    
    # projecteuler number:
    report(1000)
    # 233168
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()