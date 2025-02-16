# import sys

INF = 10**18


def main():
    n = int(input())
    # n, m = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    looks = {i + 1: 0 for i in range(n)}
    for i in range(n):
        looks[Q[i]] = Q[P[i] - 1]
    for i, v in looks.items():
        print(v, end="")
        if i != n:
            print("", end=" ")
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
