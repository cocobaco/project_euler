# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:59:40 2020

@author: Admin
"""
# ONGOING

# project euler: https://projecteuler.net
# problem 67: Maximum path sum II

from time import time, process_time

# doesn't work for big triangle. too memory intensive.
# from prob18 import report, arr_from_string
from prob18 import arr_from_string
from prob18 import solution as sol18


def check_triang_value(t, row, col):
    print(t[row][col])
    
    
# This gives wrong answer for Prob 67's 100-row triangle
def solution(triang, verbose=True):
    arr = arr_from_string(triang)
    
    # go from top. go down each possible series and only keep the max sum
    
    n_rows = len(arr)
    
    row_idxs = list(range(n_rows))
    # first series
    series_idxs = [0] * n_rows
    
    # final series
    final_series_idxs = [i for i in range(n_rows)]
    
    # first sum
    series = []
    for s_idx, r_idx in zip(series_idxs, row_idxs):
        series.append(arr[r_idx][s_idx])
    summ = sum(series)
    
    max_series = series
    max_sum = summ

    while series_idxs != final_series_idxs:
        if verbose:
            print('-' * 20)
            print('current series_idxs:', series_idxs)
            print('current series:', series)
#            print(series, '--> sum =', summ)
        new_series_idxs = series_idxs
        idx_to_change = n_rows - 1  # start checking at last index
        idx_to_check = idx_to_change - 1
        # check index to change, starting from the end
        while True:
            if new_series_idxs[idx_to_change] == new_series_idxs[idx_to_check]:
                new_series_idxs[idx_to_change] += 1
                break
            else:
                idx_to_change -= 1
                idx_to_check = idx_to_change - 1
                continue
        if verbose:
            print('index to change:', idx_to_change)
#            print('new_series_idxs:', new_series_idxs)
        series_idxs = new_series_idxs
        
#        for s_idx, r_idx in zip(new_series_idxs, row_idxs):
#            series.append(arr[r_idx][s_idx])

        series = []
        for i, s_idx in enumerate(new_series_idxs):
            series.append(arr[i][s_idx])
            
        # check whether the new value is larger than the old one
        new_val = arr[idx_to_change][new_series_idxs[idx_to_change]]
        old_val = arr[idx_to_change][new_series_idxs[idx_to_change-1]]
        if verbose:
            print('old val: {}, new val: {}'.format(old_val, new_val))
        
        # always sum
#        summ = sum(series)
#        max_sum = max([max_sum, summ])
#        if max_sum == summ:
#            max_series = series
            
        # sum only when new_val > 0
        if new_val <= old_val:
            if verbose:
                print('new value is not larger than old one, no summing necessary')
            continue
        else:
            summ = sum(series)
            max_sum = max([max_sum, summ])  # check if sum is greatest ever
            if max_sum == summ:
                max_series = series
#                if verbose:
#                    print('new max series:', max_series, '--> sum:', max_sum)
               
    if verbose:
        print('max series:', max_series, '--> sum:', max_sum)
    
    return max_sum


# def solution2(triang, verbose=True):
#     # https://radiusofcircle.blogspot.com/2017/01/project-euler-problem-67-solution-with-python.html
#     arr = arr_from_string(triang)
#     if verbose:
#         print(arr)
#     counter = 0
#     for r in range(len(arr)-2, -1, -1):
#         if verbose:
#             print('row:', r)
#             print(arr[r])
#         for c in range(len(arr[r])):
# #            print(c)
#             arr[r][c] = arr[r][c] + max(arr[r+1][c], arr[r+1][c+1])
#             counter += 1
#         arr.pop()
#         if verbose:
#             print('arr after pop:', arr)
#     if verbose:
#         print('counter:', counter)
#     ans = arr[0][0]
#     return ans


def solution3(triang):
    arr = arr_from_string(triang)
    
    for row in range(len(arr)-2, -1, -1):
        for col in range(len(arr[row])):
            arr[row][col] += max(arr[row+1][col], arr[row+1][col+1])
        arr.pop()
    ans = arr[0][0]
    return ans


def report(triang, verbose=False):
    ans = solution(triang, verbose=verbose)
    if verbose:
        print(f'max total of the triangle\n{triang}\nis {ans}')    
    else:
        print(f'max total of the triangle is {ans}') 


def main():
    tic = time()
    
    triang1 = '''3
    7 4
    2 4 6
    8 5 9 3'''
    
    
    nloops = 1000
    print('benchmarking methods ({} loops)'.format(nloops))
    print('using this solution (67):')
    t1 = process_time()
    for _ in range(nloops):
        ans = solution(triang1, verbose=False)
    t2 = process_time()
    print('time (s):', t2 - t1)
    print('ans =', ans)
    
    print('-' * 20)
    print('using solution from prob18:')
    t1 = process_time()
    for _ in range(nloops):
        ans = sol18(triang1, verbose=False)
    t2 = process_time()
    print('time (s):', t2 - t1)
    print('ans =', ans)

    print('-' * 20)
    print('using solution3:')
    t1 = process_time()
    for _ in range(nloops):
        ans = solution3(triang1)
    t2 = process_time()
    print('time (s):', t2 - t1)
    print('ans =', ans)
    
    
    print('-' * 20)
    # projecteuler number:
    file = 'data/p067_triangle.txt'
    
    with open(file, 'r') as myfile:
        # read all lines
        triang2 = myfile.read()
    report(triang2, verbose=False)
    
    # print('-' * 20)
    # print('solution from web:', solution2(triang2, verbose=False))
#    with open(file, 'r') as myfile:
    # read first N lines
#        triang2_list = [next(myfile) for x in range(5)]   
#    triang2 = ''.join(triang2_list)
#    report(triang2, verbose=True)
     
    print('-' * 20)
    print(solution3(triang2))
    
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()