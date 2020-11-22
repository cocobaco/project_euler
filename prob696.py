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
from itertools import chain
# from itertools import tee
import pandas as pd


def find_all_pungs(tiles):
    '''same suit and same number'''
    trips = []
    counter = Counter(tiles)
    for k, v in counter.items():
        if v >= 3:
            trips.append([k] * 3)
            
    return trips


def find_all_pungs2(tiles):
    '''same suit and same number'''

    counter = Counter(tiles)
    
    count = 0
    trips = iter([])
    
    for i, (k, v) in enumerate(counter.items()):
        if v >= 3:
            # trips.append([k] * 3)
            three_tiles = [k] * 3
            if count == 0:
                trips = chain(iter([three_tiles]))
            else:
                trips = chain(trips, iter([three_tiles]))
            count += 1
    
    # print('type check pung trips:', type(trips))
    return trips


def gen_remain_suits(tiles):
    suits = set((tile[0] for tile in tiles))
    return iter(suits)
            
            
def find_all_chows(tiles):
    '''same suit and 3 consecutive numbers'''
    trips = []
    
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


def find_all_chows2(tiles):
    '''same suit and 3 consecutive numbers'''
    trips = iter([])
    
    remaining_suits = gen_remain_suits(tiles)
    
    # go through each remaining suit
    for i, s in enumerate(remaining_suits):
        s_chows = []
        # s_chows = iter([])
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
                # s_chows = chain(s_chows, chow)
                # if chow not in s_chows:
                #     # print('new chow:', chow)
                #     s_chows.append(chow)
                    # for tile in chow:
                    #     rem_tiles.remove(tile)
                # print('updated remain tiles:', rem_tiles)
        # trips.extend(s_chows)
        if i == 0:
            trips = chain(iter(s_chows))
        else:
            trips = chain(trips, iter(s_chows))
    
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
    

def find_pairs2(n, s):
    pairs = iter([(i,j)] * 2 for i in range(1, s+1) for j in range(1, n+1))    
    return pairs


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


def remove_dupes_lol_pd(lol):
    # remove duplicated lists in list of lists
    # https://stackoverflow.com/a/52452368/5421647
    lol_s = [sorted(l) for l in lol]
    s = pd.Series(list(map(tuple, lol_s)))
    unique = s[~s.duplicated(keep='first')].tolist()
    unique = [list(l) for l in unique]
    return unique


def remove_dupes_lol_counter(lol):
    # remove duplicated lists in list of lists
    # https://stackoverflow.com/a/52452336/5421647
    lol_s = [sorted(l) for l in lol]
    ct = Counter(map(tuple, lol_s))
    unique = [list(l) for l in list(ct.keys())]
    return unique


def remove_dupes_lol_counter2(lol):
    # remove duplicated lists in list of lists
    # https://stackoverflow.com/a/52452336/5421647
    # print('type check lol:', type(lol))
    # for l in lol:
    #     print(l)
    #     print(sorted(l))
    lol_s = iter([sorted(l) for l in lol])
    ct = Counter(map(tuple, lol_s))
    unique = iter([list(l) for l in list(ct.keys())])
    return unique


def get_remain_tiles(wh, all_tiles):
    remain_tiles = all_tiles.copy()
            
    # print('wh:', wh)
    for tile in wh:
        # print('current remaining tiles:', remain_tiles)
        # print('removing', tile)
        
        remain_tiles.remove(tile)
    
    return iter(remain_tiles)


