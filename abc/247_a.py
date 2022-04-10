import sys

INF = 10 ** 18


def main():
    S = list(input())
    ans = ["0"]
    for i in range(3):
        ans.append(S[i])
    print_list(ans, sep="")


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
