# import sys

INF = 10**18


def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print("Yes")
        return

    for i in range(2, N):
        if A[i - 1] * (A[1] / A[0]) != A[i]:
            print("No")
            return

    print("Yes")


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
