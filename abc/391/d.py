# import sys

INF = 10**18


def main():
    N, W = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(N)]

    Y = {i + 1: [] for i in range(W)}
    for i in range(N):
        Y[block[i][0]].append((block[i][1], i))
    disapper_at = [0] * (N + 1)
    order = [0] * N
    for i in range(W):
        Y[i + 1].sort(key=lambda x: x[0])
        for j, (y, b) in enumerate(Y[i + 1]):
            disapper_at[j] = max(disapper_at[j], y)
            order[b] = j
        disapper_at[len(Y[i + 1])] = INF

    for i in range(1, N + 1):
        disapper_at[i] = max(disapper_at[i], disapper_at[i - 1] + 1)

    Q = int(input())
    for _ in range(Q):
        T, A = map(int, input().split())
        judge(disapper_at[order[A - 1]] > T)


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
