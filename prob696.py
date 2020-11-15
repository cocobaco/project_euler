# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:02:38 2020

@author: PC1
"""

# project euler: https://projecteuler.net
# problem 696: Mahjong

# ONGOING


from time import time
# from math import factorial
from collections import Counter
from itertools import groupby


def find_all_pungs(tiles):
    '''same suit and same number'''
    trips = []
    
    counter = Counter(tiles)
    
    for k, v in counter.items():
        if v >= 3:
            trips.append([k] * 3)
            
    return trips


def find_all_chows(tiles):
    '''same suit and 3 consecutive numbers'''
    trips = []
    remaining_suits = []
    
    for tile in tiles:
        s = tile[0]
        if s not in remaining_suits:
            remaining_suits.append(s)
    
    # print('remaining suits:', remaining_suits)
    # rem_tiles = tiles.copy()
    # print('remain tiles:', rem_tiles)
    
    # go through each remaining suit
    for s in remaining_suits:
        # print('checking suit', s)
        s_chows = []
        # tiles_s = [tile for tile in rem_tiles if tile[0]==s]
        tiles_s = [tile for tile in tiles if tile[0]==s]
        nums = [tile[1] for tile in tiles_s]
        # print(s, nums)
        for n in set(nums):
            if all(x in nums for x in [n, n+1, n+2]):
                chow = [(s,n), (s,n+1), (s,n+2)]
                if chow not in s_chows:
                    # print('new chow:', chow)
                    s_chows.append(chow)
                    # for tile in chow:
                    #     rem_tiles.remove(tile)
                # print('updated remain tiles:', rem_tiles)
        trips.extend(s_chows)
    
    return trips


def find_pairs(n, s):
    pairs = []
    # initiate with a pair
    for i in range(1, s+1):
        for j in range(1, n+1):
            tile = (i, j)
            if tile not in pairs:
                pairs.append([tile, tile])
    return pairs
    

def remove_dupes_lol(lol):
    # remove duplicated lists in list of lists
    lol.sort()
    new_lol = list(lol for lol,_ in groupby(lol))
    return new_lol


def trip_loop(whs, all_tiles, t, verbose=True):
    
    final_whs = []
    initial_whs = whs.copy()
    
    if verbose:
        # find possible n_pungs/n_chows combination:
        print('going through each n_pungs, n_chows combination:')
    
    for n_pungs in range(0, t+1):
        
        n_chows = t - n_pungs
        if verbose:
            print('*' * 20)
            print(f'*** {n_pungs} pungs + {n_chows} chows ***')
        
        whs = initial_whs.copy()
        # new_whs = []
        
        # pung loops
        if n_pungs > 0:
            for _ in range(n_pungs):
                new_whs = []
                for wh in whs:
                    wh_extend = []  # extend each winning hand
                    # new_whs = whs
                    if verbose:
                        print('-' * 20)
                        print('hand so far:', wh)
                    remain_tiles = all_tiles.copy()
                    for tile in wh:
                        remain_tiles.remove(tile)
                    if verbose:
                        print('remaining tiles:', remain_tiles)
                    trips_pung = find_all_pungs(remain_tiles)
                    if verbose:
                        print('pung trips:', trips_pung)
                    # for trip in trips_pung:
                    for trip in trips_pung:
                        new_wh = wh + trip
                        if verbose:
                            print('new hand:', new_wh)
                        wh_extend.append(new_wh)
                        if new_wh not in new_whs:
                            new_whs.extend(wh_extend)
                            # whs.append(new_wh)
                whs = new_whs
                # whs = list(k for k,_ in groupby(sorted(whs)))
                whs = remove_dupes_lol(whs)
                
        # chow loops
        if n_chows > 0:
            for _ in range(n_chows):
                new_whs = []
                for wh in whs:
                    wh_extend = []
                    # new_whs = whs
                    if verbose:
                        print('-' * 20)
                        print('hand so far:', wh)
                    remain_tiles = all_tiles.copy()
                    for tile in wh:
                        remain_tiles.remove(tile)
                    if verbose:
                        print('remaining tiles:', remain_tiles)
                    trips_chow = find_all_chows(remain_tiles)
                    if verbose:
                        print('chow trips:', trips_chow)
                    for trip in trips_chow:
                        new_wh = wh + trip
                        if verbose:
                            print('new hand:', new_wh)
                        wh_extend.append(new_wh)
                        if new_wh not in new_whs:
                            new_whs.extend(wh_extend)
                whs = new_whs
                # whs = list(k for k,_ in groupby(sorted(whs)))
                whs = remove_dupes_lol(whs)
                
    # remove duplicates from list of lists
    # https://stackoverflow.com/a/2213973/5421647
    # whs = list(k for k,_ in groupby(sorted(whs)))
        
        final_whs.extend(whs)
        
    # final_whs = list(k for k,_ in groupby(sorted(final_whs)))
    final_whs = remove_dupes_lol(final_whs)
        
        # num_tiles_hand = 2 + 3 * t
        # for wh in whs:
        #     if len(wh) == num_tiles_hand:
        #         final_whs.append(wh)
    
    return final_whs


def build_tiles(n, s):
    all_tiles = []
    
    for i in range(1, s+1):
        for j in range(1, n+1):
            # print(i, j)
            tiles = [(i, j)] * 4
            # print(tiles)
            all_tiles.extend(tiles)
    return all_tiles    
    
    
def solution(n, s, t, verbose=True):
    
    num_tiles_hand = 2 + 3 * t
    num_tiles_total = n * s * 4
    
    if verbose:
        print(f'{s} suits, 1-{n}')
        print('tiles in hand:', num_tiles_hand)
        print('tiles total:', num_tiles_total)
    
    # all_tiles = []
    
    # for i in range(1, s+1):
    #     for j in range(1, n+1):
    #         # print(i, j)
    #         tiles = [(i, j)] * 4
    #         # print(tiles)
    #         all_tiles.extend(tiles)
    
    all_tiles = build_tiles(n, s)
    
    
    # find number of 3t + 2 tiles collection
    # n: number: 1, 2, 3, ... n
    # s: suits: s1, s2, s3, ...
    # 1: pick a pair: pick a number, and pick a suite
    # num_possible_pairs = n * s
    
    # whs = []
    # # initiate with a pair
    # for i in range(1, s+1):
    #     for j in range(1, n+1):
    #         tile = (i, j)
    #         if tile not in whs:
    #             if verbose:
    #                 print('pair:', tile, tile)
    #             whs.append([tile, tile])
    #             # whs.append(tile)
                
    pairs = find_pairs(n, s)
    
    if verbose:                
        print('winning hands starter (a pair):', pairs)
        # for wh in whs:
        #     print(wh)
        
    # find accompanying triples (pungs/chows)
    # n_pung_range = range(t)
    # n_chow_range = range(t)
    
    final_whs = trip_loop(pairs, all_tiles, t, verbose=verbose)

    
    # find possible n_pungs/n_chows combination:
    # print('n_pungs, n_chows combinations:')
    # for n_pungs in range(0, t+1):
    #     n_chows = t - n_pungs
    #     print(n_pungs, n_chows)

    # for k in range(t):
    #     new_whs = []
    #     for wh in whs:
    #         wh_extend = []
    #         # new_whs = whs
    #         if verbose:
    #             print('-' * 20)
    #             print('hand so far:', wh)
    #         remain_tiles = all_tiles.copy()
    #         for tile in wh:
    #             remain_tiles.remove(tile)
    #         if verbose:
    #             print('remaining tiles:', remain_tiles)
    #         # trips_pung = find_all_pungs(remain_tiles)
    #         trips_chow = find_all_chows(remain_tiles)
    #         if verbose:
    #             # print('pung trips:', trips_pung)
    #             print('chow trips:', trips_chow)
    #         # for trip in trips_pung:
    #         for trip in trips_chow:
    #             new_wh = wh + trip
    #             if verbose:
    #                 print('new hand:', new_wh)
    #             wh_extend.append(new_wh)
    #             if new_wh not in new_whs:
    #                 new_whs.extend(wh_extend)
    #                 # whs.append(new_wh)
    #         # whs.remove(wh)
    #     whs = new_whs
    #     # remove duplicates from list of lists
    #     # https://stackoverflow.com/a/2213973/5421647
    #     whs = list(k for k,_ in groupby(sorted(whs)))
    #             # wh.extend(trip)
    #     # whs = new_whs
    # # whs = new_whs
    # # whs = list(set(whs))
    
    # if verbose:
    #     print('final winning hands:')
    #     for wh in whs:
    #         print(wh)
        
    if verbose:
        print('-' * 20)
        print('final winning hands:')
        for i, wh in enumerate(final_whs):
            print(f'{i+1}: {wh}')
        
    ans = len(final_whs)    
    return ans


def report(n, s, t, verbose=True):
    print((f'number of distinct winning hands for n={n}, s={s}, t={t} '
           f'is {solution(n, s, t, verbose)}'))


def main():
    tic = time()
    
    report(2, 1, 1, verbose=True)  # minimum possible deck
    # 2
    
    report(4, 1, 1, verbose=True)
    # 20
    
    # report(9, 1, 4, verbose=False)
    # 13259
    
    # projecteuler number:
    # report(10**8, 10**8, 30)
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()