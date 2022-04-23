# import sys

INF = 10 ** 18


def main():
    S = list(input())

    small = False
    big = False
    chars = []

    for s in S:
        if s in chars:
            print("No")
            return

        chars.append(s)

        if s.islower():
            small = True
        else:
            big = True

    judge(small & big)


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
