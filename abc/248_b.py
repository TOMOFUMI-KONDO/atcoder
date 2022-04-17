import sys

INF = 10 ** 18


def main():
    A, B, K = map(int, input().split())
    cnt = 0
    while True:
        if A >= B:
            print(cnt)
            return

        A *= K
        cnt += 1


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
