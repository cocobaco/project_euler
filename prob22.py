# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:18:29 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 22: Names scores

from time import time
from string import ascii_uppercase


def get_score(name, order, letters_dict):
    letters = list(name)
    summ = 0
    for lett in letters:
        summ += letters_dict[lett]
    # print('sum =', summ)
    score = summ * order
    return score
    
    
def solution(name_list, letters_dict):
    score = 0
    for i, name in enumerate(name_list):
        score += get_score(name, i+1, letters_dict)
    return score


def report(name_list, letters_dict):
    print(f'total score is {solution(name_list, letters_dict)}')


def main():
    tic = time()
    
    file = 'data/p022_names.txt'
    
    with open(file, 'r') as myfile:
        # read all lines
        names = myfile.read()
        
    name_list = names.split(',')
    
    # clean quotes
    name_list = [name.strip('"') for name in name_list]
    
    # sort
    name_list.sort()

    print(len(name_list), 'names found')
    
    LETTERS = ascii_uppercase
    
    letters_dict = {letter: n+1 for n, letter in enumerate(LETTERS)}
    
    # projecteuler data
    report(name_list, letters_dict)
    # 871198282
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()