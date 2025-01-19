# https://atcoder.jp/contests/abc387/editorial/11833

# import sys
from collections import deque

INF = 10**18


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == "S":
                s = (i, j)
            if S[i][j] == "G":
                g = (i, j)

    moves = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
    ans = INF
    memo = {(i, j): INF for i in range(H) for j in range(W)}
    memo[s] = 0

    queue = deque([s])

    while len(queue) > 0:
        i, j = queue.popleft()

        for m in moves[(i + j) % 2]:
            ni, nj = i + m[0], j + m[1]
            if ni < 0 or ni > H - 1 or nj < 0 or nj > W - 1:
                continue
            if S[ni][nj] == "#":
                continue

            if memo[ni, nj] == INF:
                memo[ni, nj] = memo[i, j] + 1
                queue.append((ni, nj))

    ans = memo[g]

    memo = {(i, j): INF for i in range(H) for j in range(W)}
    memo[s] = 0
    queue = deque([s])

    while len(queue) > 0:
        i, j = queue.popleft()

        for m in moves[(i + j + 1) % 2]:
            ni, nj = i + m[0], j + m[1]
            if ni < 0 or ni > H - 1 or nj < 0 or nj > W - 1:
                continue
            if S[ni][nj] == "#":
                continue

            if memo[ni, nj] == INF:
                memo[ni, nj] = memo[i, j] + 1
                queue.append((ni, nj))

    ans = min(ans, memo[g])

    print(ans if ans != INF else -1)


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
