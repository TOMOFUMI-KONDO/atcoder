import math
import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=""):
    print(sep.join(l))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


def main():
    N = int(input())

    removed = set()
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        for j in range(2, math.floor(math.log(N, i)) + 1):
            removed.add(i ** j)

    print(N - len(list(removed)))


def is_pow(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
