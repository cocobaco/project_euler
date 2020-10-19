# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:53:26 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 12: Highly divisible triangular number

from time import time
import matplotlib.pyplot as plt
import math

plt.style.use('default')


def find_divisors(n):
    divisors = [1, n]
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if (n % i == 0):
            divisors.extend([i, int(n / i)])
    return sorted(list(set(divisors)))


def solution(n):
    ans = 0
    for i in range(n+1):
        ans += i
    divisors = find_divisors(ans)
    # print(divisors)
    n_divisors = len(divisors)
    return ans, n_divisors
    

def report(n):
    triang, n_divisors = solution(n)
    print(f'the {n}-th triangle number is {triang} ({n_divisors} divisors)')    
    
    
def main():
    tic = time()
    
    report(7)
    # triang = 28, 6 divisors
    
    report(1000)
    # triang = 500500, 96 divisors
    
    # report(5984)
    # triang = 17907120, 480 divisors
    
    # projecteuler number:
    target_n_divisors = 500
    n = 1  # starting number
    # n = 5900  # starting number
    ns, triangs, n_divs = [], [], []
    while True:
        triang, n_divisors = solution(n)
        ns.append(n)
        triangs.append(triang)
        n_divs.append(n_divisors)
        # print(f'{n}: triangle number = {triang}, {n_divisors} divisors')
        if n_divisors > target_n_divisors:
            break
        else:
            if n % 100 == 0:
                print(n, triang, n_divisors)
            n += 1
    print(f'{n}-th triangle number is {triang} ({n_divisors} divisors) is first with over {target_n_divisors} divisors')
    # answer: n = 12375, triang = 76576500, n_divisors = 576
    
    f, ax = plt.subplots(nrows=2)
    ax[0].plot(ns, n_divs)
    ax[0].set_xlabel('number to calculate triangle number')
    ax[0].set_ylabel('number of divisors')
    ax[1].plot(triangs, n_divs)
    ax[1].set_xlabel('triangle number')
    ax[1].set_ylabel('number of divisors')
    plt.show()
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()