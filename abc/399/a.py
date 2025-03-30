# import sys
import math

INF = math.inf


def main():
    n = int(input())
    s = input()
    t = input()
    ans = 0
    for i in range(n):
        if s[i] != t[i]:
            ans += 1
    print(ans)
    # n, m = map(int, input().split())
    # A = list(map(int, input().split()))


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
