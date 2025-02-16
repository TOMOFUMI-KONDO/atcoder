# import sys

INF = 10**18


def main():
    # n = int(input())
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    N = {i + 1: True for i in range(n)}
    C = n
    for a in A:
        N[a] = False
        C -= 1
    print(C)
    for k, v in N.items():
        if v:
            print(k, end="")
            if k != n:
                print(" ", end="")
    print("")


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
