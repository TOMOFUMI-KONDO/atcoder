import sys
from collections import deque

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=""):
    print(sep.join(l))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


def main():
    N, K = map(int, input().split())

    A = deque([N])
    for i in range(K):
        prev = A.pop()
        A.append(prev)

        g1 = list(sorted(map(int, list(str(prev))), reverse=True))
        g2 = list(reversed(g1))
        A.append(int("".join(map(str, g1))) - int("".join(map(str, g2))))

    print(A.pop())


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
