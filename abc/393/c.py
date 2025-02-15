# import sys


INF = 10**18


def main():
    # n = int(input())
    n, m = map(int, input().split())
    # A = list(map(int, input().split()))
    links = {}
    ans = 0
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        if f"{u},{v}" in links or u == v:
            ans += 1
        else:
            links[f"{u},{v}"] = True
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
