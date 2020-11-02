# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:11:36 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 24: lexicographic permutations

from time import time

def solution(n, ith, verbose=False):
    perms = []
    nums = list(range(n+1))
    for num in nums:
        perms.append(str(num))
    if verbose:
        print('initial perms:', perms) 
    
    length = len(perms[0])
    # print(length)
    while length < n + 1:
        new_perms = []
        for perm in perms:
            if verbose:
                print(perm)
            li = list(map(int, list(perm)))
            remains = [x for x in nums if x not in li]
            if len(remains) == 0:
                continue
            else:
                if verbose:
                    print('remains:', remains)
                for j in remains:
                    new_perm = li + [j]
                    new_perm_str = ''.join(map(str, new_perm))
                    if verbose:
                        print(new_perm_str)
                    new_perms.append(new_perm_str)
        perms = new_perms
        length = len(perms[0])
        if verbose:
            print('length:', length)
        
    perms.sort()
    if verbose:
        print('sorted perms:', perms)
        
    perm_ith = perms[ith-1]
    
    return perms, perm_ith


def report(n, ith, verbose=False):
    print(f'the {ith}-th lexicographic permutation of digits 0-{n} is {solution(n, ith, verbose=verbose)[1]}.')    

    
def main():
    tic = time()
    
    report(3, 2, verbose=True)
    
    # projecteuler number:
    report(9, 1000000, verbose=False)
    # 2783915460
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()