# 2020-12-27 14:54:02

# ONGOING 

# project euler: https://projecteuler.net
# problem 51: Prime digit replacements

from time import time
from itertools import combinations

from prob3 import is_prime
from prob35 import num_to_digitlist, digitlist_to_num


def get_min_max(len_n):
    n_min = 10 ** (len_n-1)
    n_max = 10 ** (len_n) - 1
    return n_min, n_max

    
def solution(n_fam, verbose=False):
    len_n = 2
    while True:
        n_min, n_max = get_min_max(len_n)
        
        possible_n_replaces = range(1, len_n)

        # print(n_min, n_max)
        primes = []
        for n in range(n_min+1, n_max+1):
            if is_prime(n):
                primes.append(n)
        if len(primes) == 0:
            len_n += 1
            continue
        for p in primes:
            # p_digitlist = num_to_digitlist(p)
            for nr in possible_n_replaces:
                poss_nr_idxs = list(combinations(range(len_n), nr))
                
                for nr_idxs in poss_nr_idxs:
                    if verbose:
                        print('index/indices to replace:', nr_idxs)
                    if 0 in nr_idxs:
                        r_digits = range(1, 10)
                    else:
                        r_digits = range(0, 10)
                    
                    prime_family = []
                    
                    for r in r_digits:
                        p_replist = num_to_digitlist(p)
                        for nr_idx in nr_idxs:     
                            # print(nr_idx, r)
                            p_replist[nr_idx] = r
                        p_rep_num = digitlist_to_num(p_replist)
                        if is_prime(p_rep_num):
                            prime_family.append(p_rep_num)
                    if verbose:
                        print(p, prime_family)
                    if len(prime_family) == n_fam:
                        # print(prime_family)
                        return min(prime_family)
        len_n += 1
        

def report(n_fam, verbose=False):
    print(
        (
            f"smallest prime in the {n_fam}-prime family "
            f"is {solution(n_fam, verbose=verbose)}"
        )
    )


def main():
    tic = time()

    report(6, verbose=True)
    # 13

    report(7, verbose=False)
    # 56003
    
    # projecteuler number:
    report(8, verbose=False)
    # 121313

    toc = time()

    print("time used:", toc - tic)


if __name__ == "__main__":
    main()
