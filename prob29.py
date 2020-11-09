# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:43:35 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 29: Distinct powers

from time import time
    

def solution(arange, brange):
    ans = []
    for a in arange:
        for b in brange:
            term = a ** b
            if term not in ans:
                ans.append(a ** b)
    return ans, len(ans)


def report(arange, brange):
    print(('number of distinct terms in the sequence a^b for '
           f'a in {arange} and b in {brange} is {solution(arange, brange)[1]}'))


def main():
    tic = time()
    
    report(range(2, 6), range(2, 6))
    # 15
    
    # projecteuler number:
    report(range(2, 101), range(2, 101))
    # 9183
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()