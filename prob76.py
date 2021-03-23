# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 03:58:03 2021

@author: rop
"""

# ONGOING

# project euler: https://projecteuler.net
# problem 76: counting summations


from time import time
from itertools import combinations


def get_new_summ(ans_all, n_upper, ans_base, verbose=True):
    '''recusrive function to get possible sum combinations'''
    # print('verbose:', verbose)
    new_ans_all = ans_all.copy()
    for x in range(1, n_upper):
        remain = n_upper - x
        ans = ans_base + [x, remain]
        ans_sorted = sorted(ans)
        if verbose:
            print('x, remain, ans:', x, remain, ans)
        if ans_sorted not in new_ans_all:
            if verbose:
                print('added:', ans_sorted)
            new_ans_all.append(ans_sorted)
            if remain == 1:
                continue
            else:
                new_ans_all = get_new_summ(new_ans_all, remain, ans[:-1],
                                           verbose=verbose)

    return new_ans_all


def solution2(num, verbose=True):  # too slow
    ans_all = [[1] * num]
    new_ans_all = get_new_summ(ans_all, num, [], verbose=verbose)
    if verbose:
        print(new_ans_all)
    return len(new_ans_all)


def solution(num):
    '''brute force for 5'''
    ans = [1] * num
    ans_all = [sorted(ans)]

    for x in range(1, num):  # 1
        remain = num-x
        ans = [x, remain]
        # ans = sorted([x, remain])
        if sorted(ans) not in ans_all:
            ans_all.append(sorted(ans))
        if remain > 1:
            ans_wo_remain = ans[:-1].copy()
            for x2 in range(1, remain):  # 2
                remain2 = remain-x2
                new_elems = [x2, remain2]
                new_ans = ans_wo_remain + new_elems
                # ans = sorted([x, x2, remain2])
                if sorted(new_ans) not in ans_all:
                    ans_all.append(sorted(new_ans))
                if remain2 > 1:
                    # ans_wo_remain = new_ans[:-1].copy()
                    for x3 in range(1, remain2):  # 3
                        remain3 = remain2-x3
                        new_ans = sorted([x, x2, x3, remain3])
                        if new_ans not in ans_all:
                            ans_all.append(new_ans)

    print(ans_all)
    return len(ans_all)


def solution3(num, verbose=True):
    ''' ooo | oo | oooo '''
    ans0 = [1] * num
    ans_all = [ans0]

    n_btwn = num - 1

    for nb in range(1, n_btwn):
        print(f'{nb} dividers')
        # choose nb locations [0, 1, ...]
        combis = combinations(range(n_btwn), nb)

        for combi in combis:
            # print(combi)
            ans = []
            idx_prev = 0
            for i, c in enumerate(combi):
                # ans.append(sum(ans0[idx_prev:c+1]))
                ans.append(c + 1 - idx_prev)
                idx_prev = c + 1
                # if i == len(combi) - 1:
                #     # ans.append(sum(ans0[idx_prev:]))
                #     ans.append(num - c - 1)
            ans.append(num - c - 1)
            if verbose:
                print(combi, ans)
            ans.sort()
            if ans not in ans_all:
                ans_all.append(ans)

    if verbose:
        print(ans_all)
    return len(ans_all)


def solution4(num, verbose=True):
    ''' 5 -> 1, 4
                4 -> 1, 3
                        3 -> 1, 2, ...
    '''
    ans_all = []
    for i in range(1, int((num+1)/2+1)):
        remain = num - i
        a = [i, remain]
        if verbose:
            print('i, remain:', i, remain)
        if sorted(a) not in ans_all:
            ans_all.append(sorted(a))
            if verbose:
                print(ans_all)
        while remain > i:
            a_base = a[:-1].copy()
            new_remain = remain - i
            a_new = a_base + [i, new_remain]
            if verbose:
                print(a_new)
            remain = new_remain
            if sorted(a_new) not in ans_all:
                ans_all.append(sorted(a_new))
                if verbose:
                    print(ans_all)
                a = a_new.copy()

    for i, a in enumerate(ans_all):
        print(i+1, a)

    return len(ans_all)


def solution5(num, verbose=True):
    ''' 5 -> 1, 4
                4 -> 1, 3
                        3 -> 1, 2, ...
    '''
    ans_all = []
    for i in range(1, int((num+1)/2+1)):
        remain = num - i
        a = [i, remain]
        if verbose:
            print('-' * 20)
            print('i, remain:', i, remain)
        if sorted(a) not in ans_all:
            ans_all.append(sorted(a))
            if verbose:
                print('ans_all:', ans_all)
        while remain > 1:
            a_base = a[:-1].copy()
            jrange = range(1, i+1)
            for j in jrange:
                j_remain = remain - j
                if j_remain > 0:
                    a_new = a_base + [j, j_remain]
                    print('i, j, a_new, j_remain:', i, j, a_new, j_remain)
                    if (sorted(a_new) not in ans_all) and (sum(a_new) == num):
                        ans_all.append(sorted(a_new))
                        if verbose:
                            print('updated ans_all:', ans_all)
                        a = a_new.copy()
            remain = j_remain

    for i, a in enumerate(ans_all):
        print(i+1, a, sum(a))

    return len(ans_all)


def solution6(num, verbose=True):
    ''' 5 -> 1, 4
                4 -> 1, 3
                        3 -> 1, 2, ...
    '''
    ans_all = []
    for i in range(1, int((num+1)/2+1)):
        remain = num - i
        a = [i, remain]
        if verbose:
            print('i, remain:', i, remain)
        if sorted(a) not in ans_all:
            ans_all.append(sorted(a))
            if verbose:
                print(ans_all)
        a_base = a[:-1].copy()
        while remain > 1:
            # print('a_base, remain:', a_base, remain)
            jrange = range(1, i+1)
            # jrange = range(1, remain)
            for j in jrange:
                print('i, j =', i, j)
                j_remain = remain - j
                if j_remain > 0:
                    a_new = a_base + [j, j_remain]
                    # print('i, j, a_new, j_remain:', i, j, a_new, j_remain)
                    if (sorted(a_new) not in ans_all) and (sum(a_new) == num):
                        ans_all.append(sorted(a_new))
                        if verbose:
                            print('updated ans_all:', ans_all)
                a_base = a_new[:-1].copy()
                # a = a_new.copy()
                remain = j_remain

    for i, a in enumerate(ans_all):
        print(i+1, a, sum(a))

    return len(ans_all)


def get_sum_pairs(num):
    pairs = []
    for i in range(1, int((num)/2)+1):
        remain = num - i
        a = [i, remain]
        pairs.append(sorted(a))
    return pairs


def get_sum_pairs_gen(num):
    for i in range(1, int((num)/2)+1):
        # remain = num - i
        # yield ([i, remain]).sort()
        # a = [i, remain]
        # yield a
        yield [i, num - i]
        # yield sorted(a)


def solution7(num, verbose=True):
    ''' break number into pairs successively
        5 -> [1, 4], [2, 3]
        [1, 4] -> [1, 1, 3], [1, 2, 2]
        [2, 3] -> [2, 1, 2]
    '''

    # initialize
    # pairs = get_sum_pairs(num)
    pairs = get_sum_pairs_gen(num)

    ans_prev = list(pairs)

    # ans_all = ans_prev.copy()

    print('-' * 20)
    print(f'{len(ans_prev)} initial pairs for {num}: {ans_prev}')

    cnt = len(ans_prev)

    # curr_max_len = 2
    nloop = 1
    keep_repeat = True

    while keep_repeat:
        if verbose:
            print('-' * 10)
            print('loop', nloop)
        keep_repeat = False
        # ans_all_updated = ans_prev.copy()
        ans_new = []  # refresh at start of each loop

        for a in ans_prev:
            # if len(a) < curr_max_len:
            #     continue
            a_last = a[-1]
            if a_last > 1:
                a_base = a[:-1].copy()
                # pairs_last = get_sum_pairs(a_last)
                pairs_last = get_sum_pairs_gen(a_last)
                for pair in pairs_last:
                    a_new = a_base + pair
                    a_new_sort = sorted(a_new)
                    if verbose:
                        print(a, '-->', a_new)
                        # print(a, '-->', a_new_sort)
                    # if a_new not in ans_new:
                    if a_new_sort not in ans_new:
                        ans_new.append(a_new_sort)
                        cnt += 1
                        if a_new[-1] > 1:
                            keep_repeat = True

        # curr_max_len += 1
        ans_prev = ans_new.copy()
        # ans_all += ans_new
        # ans_all = ans_all_updated

        if verbose:
            print(f'new_ans in loop {nloop}: {ans_new}')
            # print(f'current ans_all in loop {nloop}: {ans_all}')
            nloop += 1

    # ans_len = len(ans_all)

    # if verbose:
    #     print('-' * 20)
    #     print('summations:')
    #     if ans_len > 20:
    #         for i, a in enumerate(ans_all[-20:]):
    #             print(i+1, a, sum(a))
    #     else:
    #         for i, a in enumerate(ans_all):
    #             print(i+1, a, sum(a))

    # return ans_len

    return cnt


def report(num, verbose=True):
    print((f'number of different ways can {num} be written as sum '
           # f'is {solution2(num, verbose=verbose)}'))
           # f'is {solution3(num, verbose=verbose)}'))
           # f'is {solution4(num, verbose=verbose)}'))
           # f'is {solution5(num, verbose=verbose)}'))
           f'is {solution7(num, verbose=verbose)}'))


def main():
    tic = time()

    report(5, verbose=True)
    # 6

    report(40, verbose=False)
    # 37337

    # projecteuler number:
    # report(100, verbose=False)
    # 2500

    toc = time()

    print('time used:', toc - tic)


if __name__ == '__main__':
    main()
