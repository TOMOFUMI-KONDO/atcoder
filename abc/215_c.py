import itertools
import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    S, K = input().split()
    K = int(K)

    strings = set()
    for s in itertools.permutations(S):
        strings.add(s)
    strings = list(strings)
    strings.sort()

    print("".join(strings[K - 1]))


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
