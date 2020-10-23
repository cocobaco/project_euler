# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:03:32 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 15: Lattice paths

from time import time
# from itertools import chain
from math import factorial


# first try. does not work at all.
# def solution2(n):
#     i, j = 0, 0
#     n_routes = 0
#     p = np.array([i, j])
#     step = 1
#     while step < 2 * n:
#         print('present location:', p)
#         print(f'taking step {step}')
#         if (p[0] == n) and (p[1] < n):
#             poss_dir = np.array([[0,1]])
#         elif (p[0] < n) and (p[1] == n):
#             poss_dir = np.array([[1,0]])
#         else:
#             poss_dir = np.array([[0,1], [1,0]])
        
#         for direction in poss_dir:
#             new_p = p + direction
#             print('new location:', new_p)
#             if step < 2 * n:
#                 p = new_p
#                 step += 1
#             elif (new_p == np.array([n, n])).all():
#                 print('valid route')
#                 n_routes += 1

#     return n_routes


# MEMORY INTENSIVE
# works up to step 22 then hangs
# def solution(n, verbose=True):
#     n_routes = 0
#     p = [0,0]
#     routes_valid = [[p]]
#     n_steps = 2 * n
#     print('steps to take:', n_steps)
#     for step in range(1, n_steps+1):
#         if verbose:
#             print('step', step)
#         routes_valid_update = []
#         for route in routes_valid:
#             p_prev = route[-1]
#             if verbose:
#                 print('latest point =', p_prev)
#             if p_prev[0] < n:
#                 # go right
#                 p_go_right = [p_prev[0] + 1, p_prev[1]]
#                 # if p_go_right[0] <= n and p_go_right[1] <= n:
#                 route_update = route + [p_go_right]
#                 if verbose:
#                     print('right is valid route')
#                     print(route_update)
#                 routes_valid_update.append(route_update)
#             if p_prev[1] < n:
#                 # go down
#                 p_go_down = [p_prev[0], p_prev[1] + 1]
#                 # if p_go_down[0] <= n and p_go_down[1] <= n:
#                 route_update = route + [p_go_down]
#                 if verbose:
#                     print('down is valid route')
#                     print(route_update)
#                 routes_valid_update.append(route_update)
#         routes_valid = routes_valid_update
        
#         print(f'after step {step}, there are {len(routes_valid)} valid routes.')
        
#     n_routes = len(routes_valid)
    
#     return n_routes


# STILL MEMORY INTENSIVE
# hangs after step 25
# store latest points only
# def solution(n, verbose=True):
#     n_routes = 0
#     p = [0,0]
#     # routes_valid = [[p]]
#     p_prevs_valid = [p]
#     n_steps = 2 * n
#     print('steps to take:', n_steps)
#     for step in range(1, n_steps+1):
#         if verbose:
#             print('step', step)
#         # routes_valid_update = []
#         p_prevs_valid_update = []
#         for p_prev in p_prevs_valid:
#             # p_prev = route[-1]
#             if verbose:
#                 print('latest point =', p_prev)
#             if p_prev[0] < n:
#                 # go right
#                 new_p = [p_prev[0] + 1, p_prev[1]]
#                 # if p_go_right[0] <= n and p_go_right[1] <= n:
#                 # route_update = route + [new_p]
#                 p_prevs_valid_update.append(new_p)
#                 if verbose:
#                     print('right is valid route')
#                     # print(route_update)
#                 # routes_valid_update.append(route_update)
#             if p_prev[1] < n:
#                 # go down
#                 new_p = [p_prev[0], p_prev[1] + 1]
#                 # if p_go_down[0] <= n and p_go_down[1] <= n:
#                 # route_update = route + [new_p]
#                 p_prevs_valid_update.append(new_p)
#                 if verbose:
#                     print('down is valid route')
#                     # print(route_update)
#                 # routes_valid_update.append(route_update)
#         # routes_valid = routes_valid_update
#         p_prevs_valid = p_prevs_valid_update
        
#         print(f'after step {step}, there are {len(p_prevs_valid)} valid routes.')
        
#     n_routes = len(p_prevs_valid)
    
#     return n_routes


# # store latest points only, using generator instead of list
# def solution(n, verbose=False):
#     # n_routes = 0
#     n_branches = 1
#     p = [0,0]
#     # routes_valid = [[p]]
#     p_prevs_valid = [p]
#     n_steps = 2 * n
#     print('steps to take:', n_steps)
#     for step in range(1, n_steps+1):
#         # n_branches = 0
#         if verbose:
#             print('step', step)
#         # routes_valid_update = []
#         p_prevs_valid_update = iter(())
#         for p_prev in p_prevs_valid:
#             # p_prev = route[-1]
#             if verbose:
#                 print('latest point =', p_prev)
#             # if both right and down are possible, add +1 to n_branches
#             if p_prev[0] < n and p_prev[1] < n:
#                 n_branches += 1
#             if p_prev[0] < n:
#                 # go right
#                 new_p = [p_prev[0] + 1, p_prev[1]]
#                 # n_branches += 1
#                 # if p_go_right[0] <= n and p_go_right[1] <= n:
#                 # route_update = route + [new_p]
#                 # p_prevs_valid_update.append(new_p)
#                 p_prevs_valid_update = chain(p_prevs_valid_update, [new_p])
#                 if verbose:
#                     print('right is valid route')
#                     # print(p_prevs_valid_update)
#                 # routes_valid_update.append(route_update)
#             if p_prev[1] < n:
#                 # go down
#                 new_p = [p_prev[0], p_prev[1] + 1]
#                 # n_branches += 1
#                 # if p_go_down[0] <= n and p_go_down[1] <= n:
#                 # route_update = route + [new_p]
#                 # p_prevs_valid_update.append(new_p)
#                 p_prevs_valid_update = chain(p_prevs_valid_update, [new_p])
#                 if verbose:
#                     print('down is valid route')
#                     # print(p_prevs_valid_update)
#                 # routes_valid_update.append(route_update)
#         # routes_valid = routes_valid_update
#         p_prevs_valid = iter(p_prevs_valid_update)
#         # p_prevs_valid = iter(set(tuple(p) for p in p_prevs_valid_update))
#         print(f'after step {step} there are {n_branches} valid branchs')
#         if verbose:
#             print('-' * 20)
#         if step == n_steps:
#             n_routes = n_branches
#         # print(f'after step {step}, there are {len(p_prevs_valid)} valid routes.')
        
#     # n_routes = len(p_prevs_valid)
    
#     return n_routes


# after long struggle, came to realization
def solution(n):
    # it is a permutation of downs and rights
    # e.g. 2x2: ddrr, drdr, rrdd
    n_routes = int(factorial(2*n) / (factorial(n) * factorial(n)))
    return n_routes


def report(n):
    print(f'there are {solution(n)} routes to move from top left to bottom right of {n}x{n} grid.')    

    
def main():
    tic = time()
    
    # report(2, verbose=True)
    report(2)
    # 6
    
    # projecteuler number:
    # report(20, verbose=False)
    report(20)
    
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()