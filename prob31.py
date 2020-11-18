# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:38:49 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 31: Coin sums

from time import time
    
coins = {'1p': 0.01, '2p': 0.02, '5p': 0.05, '10p': 0.1, 
             '20p': 0.2, '50p': 0.5, '1': 1., '2': 2.}


def sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p):
    ans = coins['2'] * n2 + coins['1'] * n1 + coins['50p'] * n50p \
        + coins['20p'] * n20p + coins['10p'] * n10p + coins['5p'] * n5p \
        + coins['2p'] * n2p + coins['1p'] * n1p
    return round(ans, 2)

        
def solution(num, verbose=True):
    
    combos = []
    
    max_coins = {k:int(num/v) for k,v in coins.items()}
        
    for n2 in range(max_coins['2'], -1, -1):
        n1, n50p, n20p, n10p, n5p, n2p, n1p = 0, 0, 0, 0, 0, 0, 0
        val = sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p)
        if val > num:
            continue
        if val == num:
            # n1, n50p, n20p, n10p, n5p, n2p, n1p = 0, 0, 0, 0, 0, 0, 0
            combo = {'2': n2, '1': n1, '50p': n50p, '20p': n20p, 
                     '10p': n10p, '5p': n5p, '2p': n2p, '1p': n1p}
            combos.append(combo)
            continue
        for n1 in range(max_coins['1'], -1, -1):
            n50p, n20p, n10p, n5p, n2p, n1p = 0, 0, 0, 0, 0, 0
            val = sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p)
            if val > num:
                continue
            if val == num:
                combo = {'2': n2, '1': n1, '50p': n50p, '20p': n20p, 
                         '10p': n10p, '5p': n5p, '2p': n2p, '1p': n1p}
                combos.append(combo)
                continue
            for n50p in range(max_coins['50p'], -1, -1):
                n20p, n10p, n5p, n2p, n1p = 0, 0, 0, 0, 0
                val = sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p)
                if val > num:
                    continue
                if val == num:
                    combo = {'2': n2, '1': n1, '50p': n50p, '20p': n20p, 
                             '10p': n10p, '5p': n5p, '2p': n2p, '1p': n1p}
                    combos.append(combo)
                    continue
                for n20p in range(max_coins['20p'], -1, -1):
                    n10p, n5p, n2p, n1p = 0, 0, 0, 0
                    val = sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p)
                    if val > num:
                        continue
                    if val == num:
                        combo = {'2': n2, '1': n1, '50p': n50p, '20p': n20p, 
                             '10p': n10p, '5p': n5p, '2p': n2p, '1p': n1p}
                        combos.append(combo)
                        continue
                    for n10p in range(max_coins['10p'], -1, -1):
                        n5p, n2p, n1p = 0, 0, 0
                        val = sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p)
                        if val > num:
                            continue
                        if val == num:
                            combo = {'2': n2, '1': n1, '50p': n50p, '20p': n20p, 
                                 '10p': n10p, '5p': n5p, '2p': n2p, '1p': n1p}
                            combos.append(combo)
                            continue
                        for n5p in range(max_coins['5p'], -1, -1):
                            n2p, n1p = 0, 0
                            val = sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p)
                            if val > num:
                                continue
                            if val == num:
                                combo = {'2': n2, '1': n1, '50p': n50p, '20p': n20p, 
                                     '10p': n10p, '5p': n5p, '2p': n2p, '1p': n1p}
                                combos.append(combo)
                                continue
                            for n2p in range(max_coins['2p'], -1, -1):
                                n1p = 0
                                val = sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p)
                                if val > num:
                                    continue
                                if val == num:
                                    combo = {'2': n2, '1': n1, '50p': n50p, '20p': n20p, 
                                             '10p': n10p, '5p': n5p, '2p': n2p, '1p': n1p}
                                    combos.append(combo)
                                    # print(combo)
                                    continue
                                for n1p in range(max_coins['1p'], -1, -1):
                                    val = sum_value(n2, n1, n50p, n20p, n10p, n5p, n2p, n1p)
                                    if val > num:
                                        continue
                                    if val == num:
                                        combo = {'2': n2, '1': n1, '50p': n50p, '20p': n20p, 
                                                 '10p': n10p, '5p': n5p, '2p': n2p, '1p': n1p}
                                        # print(combo)
                                        combos.append(combo)

    if verbose:
        for c in combos:
            print(c)
    
    return len(combos)


def report(num, verbose=True):
    print((f'there are {solution(num, verbose=verbose)} combinations of coins to '
           f'make up {num} pounds'))


def main():
    tic = time()
    
    report(0.05)
    # 4
    
    report(0.17)
    # 28
    
    # projecteuler number:
    report(2, verbose=False)
    # 66924
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()