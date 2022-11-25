# import sys

INF = 10 ** 18


def main():
    N = int(input())
    A = list(map(int, input().split()))

    runners = [0, 0, 0, 0]
    ans = 0
    for a in A:
        if a == 1:
            ans += runners[3]
            runners[3] = runners[2]
            runners[2] = runners[1]
            runners[1] = 1
        elif a == 2:
            ans += runners[3] + runners[2]
            runners[3] = runners[1]
            runners[2] = 1
            runners[1] = 0
        elif a == 3:
            ans += runners[3] + runners[2] + runners[1]
            runners[3] = 1
            runners[2] = 0
            runners[1] = 0
        else:
            ans += runners[3] + runners[2] + runners[1] + 1
            runners[3], runners[2], runners[1] = 0, 0, 0

    print(ans)


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
