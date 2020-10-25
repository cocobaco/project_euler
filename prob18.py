# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:27:15 2020

@author: Admin
"""

# ONGOING
# project euler: https://projecteuler.net
# problem 18: Maximum path sum I

from time import time


# Wrong result
#def solution(triangle_str):
#    arr1 = triangle_str.split('\n')
#    arr1_split = [x.split() for x in arr1]
#    arr1_int = [list(map(int, x)) for x in arr1_split]
#    sums = [arr1_int[0][0]]  # first element
#    for row in arr1_int[1:]:
#        print('row:', row)
#        row_sums = []
#        for i, s in enumerate(sums):
#            sums_i = [s + row[i], s + row[i+1]]
#            print(s, '--> sums_i:', sums_i)
#            row_sums.extend(sums_i)
#            print('row_sums:', row_sums)
#        sums = row_sums
#    max_sum = max(sums)
#    
#    return max_sum


def solution(triangle_str):
    '''work from bottom'''
    arr = triangle_str.split('\n')
    arr_split = [x.split() for x in arr]
    arr_int = [list(map(int, x)) for x in arr_split]
    
    bottom_row_idx = len(arr_int) - 1  # index of bottom row
#    bottom_row = arr1_int[-1]
    bottom_row = arr_int[bottom_row_idx]
    print(bottom_row)
    max_sum = 0
    sums = []
    for i, x in enumerate(bottom_row):  # 8, 5, 9, 3
        print(i, x)
        possible_sums_for_x = [x]
        row_idx = bottom_row_idx
        above_row_idx = row_idx - 1
        while above_row_idx >= 0:
            above_row = arr_int[above_row_idx]
            print(above_row)
            if i == 0:
                elems_to_add = [above_row[0]]
            elif i == len(above_row) - 1:
                elems_to_add = [above_row[-1]]
            else:
                elems_to_add = [above_row[i-1], above_row[i]]
            print('elems to add', elems_to_add)
            for elem in elems_to_add:
                sum_x_branch = possible_sums_for_x + elem  
                possible_sums_for_x.append(sum_x_branch)
            row_idx -= 1                              
            above_row_idx -= 1

        sums.append(sum_x_branch)                
            
#    print(sums)
#    sums = [arr1_int[0][0]]  # first element
#    for row in arr1_int[1:]:
#        print('row:', row)
#        row_sums = []
#        for i, s in enumerate(sums):
#            sums_i = [s + row[i], s + row[i+1]]
#            print(s, '--> sums_i:', sums_i)
#            row_sums.extend(sums_i)
#            print('row_sums:', row_sums)
#        sums = row_sums
#    max_sum = max(sums)
    
    return max_sum

def report(triangle_str):
    print(f'max total of the triangle\n{triangle_str}\nis {solution(triangle_str)}')    

    
def main():
    tic = time()
    
    triang1 = '''3
    7 4
    2 4 6
    8 5 9 3'''
    

    report(triang1)
    # 23
    
    # projecteuler number:
    triang2 = '''75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
#    report(triang2)
    
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()