def get_n_trips(n, whs, all_tiles, kind='pung', verbose=True):
    '''get possible triples (pung or chow)'''
    whs_updated = whs.copy()
    for ni in range(n):
        if verbose:
            print(f'finding {ni+1}-th {kind}...')
        new_whs = []
        for wh in whs_updated:
            wh_extend = []  # extend each hand
            
            remain_tiles = get_remain_tiles(wh, all_tiles)

            if verbose:
                print('-' * 20)
                print('hand so far:', wh)
                # print('remaining tiles:', remain_tiles)
                
            if kind == 'pung':
                trips = find_all_pungs(remain_tiles)
            elif kind == 'chow':
                trips = find_all_chows(remain_tiles)
                
            # if verbose:
            #     print(f'{kind} trips:', trips)
            for trip in trips:
                new_wh = wh + trip
                # print(new_wh)
                if verbose:
                    print('new hand:', new_wh)
                wh_extend.append(new_wh)
                # if new_wh not in new_whs:
                new_whs.extend(wh_extend)
                    # whs.append(new_wh)

        # whs_updated = remove_dupes_lol(new_whs)
        # whs_updated = remove_dupes_lol_pd(new_whs)
        whs_updated = remove_dupes_lol_counter(new_whs)
        
    return whs_updated


# STILL SLOW
def get_n_trips2(n, whs, all_tiles, kind='pung', verbose=True):
    '''get possible triples (pung or chow)'''
    # print('check type whs:', type(whs), kind)
    whs_updated = iter(whs)
    
    for ni in range(n):
        if verbose:
            print(f'finding {ni+1}-th {kind}...')
            
        new_whs = []
        # new_whs = iter([])
        
        for wh in whs_updated:
        # for wh in whs:
            # print('wh:', wh)
            wh_extend = []  # extend each hand
            # wh_extend = iter([])
            
            remain_tiles = get_remain_tiles(wh, all_tiles)

            if verbose:
                print('-' * 20)
                print('hand so far:', wh)
                # print('remaining tiles:', remain_tiles)
                
            if kind == 'pung':
                trips = find_all_pungs2(remain_tiles)
            elif kind == 'chow':
                trips = find_all_chows2(remain_tiles)
                
            # print('trips:', list(trips))
            
            # if verbose:
            #     print(f'{kind} trips:', trips)
            for i, trip in enumerate(trips):
                # print(i, wh, list(trip))
                new_wh = wh + list(trip)
                # print(i, new_wh)
                if verbose:
                    print('new hand:', new_wh)
                wh_extend.append(new_wh)
                # print('length wh_extend:', len(wh_extend))
                new_whs.extend(wh_extend)
                # new_whs = chain(new_whs, iter(wh_extend))
                # print(i) 
                # if i == 0:
                #     # print('new_wh:', new_wh)
                #     # wh_extend = iter([new_wh])
                #     # wh_extend = iter(new_wh)
                #     # new_whs = chain(wh_extend)
                #     new_whs = chain(iter(wh_extend))
                # else:
                #     # wh_extend = chain(wh_extend, [new_wh])
                #     # wh_extend = chain(wh_extend, iter(new_wh))
                #     # new_whs = chain(new_whs, iter([new_wh]))
                #     new_whs = chain(new_whs, iter(wh_extend))

        # whs_updated = remove_dupes_lol(new_whs)
        # whs_updated = remove_dupes_lol_pd(new_whs)
        whs_updated = remove_dupes_lol_counter2(new_whs)
        
    return whs_updated


def trip_loop(pairs, all_tiles, t, verbose=True):
    final_whs = []
    
    for n_pungs in range(0, t+1):
        n_chows = t - n_pungs
        
        whs_updated = pairs.copy()
        
        if verbose:
            print('*' * 20)
            print(f'*** {n_pungs} pungs + {n_chows} chows ***')
                
        # pung loops
        if n_pungs > 0:
            whs_updated = get_n_trips(n_pungs, whs_updated, all_tiles, 
                                      kind='pung', verbose=verbose)
        # elif n_chows > 0:
        #     whs_updated = get_n_trips(n_pungs, pairs, all_tiles, 
        #                               kind='chow', verbose=verbose)
        # chow loops
        if n_chows > 0:
            whs_updated = get_n_trips(n_chows, whs_updated, all_tiles, 
                                      kind='chow', verbose=verbose)

        # add complete whs (for each pungs/chows combo) to final_whs
        final_whs.extend(whs_updated)
        
    # final_whs = remove_dupes_lol(final_whs)
    # final_whs = remove_dupes_lol_pd(final_whs)
    final_whs = remove_dupes_lol_counter(final_whs)
    
    return final_whs


