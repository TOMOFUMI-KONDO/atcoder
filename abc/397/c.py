# import sys

INF = 10**18


def main():
    n = int(input())
    A = list(map(int, input().split()))

    counts = []
    memo = {i + 1: False for i in range(n)}
    counts_rev = []
    memo_rev = {i + 1: False for i in range(n)}

    prev = 0
    prev_rev = 0
    for i in range(n):
        if not memo[A[i]]:
            prev += 1
        counts.append(prev)
        memo[A[i]] = True

        if not memo_rev[A[n - 1 - i]]:
            prev_rev += 1
        counts_rev.append(prev_rev)
        memo_rev[A[n - 1 - i]] = True

    ans = 0
    for i in range(n - 1):
        ans = max(ans, counts[i] + counts_rev[n - 2 - i])

    print(ans)


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
