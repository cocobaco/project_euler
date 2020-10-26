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
from prob18 import report, arr_from_string

    
def solution(triang):
    arr = arr_from_string(triang)
    
    # go from top. go down each possible series and only keep the max sum
    
    n_rows = len(arr)
    
    row_idxs = list(range(n_rows))
    # first series
    series_idxs = [0] * n_rows
    
    # final series
    final_series_idxs = [i for i in range(n_rows)]
    
    max_sum = 0
    series = []
    while series != final_series_idxs:
        new_series_idxs = series_idxs
        
        for s_idx, r_idx in zip(series_idxs, row_idxs):
            series.append(arr[r_idx][s_idx])
        summ = sum(series)
        print(summ)
        max_sum = max([max_sum, summ])
        series_idxs = new_series_idxs
        
    
    max_sum = sum(first_series)
    print('first sum:')
    summ = arr[0][0]  # top of pyramid
    print('top element:', summ)
    for row_idx in range(1, n_rows):
        current_row = arr[row_idx]
        print('current row:', current_row)
        # n_elems = row_idx + 1
        idx_add = 0
        summ += arr[row_idx][idx_add]
        print(summ)
    # print(summ)
    max_sum = max([max_sum, summ])
    print('max_sum:', max_sum)
        

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
    with open(file, 'r') as myfile:
        triang2_list = [next(myfile) for x in range(20)]   
    triang2 = ''.join(triang2_list)
    
    report(triang2, verbose=False)
     
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()