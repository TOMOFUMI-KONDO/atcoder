# import sys

INF = 10 ** 18


def main():
    N = int(input())
    S = list(input())
    Q = int(input())

    to_small = False
    to_big = False
    excepts = set()

    for _ in range(Q):
        txc = input().split()
        t, x, c = int(txc[0]), int(txc[1]), txc[2]

        if t == 1:
            S[x - 1] = c
            excepts.add(x - 1)
        elif t == 2:
            to_small = True
            to_big = False
            excepts.clear()
        else:
            to_big = True
            to_small = False
            excepts.clear()

    for i in range(N):
        if i in excepts:
            print(S[i], end="")
        elif to_small:
            print(S[i].lower(), end="")
        elif to_big:
            print(S[i].upper(), end="")
        else:
            print(S[i], end="")

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
