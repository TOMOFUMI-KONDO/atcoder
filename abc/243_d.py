import sys
from collections import deque


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N, X = map(int, input().split())
    S = list(input())

    buf = deque([])
    skip = [0] * N

    for i in range(N):
        s = S[N - 1 - i]
        if s == "U":
            buf.append(N - 1 - i)
        elif s == "L":
            if len(buf) > 0:
                skip[N - 1 - i] = 1
                skip[buf.pop()] = 1
        else:
            if len(buf) > 0:
                skip[N - 1 - i] = 1
                skip[buf.pop()] = 1

    for i in range(N):
        if skip[i] == 1:
            continue

        s = S[i]
        if s == "U":
            X //= 2
        elif s == "L":
            X = 2 * X
        else:
            X = 2 * X + 1

    print(X)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
