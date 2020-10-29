# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:12:32 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 23: non-abundant sums

from time import time

from prob12 import find_divisors


def check_type(num):
    divs = find_divisors(num)
    divs.remove(num)
    # print(divs)
    
    sum_div = sum(divs)
    if sum_div == num:
        return 'perfect'
    elif sum_div > num:
        return 'abundant'
    else:
        return "deficient"
    
    
def solution(num):
    num_type = check_type(num)
    return num_type


def report(num):
    print(f'{num} is {solution(num)}')


def main():
    tic = time()
    
    report(28)

    report(12)
    
    # projecteuler number:
    # report(1000)
    # 233168
    
    n_max = 28123
    nums_ans = []
    for i in range(1, n_max+1):
        abundant = False
        for j in range(1, int(i/2)+1):
            # print(f'i={i}, j={j} ({solution(j)}), i-j={i-j} ({solution(i-j)})')
            if (solution(j)=='abundant') and (solution(i-j)=='abundant'):
                abundant = True
                break
        if not abundant:
            nums_ans.append(i)
    summ = sum(nums_ans)
    print('sum of all positive integers that cannot be written as the sum of two abundant numbers:', summ)
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()