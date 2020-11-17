# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 09:01:38 2020

@author: PC1
"""

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
# from itertools import groupby


def find_all_pungs(tiles):
    '''same suit and same number'''
    trips = []
    
    counter = Counter(tiles)
    
    for k, v in counter.items():
        if v >= 3:
            trips.append([k] * 3)
            
    return trips


def gen_remain_suits(tiles):
    suits = set((tile[0] for tile in tiles))
    return iter(suits)
            
            
def find_all_chows(tiles):
    '''same suit and 3 consecutive numbers'''
    trips = []
    # remaining_suits = []
    
    # for tile in tiles:
    #     s = tile[0]
    #     if s not in remaining_suits:
    #         remaining_suits.append(s)
    
    remaining_suits = gen_remain_suits(tiles)
    
    # go through each remaining suit
    for s in remaining_suits:
        s_chows = []
        # tiles_s = [tile for tile in rem_tiles if tile[0]==s]
        tiles_s = [tile for tile in tiles if tile[0]==s]
        # nums = iter(set((tile[1] for tile in tiles_s)))
        nums = set((tile[1] for tile in tiles_s))
        # print(s, nums)
        for n in nums:
            consecs = [n, n+1, n+2]
            if all(x in nums for x in consecs):
                chow = [(s,n), (s,n+1), (s,n+2)]
                s_chows.append(chow)
                # if chow not in s_chows:
                #     # print('new chow:', chow)
                #     s_chows.append(chow)
                    # for tile in chow:
                    #     rem_tiles.remove(tile)
                # print('updated remain tiles:', rem_tiles)
        trips.extend(s_chows)
    
    return trips


def find_pairs(n, s):
    # pairs = []
    # # initiate with a pair
    # for i in range(1, s+1):
    #     for j in range(1, n+1):
    #         tile = (i, j)
    #         pairs.append([tile] * 2)
    # pairs = ([(i,j)] * 2 for i in range(1, s+1) for j in range(1, n+1))
    pairs = [[(i,j)] * 2 for i in range(1, s+1) for j in range(1, n+1)]
    return pairs
    

# def gen_pairs(n, s):
#     pairs = []
#     # initiate with a pair
#     for i in range(1, s+1):
#         for j in range(1, n+1):
#             tile = (i, j)
#             pairs.append([tile] * 2)
#             yield [tile] * 2


def remove_dupes_lol(lol):
    # remove duplicated lists in list of lists
    # https://stackoverflow.com/a/2213973/5421647
    # https://stackoverflow.com/a/15353040/5421647
    # https://stackoverflow.com/a/44663976/5421647
    lol_s = [sorted(l) for l in lol]
    unique = []
    seen = set()
    for l in lol_s:
        lt = tuple(l)
        if lt not in seen:
            unique.append(l)
            seen.add(lt)
    # lol.sort()
    # new_lol = list(i for i,_ in groupby(lol_s))
    return unique


def get_remain_tiles(wh, all_tiles):
    remain_tiles = all_tiles.copy()
            
    for tile in wh:
        remain_tiles.remove(tile)
    
    return remain_tiles


def get_n_trips(n, whs, all_tiles, kind='pung', verbose=True):
    
    whs_updated = whs.copy()
    
    for i in range(n):
        if verbose:
            print(f'finding {i+1}-th {kind}...')
            
        new_whs = []
        
        for wh in whs_updated:
            wh_extend = []  # extend each winning hand
            
            remain_tiles = get_remain_tiles(wh, all_tiles)
            
            # remain_tiles = all_tiles.copy()
            
            # for tile in wh:
            #     remain_tiles.remove(tile)

            if verbose:
                print('-' * 20)
                print('hand so far:', wh)
                print('remaining tiles:', remain_tiles)
                
            if kind == 'pung':
                trips = find_all_pungs(remain_tiles)
            elif kind == 'chow':
                trips = find_all_chows(remain_tiles)
                
            if verbose:
                print(f'{kind} trips:', trips)
            # for trip in trips_pung:
            for trip in trips:
                new_wh = wh + trip
                if verbose:
                    print('new hand:', new_wh)
                wh_extend.append(new_wh)
                if new_wh not in new_whs:
                    new_whs.extend(wh_extend)
                    # whs.append(new_wh)

        whs_updated = remove_dupes_lol(new_whs)

    return whs_updated


def trip_loop(pairs, all_tiles, t, verbose=True):
    final_whs = []
    # initial_pairs = pairs.copy()

    for n_pungs in range(0, t+1):
        n_chows = t - n_pungs
        
        if verbose:
            print('*' * 20)
            print(f'*** {n_pungs} pungs + {n_chows} chows ***')
        
        # pairs = initial_pairs.copy()
        
        # pung loops
        whs_updated = get_n_trips(n_pungs, pairs, all_tiles, kind='pung', 
                                  verbose=verbose)
        # chow loops
        whs_updated = get_n_trips(n_chows, whs_updated, all_tiles, 
                                  kind='chow', verbose=verbose)

        # add complete whs (for each pungs/chows combo) to final_whs
        final_whs.extend(whs_updated)
        
    final_whs = remove_dupes_lol(final_whs)
        
        # num_tiles_hand = 2 + 3 * t
        # for wh in whs:
        #     if len(wh) == num_tiles_hand:
        #         final_whs.append(wh)
    
    return final_whs


def build_tiles(n, s):
    # all_tiles = []
    N_EACH = 4
    # for i in range(1, s+1):
    #     for j in range(1, n+1):
    #         # print(i, j)
    #         tiles = [(i, j)] * N_EACH
    #         # print(tiles)
    #         all_tiles.extend(tiles)
    all_tiles = [(i,j) for i in range(1, s+1) for j in range(1, n+1)] * N_EACH
    return all_tiles    
    
    
def solution(n, s, t, verbose=True):
    
    num_tiles_hand = 2 + 3 * t
    num_tiles_total = n * s * 4
    
    if verbose:
        print(f'{s} suits, 1-{n}')
        print('tiles in hand:', num_tiles_hand)
        print('tiles total:', num_tiles_total)
    
    all_tiles = build_tiles(n, s)
    
    pairs = find_pairs(n, s)
    
    if verbose:                
        print('winning hands starter (a pair):', pairs)
        
    final_whs = trip_loop(pairs, all_tiles, t, verbose=verbose)
        
    if verbose:
        print('-' * 20)
        print('final winning hands:')
        for i, wh in enumerate(final_whs):
            print(f'{i+1}: {wh}')
        
    num_whs = len(final_whs)
    if num_whs == 0:
        print('No winning hand possible!')
        
    return num_whs


def report(n, s, t, verbose=True):
    print((f'number of distinct winning hands for n={n}, s={s}, t={t} '
           f'is {solution(n, s, t, verbose)}'))


def main():
    tic = time()
    
    report(2, 1, 1, verbose=True)  # minimum possible deck
    # 2
    
    report(4, 1, 1, verbose=False)
    # 20
    
    report(3, 1, 2, verbose=False)
    # 12
    
    report(7, 2, 2, verbose=False)
    
    # report(9, 1, 4, verbose=False)
    # 13259
    
    # projecteuler number:
    # report(10**8, 10**8, 30)
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()