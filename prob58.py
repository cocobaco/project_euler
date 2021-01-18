# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:00:52 2021

@author: rop
"""

from time import time
import numpy as np

from prob3 import is_prime


# -------------------------------------------------------------------------- #
# BRUTE FORCE takes too long

def next_loc(direction, i, j):
    if direction == 'r':
        i_new = i
        j_new = j + 1
    elif direction == 'u':
        i_new = i - 1
        j_new = j
    elif direction == 'l':
        i_new = i
        j_new = j - 1
    elif direction == 'd':
        i_new = i + 1
        j_new = j        
        
    return i_new, j_new


def is_empty_square(a, i, j, direc):
    i_new, j_new = next_loc(direc, i, j)
    if a[i_new][j_new] == 0:
        return True
    else:
        return False
    

def make_spiral(d):
    
    diag_coords1 = [(i,i) for i in range(d)]
    diag_coords2 = [(i,d-i-1) for i in range(d)]
    diag_coords = set(diag_coords1 + diag_coords2)
    
    nums = range(1, d**2+1)
    
    a = np.zeros(shape=(d, d), dtype=int)
    center = int((d-1)/2)
    
    # direction order: ruld
    dir_order = list('ruld')
    
    dir_idx = 0
    curr_dir = dir_order[dir_idx]
    
    # sniff zeros (available space): if can't go, keep same direction
    # example: can't go r, go d... can't go u, go r
    
    # initiate first few steps
    i, j = center, center
    n_idx = 0
    
    a[i][j] = nums[n_idx]
    n_idx += 1
    
    # go right
    # check right square
    # if is_empty_square(a, i, j, curr_dir):
    #     i, j = next_loc(curr_dir, i, j)
    # else:
    #     i
    i, j = next_loc(curr_dir, i, j)
    a[i][j] = nums[n_idx]
    n_idx += 1
    
    cnt = 0
    
    # advance direction
    while n_idx < len(nums):
        if dir_idx == len(dir_order) - 1:
            next_dir = dir_order[0]
        else:
            next_dir = dir_order[dir_idx + 1]

        if is_empty_square(a, i, j, next_dir):
            # update direction
            curr_dir = next_dir
            dir_idx = dir_order.index(curr_dir)
            # print(dir_idx)
    
        # print('moving', curr_dir)
        i, j = next_loc(curr_dir, i, j)
        a[i][j] = nums[n_idx]
        n_idx += 1
        
        # print(a)
    
        if (i,j) in diag_coords:
            if is_prime(a[i][j]):
                cnt += 1
        
        pct = 100 * cnt / len(diag_coords)
    
    return a, cnt, pct
    

def count_diag_primes(a):
    if a.shape[0] != a.shape[1]:
        print('not a square array')
        return None
    d = a.shape[0]
    diag_coords1 = [(i,i) for i in range(d)]
    diag_coords2 = [(i,d-i-1) for i in range(d)]
    diag_coords = set(diag_coords1 + diag_coords2)
    # print(diag_coords)
    cnt = 0
    for (i,j) in diag_coords:
        if is_prime(a[i][j]):
            cnt += 1
    
    pct = 100 * cnt / len(diag_coords)
            
    return cnt, pct
        
    
# def solution(thres, verbose=True):
    
#     # d = 7
#     d = 3035
    
#     while True:
#         a, cnt, pct = make_spiral(d)
        
#         # cnt, pct = count_diag_primes(a)
        
#         if verbose:
#             print(f'side length: {d}, diag primes: {cnt} ({pct:.2f}%)')
#         if pct < thres:
#             return d
#         else:
#             d += 2

# -------------------------------------------------------------------------- #
    
          
# using observation

def solution(thres, verbose=True):
    
    '''
    3x3
    1 3 5 7 9
    total diag elems = 5
    
    5x5
    13 17 21 25
    (9 + (5-1)), +4, +4, +4
    total diag elems = 5 + 4
    
    7x7
    31 37 43 49
    (25 + (7-1)), +6, +6, +6
    total diag elems = 5 + (4*2)
    '''
    
    d = 3
    num_diags = [1, 3, 5, 7, 9]
    last_num = num_diags[-1]
    num_diags_count = len(num_diags)
    
    primes = [n for n in num_diags if is_prime(n)]
    primes_count = len(primes)
    
    # float decimal problem
    # pct = 100 * primes_count / num_diags_count
    
    # while pct >= thres:
    while True:
        d += 2
        step = d - 1
        
        new_diag_num_first = last_num + step
        
        num_diags_new = [new_diag_num_first, 
                         new_diag_num_first + step, 
                         new_diag_num_first + 2*step, 
                         new_diag_num_first + 3*step]
        last_num = num_diags_new[-1]
        
        new_primes = [n for n in num_diags_new if is_prime(n)]
        # new_primes_count = len(new_primes)
        
        primes_count += len(new_primes)
        num_diags_count += 4
        
        # pct = 100. * primes_count / num_diags_count
    
        if verbose:
            # print(f'side length: {d}, diag primes: {pct:.3f}%')
            print(f'side length: {d}, {primes_count} primes (out of {num_diags_count})')
        
        # if pct < 10.0:
        # if int(str(pct).split('.')[0]) == 9:
        if primes_count * thres < num_diags_count:
            return d
        
    # return d
            
            

def report(thres, verbose=False):
    print(('side length of the square spiral for which ratio of primes along '
           f'both diagonals first falls below {thres}% is {solution(thres, verbose=verbose)}'))


def main():
    tic = time()
    
    
    # projecteuler number:
    report(10, verbose=False)
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()
    