# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:36:58 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 14: Longest Collatz sequence

from time import time
import matplotlib.pyplot as plt

plt.style.use('default')


def solution(n):
    seq = [n]
    while True:
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3 * n + 1
        seq.append(n)
        if n == 1:
            break
    length = len(seq)
    return seq, length
    

def report(n):
    seq, length = solution(n)
    print(f'the Collatz sequence starting with {n} is {seq} (length={length})')    
    plt.figure()
    plt.plot(seq)
    plt.title(f'Collatz sequence with starting number = {n}\n(length = {length})')
    plt.show()
    
    
def main():
    tic = time()
    
    report(13)
    
    report(100)
    
    # projecteuler number:
    n_max = 999999
    ns, lengths = [], []
    for n in range(1, n_max+1):
        if n % 100000 == 0:
            print(n)
        seq, length = solution(n)
        ns.append(n)
        lengths.append(length)
    
    max_length = max(lengths)
    max_start_n = ns[lengths.index(max_length)]
    
    print(f'starting number of {max_start_n} gives maximum length of {max_length}')
    
    f, ax = plt.subplots()
    ax.plot(ns, lengths)
    ax.set_xlabel('starting number')
    ax.set_ylabel('length of Collatz sequence')

    plt.show()
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()