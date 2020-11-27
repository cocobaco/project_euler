# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:34:15 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 35: circular primes

from time import time
    
from prob3 import is_prime


def num_to_digitlist(n):
    list_digits = list(map(int, list(str(n))))
    return list_digits


def digitlist_to_num(mylist):
    num = int(''.join(str(n) for n in mylist))
    return num


def rotate_list(mylist, i):
    # 1st rotation: 0 -> len_n - 1, 1 -> 0, 2 -> 1, 3, -> 2
    # 2nd rotation: 0 -> len_n - 2, 1 -> len_n - 1, 2 -> 0, 3 -> 1
    # nth rotation: 0 -> -n, 1 -> -n+1, 2 -> -n+2, 3 -> -n+3
    # first element of nth rotation = nth of original number
    
    len_list = len(mylist)
    newlist = [0] * len_list
    for j in range(len_list):
        newlist[-i+j] = mylist[j]
    return newlist


def check_circular(n):
    if not is_prime(n):
        return False
    
    digitlist = num_to_digitlist(n)
    
    len_n = len(digitlist)
    
    if len_n == 1:
        return is_prime(n)
    
    digitlist = num_to_digitlist(n)
    
    for r in range(1, len_n):
        digitlist_rotated = rotate_list(digitlist, r)
        num_rotated = digitlist_to_num(digitlist_rotated)
        if is_prime(num_rotated):
            continue
        else:
            return False
    
    return True
    

def solution(n_max):
    count = 0
    for n in range(2, n_max):
        if check_circular(n):
            # print(n)
            count += 1
            
    return count


def report(n_max):
    print((f'number of circular primes below {n_max} '
           f'is {solution(n_max)}'))


def main():
    tic = time()
    
    report(100)
    # 13
    
    # projecteuler number:
    report(1000000)
    # 55
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()