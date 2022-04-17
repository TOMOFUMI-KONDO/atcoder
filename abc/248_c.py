import sys

INF = 10 ** 18
MOD = 998244353


def main():
    N, M, K = map(int, input().split())

    memo = [[0] * (K + 1) for _ in range(N + 1)]
    memo[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            for k in range(1, min(M + 1, j + 1)):
                memo[i][j] += memo[i - 1][j - k]

    ans = 0
    for m in memo[-1]:
        ans = (ans + m) % MOD

    print(ans)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
