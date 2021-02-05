#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:54:58 2021

@author: rop
"""


# project euler: https://projecteuler.net
# problem 62: cubic permutations


from time import time
from itertools import permutations
from math import isclose


def check_cube(n):
    root3 = n ** (1/3)
    if isclose(root3, round(root3)):
        return True
    return False


def num_from_lst(lst):
    n = int(''.join(str(x) for x in lst))
    return n

    
def permutes(x):
    '''get set of permutations of number x'''
    digits = list(map(int, list(str(x))))
    permutes1 = permutations(digits, len(digits))
    permutes2 = set([])
    for p in permutes1:
        # if p[0] == 0:
        #     continue
        n2 = num_from_lst(p)
        if (n2 not in permutes2):
            permutes2.add(n2)  
    return permutes2


def count_cubes_perm(x):
    cnt = 0
    for p in permutes(x):
        if check_cube(p):
            cnt += 1
    return cnt


def solution(num):
    i = 344
    
    while True:
        x = i ** 3
        cnt = count_cubes_perm(x)
        if cnt > 1:
            print(f'{i}, {x}: {cnt} cubes')
        if cnt == num:
            return x
        i += 1
    

def solution2(num):
    # https://radiusofcircle.blogspot.com/2016/11/project-euler-problem-62-solution-with.html
    i = 1
    cubes = []
    while True:
        digits = sorted(list(str(i**3)))
        cubes.append(digits)
        if cubes.count(digits) == num:
            lowest_cube = cubes.index(digits) ** 3
            return lowest_cube
        i += 1
        

def report(num):
    print((f'smallest cube for which exactly {num} permutations of its digits are cube '
           # f'is {solution(num)}'))
            f'is {solution2(num)}'))


def main():
    tic = time()
    
    # report(3)
    # 41063625
    
    # projecteuler number:
    report(5)
    # 1006012008  # incorrect
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()