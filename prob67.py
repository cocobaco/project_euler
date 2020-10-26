# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:59:40 2020

@author: Admin
"""
# ONGOING

# project euler: https://projecteuler.net
# problem 67: Maximum path sum II

from time import time

# doesn't work for big triangle. too memory intensive.
# from prob18 import report, arr_from_string
from prob18 import arr_from_string

    
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
        
    max_sum = summ

    while series_idxs != final_series_idxs:
        if verbose:
            print('current series_idxs', series_idxs)
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
            print('new_series_idxs:', new_series_idxs)
        series = []
        for s_idx, r_idx in zip(new_series_idxs, row_idxs):
            series.append(arr[r_idx][s_idx])
        summ = sum(series)
        if verbose:
            print(series, '--> sum =', summ)
        max_sum = max([max_sum, summ])
        # set up next series
        # new_series_idxs = series_idxs   
        series_idxs = new_series_idxs
    
    return max_sum


def report(triang, verbose=False):
    ans = solution(triang, verbose=verbose)
    print(f'max total of the triangle\n{triang}\nis {ans}')    


def main():
    tic = time()
    
    triang1 = '''3
    7 4
    2 4 6
    8 5 9 3'''
    
    report(triang1, verbose=True)
    # 23
    
    # projecteuler number:
    file = 'data/p067_triangle.txt'
    with open(file, 'r') as myfile:
        triang2 = myfile.read()
    
    # read first N lines
    # with open(file, 'r') as myfile:
    #     triang2_list = [next(myfile) for x in range(50)]   
    # triang2 = ''.join(triang2_list)
    
    report(triang2, verbose=False)
     
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()