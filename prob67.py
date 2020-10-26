# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:59:40 2020

@author: Admin
"""
# ONGOING

# project euler: https://projecteuler.net
# problem 67: Maximum path sum II

from time import time

from prob18 import solution


def report(triangle_str):
    print(f'max total of the triangle\n{triangle_str}\nis {solution(triangle_str)}')    

    
def main():
    tic = time()
    
    test_str1 = '''3
    7 4
    2 4 6
    8 5 9 3'''
    
    report(test_str1)
    # 23
    
    # projecteuler number:
    file = 'data/p067_triangle.txt'
    with open(file, 'r') as myfile:
        test_str2 = myfile.read()
        
#    print(test_str2)
#    test_str2 = '''75
#    95 64
#    17 47 82
#    18 35 87 10
#    20 04 82 47 65
#    19 01 23 75 03 34
#    88 02 77 73 07 63 67
#    99 65 04 28 06 16 70 92
#    41 41 26 56 83 40 80 70 33
#    41 48 72 33 47 32 37 16 94 29
#    53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#    91 71 52 38 17 14 91 43 58 50 27 29 48
#    63 66 04 68 89 53 67 30 73 16 69 87 40 31
#    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
    report(test_str2)
    
     
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()