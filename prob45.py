# 2020-12-20 15:21:11

# project euler: https://projecteuler.net
# problem 45: Triangular, pentagonal, and hexagonal

from time import time

from prob44 import is_pentagon


def calc_n_triang(n):
    ans = int(n * (n + 1) * 0.5)
    return ans


def calc_n_hexa(n):
    ans = int(n * (2 * n - 1))
    return ans


# def is_triang(num):
#     i = 1
#     n_triang = calc_n_triang(i)

#     while num > n_triang:
#         i += 1
#         n_triang = calc_n_triang(i)
#         if n_triang == num:
#             return True
#     return False


def is_hexa(num):
    i = 1
    n_hexa = calc_n_hexa(i)

    while num > n_hexa:
        i += 1
        n_hexa = calc_n_hexa(i)
        if n_hexa == num:
            return True
    return False


def solution():
    n = 40755
    while True:
        n += 1
        if n % 1000 == 0:
            print(n)
        tn = calc_n_triang(n)
        # pn = calc_n_pent(n)
        # hn = calc_n_hexa(n)
        if is_pentagon(tn) and is_hexa(tn):
            return tn


def report():
    print(
        (
            "next triangle number from 40755 that is also penta and hexa "
            f"is {solution()}"
        )
    )


def main():
    tic = time()

    # projecteuler number:
    report()
    #

    toc = time()

    print("time used:", toc - tic)


if __name__ == "__main__":
    main()
