# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:17:57 2020

@author: Admin
"""
# project euler: https://projecteuler.net
# problem 32: pandigital product

from time import time
    

def digits_unique(num):
    num_str_list = list(str(num))
    if len(set(num_str_list)) == len(num_str_list):
        return True
    else:
        return False
    

def is_pandigital(num):
    str_num = list(map(int, list(str(num))))
    # print(str_num)
    if len(str_num) == len(set(str_num)):
        if set(str_num) == set(range(1, len(str_num)+1)):
            return True
        else:
            return False
    else:
        return False


def solution(n_max):
    # num_pandigit = int(''.join(map(str, range(1, n_max+1))))
   
    products_pan = [] 
   
    # for prod in range(2, int(num_pandigit/2)):
    for prod in range(2, int('9' * int(n_max/2))):
        if not digits_unique(prod):
            continue
        # print(prod)
        for multiplicand in range(2, int(prod/2)):
            if len(str(multiplicand)) + len(str(prod)) >= n_max:
                continue
            if not digits_unique(multiplicand):
                continue
            if prod % multiplicand == 0:
                multiplier = int(prod / multiplicand)
                if not digits_unique(multiplier):
                    continue
                if len(str(multiplicand) + str(prod) + str(multiplier)) != n_max:
                    continue
                num3terms = int(str(multiplicand) + str(multiplier) + str(prod))
                if len(str(num3terms)) == n_max and is_pandigital(num3terms):
                    print(prod, ' = ', multiplicand, ' x ', multiplier)
                    if prod not in products_pan:
                        products_pan.append(prod)
                    break
                
    print(products_pan)

    return sum(products_pan)


def report(n_max):
    print(('sum of all products whose multiplicand/multiplier/product '
           f'can be written as 1 through {n_max} pandigital is {solution(n_max)}'))


def main():
    tic = time()
    
    report(5)
    # 29222
    
    # projecteuler number:
    report(9)
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()