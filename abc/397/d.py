# import sys
import math

INF = math.inf


def main():
    n = int(input())

    d = 1
    while d * d * d <= n:
        y = 0
        ng = 10**9
        while ng - y > 1:
            mid = (y + ng) // 2
            if 3 * d * mid**2 + 3 * d**2 * mid + d**3 == n:
                print(f"{d + mid} {mid}")
                return
            elif 3 * d * mid**2 + 3 * d**2 * mid + d**3 < n:
                y = mid
            elif 3 * d * mid**2 + 3 * d**2 * mid + d**3 > n:
                ng = mid

        d += 1
    print("-1")


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
