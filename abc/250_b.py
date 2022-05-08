# import sys

INF = 10 ** 18


def main():
    N, A, B = map(int, input().split())

    for i in range(N):
        for _ in range(A):
            for j in range(N):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                    print("." * B, end="")
                else:
                    print("#" * B, end="")
            print()


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
