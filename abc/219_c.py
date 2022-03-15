import sys
from functools import cmp_to_key

chars = []


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def cmp(a, b):
    for i in range(max(len(a), len(b))):
        if i >= len(a) or i >= len(b):
            break

        if a[i] != b[i]:
            return chars[a[i]] - chars[b[i]]
    return 1 if len(a) > len(b) else -1


def main():
    global chars
    chars = {chr(97 + i): 0 for i in range(26)}
    X = list(input())
    for i in range(26):
        chars[X[i]] = i

    N = int(input())
    S = [input() for _ in range(N)]
    S.sort(key=cmp_to_key(cmp))
    for s in S:
        print(s)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