def trip_loop2(n, s, t, verbose=True):
    # whs_updated = iter(pairs)
    # whs_updated = pairs
    
    all_tiles = build_tiles(n, s)
    
    # t1 = time()
    for n_chows in range(0, t+1):
        n_pungs = t - n_chows
        
        # whs_updated = iter(pairs)  # This gives wrong result
        # https://stackoverflow.com/a/42132767/5421647
        # pairs, whs_updated = tee(pairs)
        
        whs_updated = find_pairs(n, s)
        
        if verbose:
            print('*' * 20)
            print(f'*** {n_pungs} pungs + {n_chows} chows ***')
        
        # pung loops
        if n_pungs > 0:
            whs_updated = get_n_trips2(n_pungs, whs_updated, all_tiles, 
                                        kind='pung', verbose=verbose)

        # chow loops
        if n_chows > 0:
            whs_updated = get_n_trips2(n_chows, whs_updated, all_tiles, 
                                        kind='chow', verbose=verbose)

        # final_whs.extend(whs_updated)
        if n_chows == 0:
            final_whs = chain(iter(whs_updated))
        else:
            final_whs = chain(final_whs, iter(whs_updated))
      
    # t2 = time()
    # print('t trip_loop2:', t2-t1)
            
   
    # final_whs = remove_dupes_lol(final_whs)
    # final_whs = remove_dupes_lol_pd(final_whs)
    final_whs = remove_dupes_lol_counter2(final_whs)
  
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


# GIVE CORRECT RESULT BUT SLOW and MEMORY INTENSIVE
def solution(n, s, t, verbose=True):
    print('=' * 30)
    '''using list'''
    num_mod = 1000000007
    
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
        
    len_final_whs = len(final_whs)
    
    if len_final_whs == 0:
        print('No winning hand possible!')
            
    num_whs = len_final_whs % num_mod
    
    return num_whs


def solution2(n, s, t, verbose=True):
    print('=' * 30)
    # using generator instead of list
    num_mod = 1000000007
    
    num_tiles_hand = 2 + 3 * t
    num_tiles_total = n * s * 4
    
    if verbose:
        print(f'{s} suits, 1-{n}')
        print('tiles in hand:', num_tiles_hand)
        print('tiles total:', num_tiles_total)
    
    # all_tiles = build_tiles(n, s)
    # # pairs = find_pairs(n, s)
    # pairs = find_pairs2(n, s)
        
    # if verbose:                
    #     print('winning hands starter (a pair):', pairs)
        
    # final_whs = trip_loop(pairs, all_tiles, t, verbose=verbose)  
    # final_whs = trip_loop2(pairs, all_tiles, t, verbose=verbose)
    final_whs = trip_loop2(n, s, t, verbose=verbose)
    
    # if verbose:
    #     print('-' * 20)
    #     print('final winning hands:')
    #     for i, wh in enumerate(final_whs):
    #         print(f'{i+1}: {wh}')
        
    len_final_whs = sum(1 for _ in final_whs)
    
    if len_final_whs == 0:
        print('No winning hand possible!')
        
    num_whs = len_final_whs % num_mod
        
    return num_whs


def report(n, s, t, verbose=True):
    print((f'number of distinct winning hands for n={n}, s={s}, t={t} '
            f'is {solution(n, s, t, verbose)} (mod 1000000007)'))
            # f'is {solution2(n, s, t, verbose)} (mod 1000000007)'))


def main():
    tic = time()
    
    report(2, 1, 1, verbose=True)  # minimum possible deck
    # report(2, 1, 1, verbose=False)  # minimum possible deck
    # 2
    
    report(4, 1, 1, verbose=False)
    # 20
    
    report(3, 1, 2, verbose=False)
    # 12
    
    report(7, 2, 2, verbose=False)
    # 3666
    
    report(9, 1, 4, verbose=False)
    # 13259
    
    report(10, 1, 4, verbose=False)
    # 
    
    # projecteuler number:
    # report(10**8, 10**8, 30, verbose=False)
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()