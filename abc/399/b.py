# import sys
import math

INF = math.inf


def main():
    n = int(input())
    P = list(map(int, input().split()))

    r = 1
    order = {}
    while r <= n:
        x = 0
        k = 0
        for i in range(n):
            if P[i] in order:
                continue

            if P[i] == x:
                k += 1
            elif P[i] > x:
                x = P[i]
                k = 1
        order[x] = r
        r += k

    for i in range(n):
        print(order[P[i]])

    # P2 = []
    # for i in range(n):
    #     P2.append([i, P[i]])

    # P2.sort(key=lambda x: x[1], reverse=True)

    # stack = 0
    # order = 1
    # prev = P2[0][1]
    # ans = [0 for _ in range(n)]
    # for i in range(n):
    #     if prev == P2[i][1]:
    #         stack += 1
    #     else:
    #         stack = 0
    #         order += 1 + stack
    #     ans[P2[i][0]] = order
    #     prev = P2[i][1]

    # for p in ans:
    #     print(p)


def judge(cond, yes="Yes", no="No"):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
