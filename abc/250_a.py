# import sys

INF = 10 ** 18


def main():
    H, W = map(int, input().split())
    R, C = map(int, input().split())

    ans = 0
    if 1 < R:
        ans += 1
    if R < H:
        ans += 1
    if 1 < C:
        ans += 1
    if C < W:
        ans += 1

    print(ans)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
