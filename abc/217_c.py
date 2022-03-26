import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    P = list(map(int, input().split()))

    ans = [0] * N
    for i in range(N):
        ans[P[i] - 1] = i + 1

    ans = map(str, ans)
    print(" ".join(ans))


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
