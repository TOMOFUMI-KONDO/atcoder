# import sys

INF = 10**18


def main():
    # n = int(input())
    # n, m = map(int, input().split())
    A = list(map(int, input().split()))
    judge(A[0] * A[1] == A[2] or A[0] * A[2] == A[1] or A[1] * A[2] == A[0])


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
