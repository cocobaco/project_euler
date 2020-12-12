# 2020-12-11 18:42:24

from time import time
import csv
from string import ascii_uppercase


def triang(n):
    t = int(0.5 * n * (n + 1))
    return t


def is_triang(word):
    val = calc_word_value(word)
    n = 0
    while triang(n) < val:
        n += 1
        if triang(n) == val:
            return True
    return False


def calc_word_value(word):
    letters = list(ascii_uppercase)
    lett_dict = {lett: (val + 1) for val, lett in enumerate(letters)}

    char_list = list(word)
    ans = 0
    for char in char_list:
        ans += lett_dict[char]
    return ans


def solution():
    file = "data/p042_words.txt"

    with open(file, "r") as f:
        text = f.read()

    words = text.split(",")
    words = [w.strip('"') for w in words]

    count = 0

    for word in words:
        if is_triang(word):
            count += 1

    return count


def report():
    print(("from 2000 words in word list, " f"{solution()} is a triangle word"))


def main():
    tic = time()

    # projecteuler number:
    report()
    #

    toc = time()

    print("time used:", toc - tic)


if __name__ == "__main__":
    main()
