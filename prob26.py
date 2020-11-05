# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:41:03 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 26: Reciprocal cycles

# ONGOING

from time import time
    

def long_divide(num, div, verbose=True):
    ans = num // div
    if verbose:
        print(ans)
    ans_str = str(ans) + '.'
    
    remain = int(num % div)
    decimals = []
    
    # i = 1
    # i_max = 10
    num_digits_recur = 0
    
    # while i < i_max:
    while True:
        next_num = remain * 10
        next_digit = int(next_num // div)
        if verbose:
            print('next_digit:', next_digit)
        remain = int(next_num % div)
        if verbose:
            print('remain:', remain)

        ans_str = ans_str + str(next_digit)
        ans = float(ans_str)
        # ans = ans + next_digit / (10. ** i)
        if verbose:
            print('updated_ans:', ans)
        
        if remain == 0:
            if verbose:
                print('remain = 0')
            break            
    
        # check for repeat        
        # if int(ans_str[-1]) in decimals:
        if next_digit in decimals:
            if verbose:
                print('found repeat')
            num_digits_recur = len(decimals) - decimals.index(next_digit)
            break
        
        decimals.append(next_digit)
        if verbose:
            print(decimals)
        
        # i += 1
    
    return ans, num_digits_recur
    
    
def solution(num, n, verbose=True):
    max_recur = 0
    for div in range(2, n):
        ans = long_divide(num, div, verbose=verbose)
        if ans[1] > max_recur:
            max_recur = ans[1]
            frac = ans[0]
            d = div
        
    return frac, max_recur, d


def report(num, n, verbose=True):
    frac, max_recur, d = solution(num, n, verbose=verbose)
    print(f'd < {n} for which 1/d gives the longest recurring cycle in its decimal fraction part is {max_recur}')
    print(f'd={d}, frac={frac}')    
    

def main():
    tic = time()
    
    report(1, 11, verbose=True)
    # d=7, recur=6
    
    # projecteuler number:
    report(1, 1000, verbose=False)
    # 233168
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()