# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:28:00 2021

@author: PC1
"""

# ONGOING

# project euler: https://projecteuler.net
# problem 79: passcode derivation


from time import time


def solution(nums):
    all_digits = []
    digits_dicts = []

    for i, num in enumerate(nums):
        digits = list(str(num))
        # digits_dict = {d:(i,j) for j, d in enumerate(digits)}
        # print(digits_dict)
        # digits_dicts.append({num: digits_dict})
        digits_dicts.append({num: digits})

        for digit in digits:
            all_digits.append(digit)

    print(digits_dicts)

    for i, dic in enumerate(digits_dicts):
        for k, v in dic.items():
            if i == 0:
                pw = ['', v[0], '', v[1], '', v[2], '']
                pws = [pw]
            else:
                for pw in pws:
                    for p in pw:
                        print(p)

    pw_long = ''.join([str(d) for d in all_digits])
    print(pw_long)

    return pw


def report(num):
    print((f'sum of numbers below {num} that are multiples of 3 or 5 '
           f'is {solution(num)}'))


def main():
    tic = time()

    file = 'data/p079_keylog.txt'

    with open(file, 'r') as f:
        text = f.read()
        # text = f.readlines()

    print(text)

    # nums = list(map(int, text.split()))
    nums = text.split()

    print(nums)

    report(10)
    # 23

    # projecteuler number:
    report(1000)
    # 233168

    toc = time()

    print('time used:', toc - tic)


if __name__ == '__main__':
    main()
