# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:31:48 2021

@author: rop
"""

# project euler: https://projecteuler.net
# problem 61: Cyclical figurate numbers

from time import time

from prob44 import calc_n_pent
from prob45 import calc_n_triang, calc_n_hexa


def calc_n_sq(n):
    return n ** 2


def calc_n_hepta(n):
    ans = int(n * (5*n - 3)/2)
    return ans


def calc_n_octa(n):
    ans = int(n * (3*n - 2))
    return ans


def is_polygonal(num, calc_func):
    i = 1
    n_poly = calc_func(i)
    
    while num > n_poly:
        i += 1
        n_poly = calc_func(i)
        if n_poly == num:
            # return True, i
            return True
        
    # return False, None
    return False


def check_valid(n1, n2):
    if len(str(n1)) != 4 or len(str(n2)) != 4:
        print('invalid arguments')
        return False
    if n1 == n2:
        return False
    n1a, n1b = int(str(n1)[:2]), int(str(n1)[2:])
    n2a, n2b = int(str(n2)[:2]), int(str(n2)[2:])    
    if n1a * n1b * n2a * n2b == 0:
        return False
    if (n1a == n1b) or (n2a == n2b):
        return False
    if (n1a == n2a) or (n1b == n2b) or (n1a == n2b):
        return False
    
    return True    


def check_cyclic(n1, n2):
    '''check whether two 4-digit numbers are cyclic (directional)'''    
    n1b = int(str(n1)[2:])  # last 2 digits of n1
    n2a = int(str(n2)[:2])  # first 2 digits of n2

    if (n1b == n2a):  # it should only go one-way
        return True
    return False
    

def find_cyclic_pair(x, ys):
    for y in ys:
        if check_cyclic(x, y):
            return y
    return False


def check_all_cyclic(nums):
    '''check whethers all the numbers are cyclic to one another'''
    if len(nums) <= 2:
        print('invalid arguments')
        return None

    x0 = nums[0]
    x = x0
    nums_others = [n for n in nums if n != x]
    nums_checked = [x]
    
    while len(nums_others) > 0:
        y = find_cyclic_pair(x, nums_others)
        if not y:
            return False
        
        nums_checked.append(y)
        nums_others = [n for n in nums if n not in nums_checked]
        x = y
    
    if check_cyclic(x, x0):
        return True
    return False


def check_all_valid(nums):
    if len(set(nums)) != len(nums):
        return False
    return all(check_valid(i, j) for i in nums for j in nums if j!=i)   
        

def find_nums3(nums_dict, verbose=True):
    # https://radiusofcircle.blogspot.com/2016/10/problem-61-project-euler-solution-with.html
    
    ks = list(nums_dict.keys())
    poly1 = nums_dict[ks[0]]
    
    poly_others = [nums_dict[ks[i]] for i in range(1, 6)]
    
    # for poly2 in poly_others:
    #     for n1 in poly1:
    for n1 in poly1:
        for poly2 in poly_others:
            for n2 in poly2:
                if check_cyclic(n1, n2):
                    for poly3 in poly_others:
                        if (poly3 != poly2):
                            for n3 in poly3:
                                if check_cyclic(n2, n3):
                                    for poly4 in poly_others:
                                        if (poly4 != poly3) and (poly4 != poly2):
                                            for n4 in poly4:
                                                if check_cyclic(n3, n4):
                                                    for poly5 in poly_others:
                                                        if (poly5 != poly4) and (poly5 != poly3) and (poly5 != poly2):
                                                            for n5 in poly5:
                                                                if check_cyclic(n4, n5):
                                                                    for poly6 in poly_others:
                                                                        if (poly6 != poly5) and (poly6 != poly5) and (poly6 != poly4) and (poly6 != poly3) and (poly6 != poly2):
                                                                            for n6 in poly6:
                                                                                if check_cyclic(n5, n6):
                                                                                    if check_cyclic(n6, n1):
                                                                                        ns = [n1, n2, n3, n4, n5, n6]
                                                                                        print('answer:', ns)
                                                                                        return ns
    
    

    return None


def find_nums(nums_dict, verbose=True):
    ks = list(nums_dict.keys())
    # build candidate list and check if it is cyclic and not repeated
    idx = 1
    for n5 in nums_dict[ks[5]]:
        for n4 in nums_dict[ks[4]]:
            ns = [n5[0], n4[0]]
            if not check_all_valid(ns):
            # if not all(check_valid(i, j) for i in ns for j in ns if j!=i):
            # if not check_valid(n0[0], n1[0]):
                continue
            # if (n1[0] == n0[0]):
            #     continue
            for n3 in nums_dict[ks[3]]:
                ns = [n5[0], n4[0], n3[0]]
                if not check_all_valid(ns):
                    continue
                # if (n2[0] in [n0[0], n1[0]]) or not check_valid(n2[0], n1[0]):
                #     continue
                for n2 in nums_dict[ks[2]]:
                    ns = [n5[0], n4[0], n3[0], n2[0]]
                    if not check_all_valid(ns):
                        continue
                    # if (n3[0] in [n0[0], n1[0], n2[0]]) or not check_valid(n3[0], n2[0]):
                    #     continue
                    for n1 in nums_dict[ks[1]]:
                        ns = [n5[0], n4[0], n3[0], n2[0], n1[0]]
                        if not check_all_valid(ns):
                            continue
                    # if (n3[0] in 
                        # if (n4[0] in [n0[0], n1[0], n2[0], n3[0]]) or not check_valid(n4[0], n3[0]):
                        #     continue
                        for n0 in nums_dict[ks[0]]:
                            ns = [n5[0], n4[0], n3[0], n2[0], n1[0], n0[0]]
                            if not check_all_valid(ns):
                               continue
                            # if (n5[0] in [n0[0], n1[0], n2[0], n3[0], n4[0]]) or not check_valid(n5[0], n4[0]):
                            #     continue
                            # ns = [n0[0], n1[0], n2[0], 
                            #             n3[0], n4[0], n5[0]]
                            if verbose:
                                print(idx, ns)
                            idx += 1
                            # # if list(set(ns)) != ns:
                            # #     # check that all numbers are different
                            # #     # already did the check above
                            # #     continue
                            if check_all_cyclic(ns):
                                print('answer:', ns)
                                return ns
    return None

    
def find_nums2(nums_dict, verbose=True):
    ks = list(nums_dict.keys())
    # build candidate list and check if it is cyclic and not repeated
    idx = 1
    for n0 in nums_dict[ks[0]]:
        if '0' in str(n0[0]):  # make sure it doesn't contain 0
            continue
        ns = [n0[0]]
        for n1 in nums_dict[ks[1]]:
            if ('0' in str(n1[0])) or (n1[0] == n0[0]) or (not check_cyclic(n0[0], n1[0])):
                continue
            ns.append(n1[0])
            # print(ns)
            for n2 in nums_dict[ks[2]]:
                if ('0' in str(n2[0])) or (n2[0] in [n0[0], n1[0]]) or (not check_cyclic(n1[0], n2[0])):
                    continue
                ns.append(n2[0])
                # print(ns)
                for n3 in nums_dict[ks[3]]:
                    if ('0' in str(n3[0])) or (n3[0] in [n0[0], n1[0], n2[0]]) or (not check_cyclic(n2[0], n3[0])):
                        continue
                    ns.append(n3[0])
                    # print(ns)
                    for n4 in nums_dict[ks[4]]:
                        if ('0' in str(n4[0])) or (n4[0] in [n0[0], n1[0], n2[0], n3[0]]) or (not check_cyclic(n3[0], n4[0])):
                            continue
                        ns.append(n4[0])
                        # print(ns)
                        for n5 in nums_dict[ks[5]]:
                            if ('0' in str(n5[0])) or (n5[0] in [n0[0], n1[0], n2[0], n3[0], n4[0]]) or (not check_cyclic(n4[0], n5[0])):
                                continue
                            ns.append(n5[0])
                            print(idx, ns)
                            idx += 1
                            if check_cyclic(n5[0], n0[0]):
                                # final check
                                print('answer:', ns)
                                return ns
                            # # if list(set(ns)) != ns:
                            # #     # check that all numbers are different
                            # #     # already did the check above
                            # #     continue
                            # if verbose:
                            #     print(idx, ns)     
                            # idx += 1
                            # if check_all_cyclic(ns, verbose=verbose):
                            #     # print('found answer:', ns)
                            #     summ = sum(ns)
                            #     return summ
    return None

    
def solution(verbose=True):
    
    # range of 4-digit numbers: 1000-9999
    num = 4
    n_range = range(int(10**(num-1)), int(10**(num)))
    
    poly_funcs = {'tri': calc_n_triang, 
                  'squ': calc_n_sq, 
                  'pen': calc_n_pent, 
                  'hex': calc_n_hexa, 
                  'hep': calc_n_hepta, 
                  'oct': calc_n_octa}
    
    # find all polygonal numbers in the range
    poly_nums = {k:[] for k in poly_funcs.keys()}
    
    for n in n_range:
        # if '0' in str(n):  # filter out numbers containing 0
        #     continue
        for k, f in poly_funcs.items():
            # is_poly, i = is_polygonal(n, f)
            # if is_poly:
            #     poly_nums[k].append([n, i])
            if is_polygonal(n, f):
                poly_nums[k].append(n)
    
    print('count:')
    num_combins = 1
    for k, nums in poly_nums.items():
        print(k, len(nums))
        num_combins *= len(nums)
        
    print(f'possible combinations: {num_combins:,d}')
        
    # ns = find_nums(poly_nums, verbose=verbose)
    ns = find_nums3(poly_nums, verbose=verbose)
    # summ = find_nums2(poly_nums, verbose=verbose)
    
    return sum(ns)


def report(verbose=True):
    print(('sum of six cyclic 4-digit numbers for which each polygonal type '
           f'is represented is {solution(verbose=verbose)}'))


def main():
    tic = time()
    
    # projecteuler number:
    report(verbose=True)
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()