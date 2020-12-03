# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:14:34 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 39: integer right triangles

from time import time


def check_right_tri(a, b, c):
    if c ** 2 == (a ** 2) + (b ** 2):
        return True
    else:
        return False


def solution(p_max):
    # min length: 1
    # max c: p - 2
    # a: 1, 2, ..., p-c-1
    # b = p - c - a
    
    max_n = 0
    p_ans = 0
    
    for p in range(4, p_max+1):
        if p % 50 == 0:
            print(f'p = {p}')
        combis = []
        for c in range(p-2, int((p + 2)/3), -1):
            for a in range(1, p-c-2):
                if a >= c:
                    continue
                b = p - c - a
#                print(p, a, b, c)
                if b >= c:
#                    print('b >= c')
                    continue
                is_right_tri = check_right_tri(a, b, c)
                if is_right_tri:
#                    print('a, b, c (right tri):', a, b, c, is_right_tri)
                    if set([a, b, c]) not in combis:
                        combis.append(set([a, b, c]))                     
        n = len(combis)
#        print(n)
        if n > max_n:
            max_n = n
            p_ans = p
            print(f'answer updated: p={p_ans}, max_n={max_n}')

    return max_n, p_ans


def report(p_max):
    max_n, p_ans = solution(p_max)
    print((f'value of p <= {p_max} which gives max number of solutions '
           f'is {p_ans} ({max_n} solutions)'))


def main():
    tic = time()

    # projecteuler number:
    report(1000)
    # p=840, n=8
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()