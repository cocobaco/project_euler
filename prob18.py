# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:27:15 2020

@author: Admin
"""

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


#def solution(triangle_str):
#    '''work from bottom'''
#    arr = triangle_str.split('\n')
#    arr_split = [x.split() for x in arr]
#    arr_int = [list(map(int, x)) for x in arr_split]
#    
#    bottom_row_idx = len(arr_int) - 1  # index of bottom row
##    bottom_row = arr1_int[-1]
#    bottom_row = arr_int[bottom_row_idx]
#    print(bottom_row)
#    max_sum = 0
#    sums = []
#    for i, x in enumerate(bottom_row):  # 8, 5, 9, 3
#        print(i, x)
#        possible_sums_for_x = [x]
#        row_idx = bottom_row_idx
#        above_row_idx = row_idx - 1
#        while above_row_idx >= 0:
#            above_row = arr_int[above_row_idx]
#            print(above_row)
#            if i == 0:
#                elems_to_add = [above_row[0]]
#            elif i == len(above_row) - 1:
#                elems_to_add = [above_row[-1]]
#            else:
#                elems_to_add = [above_row[i-1], above_row[i]]
#            print('elems to add', elems_to_add)
#            for elem in elems_to_add:
#                sum_x_branch = possible_sums_for_x + elem  
#                possible_sums_for_x.append(sum_x_branch)
#            row_idx -= 1                              
#            above_row_idx -= 1
#
#        sums.append(sum_x_branch)                
#            
##    print(sums)
##    sums = [arr1_int[0][0]]  # first element
##    for row in arr1_int[1:]:
##        print('row:', row)
##        row_sums = []
##        for i, s in enumerate(sums):
##            sums_i = [s + row[i], s + row[i+1]]
##            print(s, '--> sums_i:', sums_i)
##            row_sums.extend(sums_i)
##            print('row_sums:', row_sums)
##        sums = row_sums
##    max_sum = max(sums)
#    
#    return max_sum


def arr_from_string(triang):
    # arr = triang.strip('\n')
    arr = triang.strip().split('\n')
    arr_split = [x.split() for x in arr]
    arr_int = [list(map(int, x)) for x in arr_split]   
    return arr_int


# def solution(triang):
#     arr = triang.split('\n')
#     arr_split = [x.split() for x in arr]
#     arr_int = [list(map(int, x)) for x in arr_split]    

#     '''work from bottom
#     [00]    
#     [10, 11]
#     [20, 21, 22]
#     ==> 4 sums: [[20, 10, 00], [21, 10, 00], [21, 11, 00], [22, 11, 00]]
#     '''

#     current_row_idx = len(arr_int) - 1  # index of bottom row
# #    bottom_row = arr1_int[-1]
#     current_row = arr_int[current_row_idx]
#     print(current_row)
#     bottom_row = current_row
#     prev_row_idx = current_row_idx - 1
#     prev_row = arr_int[prev_row_idx]
#     print(prev_row)
    
#     for i, x in enumerate(bottom_row):
#         x_series = [[x]]
#         # for each bottom row number, find all possible series
#         while prev_row_idx >= 0:
#             for i, x in enumerate(current_row):
#                 print(i, x)
#                 x_series = [[x]]
#                 print()
#                 # for each x, construct all possible series            
#                 new_x_series = []
#                 prev_row = arr_int[prev_row_idx]
#                 possible_add_idxs = [idx for idx in [i-1, i] if idx >= 0]
#                 print('possible_add_idxs:', possible_add_idxs)
#                 possible_add_elems = [prev_row[idx] for idx in possible_add_idxs]
#                 print(possible_add_elems)
#                 for elem in possible_add_elems:
#                     for serie in x_series:
#                         serie.append(elem)
#                         new_x_series.append(serie)
#                 x_series = new_x_series
#                 prev_row_idx -= 1
#                 current_row_idx -= 1
#                 prev_row = arr_int[prev_row_idx]
#                 current_row = arr_int[current_row_idx]
#             print(x_series)


def solution(triang, verbose=True):
    # 1. build array out of multi-line string
    arr = arr_from_string(triang)
    if verbose:
        print(arr)
    nrows = len(arr)
    
    # 2. loop through each item on the bottom row
    bottom_row = arr[-1]
    
    max_sum = 0
    
    # all_series = []
    # # initiate series
    # for x in bottom_row:
    #     all_series.append([x])
    # print(all_series)

    # with last element index tag
    all_series_tagged = []
    for i, x in enumerate(bottom_row):
        all_series_tagged.append([[x], i])
    if verbose:
        print(all_series_tagged)
    
    # initial max sum
    # sums = [sum(series) for series in all_series]
    # max_sum = max(sums)
    # print('max sum:', max_sum)
    
    sums_tagged = [sum(series[0]) for series in all_series_tagged]
    max_sum = max(sums_tagged)
    if verbose:
        print('max sum:', max_sum)
    
    prev_row_idx = nrows - 2
    
    while prev_row_idx >= 0:
        # all_series_updated = []
        all_series_updated_tagged = []
        prev_row = arr[prev_row_idx]
        # for i, series in enumerate(all_series):
        #     print(i, series)
        #     print('prev_row_idx:', prev_row_idx)
        #     print('prev row:', prev_row)
        # # 3. find adjacent items on the previous row
        #     adjacent_idxs = [idx for idx in [i-1, i] if (0 <= idx <= prev_row_idx)]
        #     print('adjacent idxs:', adjacent_idxs)
        #     adjacent_elems = [prev_row[idx] for idx in adjacent_idxs]
        #     print(f'adjacent elems to {series[-1]}: {adjacent_elems}')
        #     series_updated = [series + [elem] for elem in adjacent_elems]
        #     print(series_updated)
        #     for su in series_updated:
        #         all_series_updated.append(su)
        for series, i in all_series_tagged:
            if verbose:
                print(series, i)
            adjacent_idxs = [idx for idx in [i-1, i] if (0 <= idx <= prev_row_idx)]
            if verbose:
                print('adjacent idxs:', adjacent_idxs)
            series_updated_tagged = []
            for idx in adjacent_idxs:
                series_updated_tagged.append([series + [prev_row[idx]], idx])
            for su in series_updated_tagged:
                all_series_updated_tagged.append(su)
        # print('all series')
        
        # all_series = all_series_updated
        all_series_tagged = all_series_updated_tagged
        if verbose:
            print('-' * 20)
            # print('all series:', all_series)
            print('all series_tagged:', all_series_tagged)
        prev_row_idx -= 1
    if verbose:
        print('total possible series:', len(all_series_tagged))
    sums_tagged = [sum(series[0]) for series in all_series_tagged]
    max_sum = max(sums_tagged)
    # print('max sum:', max_sum)
    
    # 4. build up series [series1, series2, ...]
    
    # 5. for each series, find adjacent items on the previous row
    
    # 6. updated series [series1.1, series1.2, series 2.1, ...]
    
    # 7. finish when the top row is reached
    
    # 8. find the sum of each series, and store the maximum sum for that bottom element

    return max_sum


def report(triang, verbose=False):
    ans = solution(triang, verbose=verbose)
    print(f'max total of the triangle\n{triang}\nis {ans}')    

    
def main():
    tic = time()
    
#    triang0 = '''3
#    7 4
#    2 4 6'''
#    
#    report(triang0, verbose=True)
    
    
    triang1 = '''3
    7 4
    2 4 6
    8 5 9 3'''
    

    report(triang1, verbose=True)
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
    report(triang2, verbose=False)
    
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()