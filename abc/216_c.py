import sys
from collections import deque

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())

    S = deque([])
    while N > 1:
        if N % 2 == 0:
            N //= 2
            S.appendleft("B")
        else:
            N -= 1
            S.appendleft("A")
    S.appendleft("A")

    for i in range(len(S)):
        print(S.popleft(), end="")
    print()


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
