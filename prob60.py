# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 18:28:04 2021

@author: rop
"""


# project euler: https://projecteuler.net
# problem 60: prime pair sets

from time import time
from itertools import combinations

from prob3 import is_prime


def sieve(n):
    """Sieve of Erotosthenes: generate prime numbers less than n"""
    # https://radiusofcircle.blogspot.com/2016/10/problem-60-project-euler-solution-with.html
    prime_check = [True] * n
    prime_check[0] = False
    prime_check[1] = False
    prime_check[2] = True
    # print(prime_check)

    # even numbers except 2 have been eliminated
    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while index < n:
            # print("marking", index, "as not prime")
            prime_check[index] = False
            index = index + i
    # print(prime_check)

    # 2 is smallest prime
    primes = [2]
    # going through each odd number
    for i in range(3, n, 2):
        if prime_check[i]:
            primes.append(i)
    return primes


def concat_nums(n1, n2):
    ans = [int(str(n1) + str(n2)), int(str(n2) + str(n1))]
    return ans


def possible_pairs(nums):
    pairs = []
    for n in nums:
        for r in nums:
            if r != n:
                concats = concat_nums(n, r)
                for c in concats:
                    if c not in pairs:
                        pairs.append(c)
    return pairs


def check_all_prime(nums):
    for n in nums:
        if not is_prime(n):
            return False
    return True


# def solution5b(num, nmax=10000):
#     primes_all = sieve(nmax)

#     for a in primes_all:
#         primes = []
#         for b in primes_all:
#             if b <= a:
#                 continue
#             pairs = possible_pairs([a, b])
#             if check_all_prime(pairs):
#                 primes.append(a)
#                 primes.append(b)
#                 while len(primes) < num:
#                     for next_prime in primes_all:
#                         if next_prime <= primes[-1]:
#                             continue
#                         current = primes.copy()
#                         pairs = []
#                         for x in current:
#                             pairs += possible_pairs([x, next_prime])
#                         # pairs = possible_pairs([a, c]) + possible_pairs([b, c])
#                         if check_all_prime(pairs):
#                             primes.append(next_prime)

#                 print(primes)
#                 return sum(primes)


def solution5(nmax=10000):
    # brute force 5 prime numbers

    primes_all = sieve(nmax)

    for a in primes_all:
        primes = [a]
        for b in primes_all:
            if b <= a:
                continue
            pairs = possible_pairs([a, b])
            if check_all_prime(pairs):
                primes = [a, b]
                for c in primes_all:
                    if c <= b:
                        continue
                    current = primes.copy()
                    pairs = []
                    for x in current:
                        pairs += possible_pairs([x, c])
                    # pairs = possible_pairs([a, c]) + possible_pairs([b, c])
                    if check_all_prime(pairs):
                        primes = [a, b, c]
                        for d in primes_all:
                            if d <= c:
                                continue
                            current = primes.copy()
                            pairs = []
                            for x in current:
                                pairs += possible_pairs([x, d])
                            if check_all_prime(pairs):
                                primes = [a, b, c, d]
                                for e in primes_all:
                                    if e <= d:
                                        continue
                                    current = primes.copy()
                                    pairs = []
                                    for x in current:
                                        pairs += possible_pairs([x, e])
                                    if check_all_prime(pairs):
                                        primes = [a, b, c, d, e]
                                        print(primes)
                                        return sum(primes)


def solution(num, nmax=10000, verbose=True):
    primes_all = sieve(nmax)

    # combis = comb(primes_all, num)
    combis = combinations(primes_all, num)

    # print(f"{len(combis)} combinations found")

    min_sum = None
    min_combi = None

    for combi in combis:
        if (min_sum is not None) and (sum(combi) > min_sum):
            # continue
            break

        pairs = possible_pairs(combi)

        if check_all_prime(pairs):
            print("found valid combi:", combi)
            summ = sum(combi)
            if (min_sum is None) or (summ < min_sum):
                min_sum = summ
                min_combi = combi

    print("answer:")
    if min_sum is not None:
        print(min_combi)
        return min_sum
    else:
        print(f"valid combinations not found under {nmax}")
        return None


# def solution(num, nmax=10000, verbose=True):
#     print(f"finding {num} primes...")
#     # primes = [3, 7, 109, 673]

#     # prime_test = 9

#     # while len(primes) < num:
#     #     primes_test = primes + [prime_test]
#     #     print('testing', primes_test)
#     #     pairs = possible_pairs(primes_test)
#     #     for p in pairs:
#     #         if not is_prime(p):
#     #             print(p, 'is not prime')
#     #             prime_test += 2
#     #             while (not is_prime(prime_test)) or (prime_test in primes):
#     #                 prime_test +=2
#     #             break

#     # primes = primes_test

#     # # initialize
#     primes = [3, 7]

#     # next_prime = 11

#     primes_all = sieve(nmax)

#     primes_to_check = [n for n in primes_all if n > primes[-1]]

#     for next_prime in primes_to_check:
#         # while True:
#         #     if next_prime > nmax:
#         #         print(f"getting over {nmax}. quitting.")
#         #         return None

#         #     if verbose:
#         #         print("testing", next_prime)
#         primes.append(next_prime)
#         pairs = possible_pairs(primes)
#         # if verbose:
#         #     print(pairs)
#         for p in pairs:
#             if not is_prime(p):
#                 # if verbose:
#                 #     print(next_prime, 'doesn\'t work')
#                 primes.remove(next_prime)
#                 # primes_test = primes
#                 next_prime += 2
#                 while not is_prime(next_prime):
#                     next_prime += 2
#                 break

#         if len(primes) == num:
#             break
#         # else:
#         #     next_prime += 2
#         #     while not is_prime(next_prime):
#         #         next_prime += 2

#     if len(primes) < num:
#         print(f"have not found enough primes under {nmax}")
#         return None

#     print(f"set of {num} primes: {primes}")
#     summ = sum(primes)
#     return summ


def report(num, nmax=10000):
    print(
        (
            f"lowest sum for a set of {num} primes for which any two primes concatenate to produce another prime "
            f"is {solution(num, nmax=nmax)}"
        )
    )


def main():
    tic = time()

    report(4, nmax=1000)
    # 792

    # projecteuler number:
    # report(5, nmax=10000)
    print(solution5(nmax=10000))
    #

    toc = time()

    print("time used:", toc - tic)


if __name__ == "__main__":
    main()