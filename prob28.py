# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:28:50 2020

@author: Admin
"""

# project euler: https://projecteuler.net
# problem 28: Number spiral diagonals

from time import time
import numpy as np

#def find_valid_dirs(arr, dim, r, c):
#    # find zeroes (empty space)
#    if c < dim - 1 and arr[r][c+1] == 0:
#        valid_right = True
#    else:
#        valid_right = False
#    if c > 0 and arr[r][c-1] == 0:
#        valid_left = True
#    else:
#        valid_left = False
#    if r < dim - 1 and arr[r+1][c] == 0:
#        valid_down = True
#    else:
#        valid_down = False
#    if r > 0 and arr[r-1][c] == 0:
#        valid_up = True
#    else:
#        valid_up = False
#    
#    valid_dirs = {'r': valid_right, 'l': valid_left, 
#              'u': valid_up, 'd': valid_down}
#    return valid_dirs
#
#
#def make_spiral(dim):
#    if dim % 2 == 0:
#        print('invalid dimension. must be odd')
#        return None
#    arr = np.zeros((dim, dim), dtype=int)
#    nums = range(1, dim * dim + 1)
#    print(nums)
#    # middle cell
#    r = int((dim-1)/2)
#    c = r
#    arr[r][c] = nums[0]
#    
#    valid_dirs = find_valid_dirs(arr, dim, r, c)
#    
#    if valid_dirs['r'] and valid_dirs[']
#    # 3 x 3
#    # r d l l u u r r
#    # 1r 1d 2l 2u 2r
#    # 5 x 5
#    # r d l l uu r r r d d d l l l l u u u u r r r r
#    # 1r 1d 2l 2u 3r 3d 4l 4u 4r
#    # 7 x 7
#    # 0 0 0 0 0 0 0
#    # 0 0 0 0 0 0 0
#    # 0 0 0 0 0 0 0
#    # 0 0 0 0 0 0 0
#    # 0 0 0 0 0 0 0
#    # 0 0 0 0 0 0 0
#    # 0 0 0 0 0 0 0
#    # r d l l u u r r r d d d l l l l u u u u r r r r r d d d d d 
#    
#    move_order = ['r', 'd', 'l', 'u']  # clockwise
#    move = 'r'  # first move is 'right'
#    move_idx = move_order.index(move)
#    c += 1
#    arr[r][c] = nums[1]
#
#    move_idx += 1
#    next_move = move_order[move_idx]
#
#    for num in nums[2:]:
#        # check right, down, left, up
#        if next_move == 'r' and c < arr.shape[1] -1 and arr[r][c+1] == 0:  # right is unfilled
#            c += 1
#            move = 'r'
##            arr[r][c] = num
#        elif next_move == 'd' and r < arr.shape[1] - 1 and arr[r+1][c] == 0:  # down is unfilled
#            r += 1
#            move = 'd'
##            arr[r][c] = num
#        elif next_move == 'l' and c > 0 and arr[r][c-1] == 0:  # left is unfilled
#            c -= 1
#            move = 'l'
#        elif next_move == 'u' and r > 0 and arr[r-1][c] == 0:  # up is unfilled
#            r -= 1
#            move = 'u'
#        arr[r][c] = num
##        print(arr)
#        
#    return arr


def make_spiral(dim):
    if dim % 2 == 0:
        print('invalid dimension. must be odd')
        return None
    arr = np.zeros((dim, dim), dtype=int)
    nums = range(1, dim * dim + 1)
#    print(nums)
    # middle cell
    r = int((dim-1)/2)
    c = r
    arr[r][c] = nums[0]
    '''
    move r until d is open, then
    move d until l is open, then
    move l until u is open, then
    move u until r is open, then loop back
    '''
    moves = ['r', 'd', 'l', 'u']
    num = 2
    move_idx = 0
    while num <= dim * dim:
        if move_idx == len(moves):
            move_idx = 0
#        print('moving', moves[move_idx])
        if move_idx == 0:  # move r
            c += 1
#            print(r, c)
            arr[r][c] = num
            num += 1
#            print(arr)
            if arr[r+1][c] == 0:
                move_idx += 1
            continue
#            else:
#                continue
#            while arr[r+1][c] != 0:  # move r until d is open
#                c += 1
#                print(r, c)
#                arr[r][c] = num
#                num += 1
#                print(arr)
        elif move_idx == 1:  # move d
            r += 1
#            print(r, c)
            arr[r][c] = num
            num += 1
#            print(arr)
            if arr[r][c-1] == 0:
                move_idx += 1
            continue
#            while arr[r][c-1] != 0:  # move d until l is open
#                r += 1
#                arr[r][c] = num
#                num += 1
#                print(arr)
        elif move_idx == 2:  # move l
            c -= 1
            arr[r][c] = num
            num += 1
#            print(arr)
            if arr[r-1][c] == 0:
                move_idx += 1
            continue
#            while arr[r-1][c] != 0:  # move l until u is open
#                c -= 1
#                arr[r][c] = num
#                num += 1
#                print(arr)
        elif move_idx == 3:  # move u
            r -= 1
            arr[r][c] = num
            num += 1
#            print(arr)
            if arr[r][c+1] == 0:
                move_idx += 1
            continue
#            while arr[r][c+1] != 0:  # move u until r is open
#                r -= 1
#                arr[r][c] = num
#                num += 1
#                print(arr)
        
    return arr


def sum_diag(arr):
    dim = arr.shape[0]
    ans = 0
    diag_elems1 = [arr[i][i] for i in range(arr.shape[0])]
    diag_elems2 = [arr[i][dim-i-1] for i in range(dim) if i != dim-i-1]
    ans += sum(diag_elems1)
    ans += sum(diag_elems2)
    return ans
            

def solution(dim):
    arr = make_spiral(dim)
    summ = sum_diag(arr)

    return summ


def report(dim):
    print(f'sum of numbers on the diagonals in a {dim}x{dim} spiral is {solution(dim)}')


def main():
    tic = time()
    
    report(5)
    # 101
    
    # projecteuler number:
    report(1001)
    # 669171001
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()