# import sys

INF = 10**18


def main():
    S = list(map(int, list(input())))

    prev = -1
    ans = 0
    for s in S:
        if prev == 0 and s == 0:
            prev = -1
            continue
        ans += 1
        prev = s

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
