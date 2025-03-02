# import sys
from queue import PriorityQueue

INF = 10**18


def main():
    n, m, x = map(int, input().split())

    E = {i: [] for i in range(n * 2)}
    for i in range(n):
        E[i].append([i + n, x])
        E[i + n].append([i, x])
    for _ in range(m):
        u, v = map(int, input().split())
        E[u - 1].append([v - 1, 1])
        E[v - 1 + n].append([u - 1 + n, 1])

    D = [INF for _ in range(n * 2)]
    D[0] = 0

    Q = PriorityQueue(n * 2)
    Q.put([D[0], 0])

    while D[n - 1] == INF or D[n * 2 - 1] == INF:
        cost, u = Q.get()
        if cost != D[u]:
            continue
        for v, cost2v in E[u]:
            d = D[u] + cost2v
            if D[v] > d:
                D[v] = d
                Q.put([d, v])

    print(min(D[n - 1], D[n * 2 - 1]))


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
