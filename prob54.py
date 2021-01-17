# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:06:49 2021

@author: rop
"""

# project euler: https://projecteuler.net
# problem 54: poker hands

from time import time
from collections import Counter
import operator
import pandas as pd


write_output = False
verbose = False


def read_2hands(s):
    cards = s.split(' ')
    h1 = cards[:5]
    h2 = cards[5:]
    return h1, h2


def handCharacteristics(cards):
    
    hands_rank = {1: 'straight flush', 2: 'quad', 3: 'full house', 
                  4: 'flush', 5: 'straight', 6: 'triple', 
                  7: 'two pairs', 8: 'pair', 9: 'high card'}


    ranks = [c[:-1] for c in cards]
    suits = [c[-1] for c in cards]
    
    # check flush
    count_suits = Counter(suits)
    if len(count_suits) == 1:
        flush_status = True
    else:
        flush_status = False
    
    # check straight
    ranks_values = [10 if r == 'T' else 11 if r == 'J' else 12 if r == 'Q' \
                    else 13 if r == 'K' else 14 if r == 'A' \
                    else int(r) for r in ranks]
    ranks_values.sort(reverse=True)
    
    count_vals = Counter(ranks_values)
    cards_sorted_by_count = sorted(count_vals.items(), 
                                   key=operator.itemgetter(1), 
                                   reverse=True)
        
    if ranks_values == list(reversed(range(min(ranks_values), 
                                           max(ranks_values)+1))):
        straight_status = True
    else:
        straight_status = False
        
    if flush_status and straight_status:  # straight flush
        hand_rank = 1
        key_card = cards_sorted_by_count[0][0]
    elif flush_status:  # flush
        hand_rank = 4
        key_card = cards_sorted_by_count[0][0]
    elif straight_status:  # straight
        hand_rank = 5
        key_card = cards_sorted_by_count[0][0]
    else:
        count_ranks = Counter(ranks)     
        num_same = count_ranks.values()
        num_same_sorted = sorted(num_same, reverse=True)
        if num_same_sorted == [4, 1]:  # quad
            hand_rank = 2
            key_card = cards_sorted_by_count[0][0]
        elif num_same_sorted == [3, 2]:  # full house
            hand_rank = 3
            key_card = cards_sorted_by_count[0][0]
        elif num_same_sorted == [3, 1, 1]:  # triple
            hand_rank = 6
            key_card = cards_sorted_by_count[0][0]
        elif num_same_sorted == [2, 2, 1]:  # 2 pairs
            hand_rank = 7
            key_card = cards_sorted_by_count[0][0]
            key_card2 = (cards_sorted_by_count[1][0], 
                         cards_sorted_by_count[2][0])
        elif num_same_sorted == [2, 1, 1, 1]:  # pair
            hand_rank = 8
            key_card = cards_sorted_by_count[0][0]
        else:
            hand_rank = 9  # high card
            key_card = cards_sorted_by_count[0][0]
            
    hand_type = hands_rank[hand_rank]
    
    # if two pairs tie at first key card, check 2nd key card and the 5th card
    if hand_rank == 7:  
        key_card2 = key_card2
    # for other hand types, check the remain cards by using full rank values
    else:
        key_card2 = None
        
    return hand_rank, hand_type, ranks_values, key_card, key_card2
    

def player1_wins(h1_rank, h1_type, h1_rankvals, h1_key1, h1_key2, 
                 h2_rank, h2_type, h2_rankvals, h2_key1, h2_key2):

    if h1_rank < h2_rank:
        return True
    elif h1_rank > h2_rank:
        return False
    elif h1_rank == 7:
        # 2 pairs. check first keycard, then 2nd key card, then the 5th card
        if (h1_key1, h1_key2) > (h2_key1, h2_key2):
            return True
        else:
            return False
    elif h1_rank in [6, 8]:
        # one pair/triple: check first keycard, then rankvals
        if (h1_key1, h1_rankvals) > (h2_key1, h2_rankvals):
            return True
        else:
            return False
    else:
        # anything else, check rankvals
        if h1_rankvals > h2_rankvals:
            return True
        else:
            return False
    
    
def solution(verbose=False):
    
    file = 'data/p054_poker.txt'
    
    with open(file, 'r') as f:
        text = f.readlines()
        
#    print(text)
    
    deals = [t.strip() for t in text]
    
    p1_wins = 0
    p2_wins = 0
    
    df = pd.DataFrame(columns=['h1', 'h2', 'h1_type', 'h2_type', 'winner'])
    
    for i, deal in enumerate(deals):
        h1, h2 = read_2hands(deal)
        
        h1_rank, h1_type, h1_rankvals, h1_key1, h1_key2 = handCharacteristics(h1)
        h2_rank, h2_type, h2_rankvals, h2_key1, h2_key2 = handCharacteristics(h2)
        

        if player1_wins(h1_rank, h1_type, h1_rankvals, h1_key1, h1_key2, 
                        h2_rank, h2_type, h2_rankvals, h2_key1, h2_key2):
            winner = 'p1'
            p1_wins += 1
        else:
            winner = 'p2'
            p2_wins += 1
            
        if verbose:
            print('-' * 20)
            print(f'deal #{i+1}: {h1} vs {h2}. {winner} wins.')
        
        data = {'h1': h1, 'h2': h2, 'h1_type': h1_type, 'h2_type': h2_type, 
                'winner': winner}
        # print(data)
        
        # build dataframe row by row
        if pd.isna(df.index.max()):
            nextloc = 1
        else:
            nextloc = df.index.max() + 1
        # print('writing loc', nextloc)
        df.loc[nextloc] = data
        # df = df.append(data, ignore_index=True)
        # df = pd.concat([df, data], ignore_index=True)
        
    print(df.head())
    print(df['winner'].value_counts())
    
    if write_output:
        fout = 'output/prob54.xlsx'
        df.to_excel(fout)
        print('-' * 20)
        print(fout, 'saved')
        
    return p1_wins


def report(verbose=verbose):
    print(('the number of wins by player 1 is '
           f'is {solution(verbose=verbose)}'))


def main():
    tic = time()
    
    # projecteuler number:
    report()
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()