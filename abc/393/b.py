# import sys

INF = 10**18


def main():
    # n = int(input())
    # n, m = map(int, input().split())
    # A = list(map(int, input().split()))
    S = input()
    ans = 0
    for i in range(len(S) - 2):
        for j in range(i + 1, len(S) - 1):
            for k in range(j + 1, len(S)):
                if j - i != k - j:
                    continue

                if S[i] == "A" and S[j] == "B" and S[k] == "C":
                    ans += 1

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
