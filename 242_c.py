import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    mod = 998244353

    N = int(input())
    memo = [[0] * 9 for _ in range(N)]
    for i in range(N):
        for j in range(9):
            if i == 0:
                memo[N - 1][j] = 1
                continue

            if j == 0:
                memo[N - 1 - i][j] = (memo[N - i][0] + memo[N - i][1]) % mod
            elif j == 8:
                memo[N - 1 - i][j] = (memo[N - i][8] + memo[N - i][7]) % mod
            else:
                memo[N - 1 - i][j] = ((memo[N - i][j] + memo[N - i][j + 1]) % mod + memo[N - i][j - 1]) % mod

    ans = 0
    for i in range(9):
        ans = (ans + memo[0][i]) % mod
    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
