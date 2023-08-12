# import sys

INF = 10 ** 18


def main():
    N = int(input())
    C = []
    A = []
    for _ in range(N):
        C.append(int(input()))
        A.append(list(map(int, input().split())))

    x = int(input())

    bet_x = []
    least = 100
    for i in range(N):
        if x in A[i]:
            bet_x.append(i)
            least = min(C[i], least)

    leasts = []
    for i in range(len(bet_x)):
        if C[bet_x[i]] == least:
            leasts.append(bet_x[i] + 1)

    print(len(leasts))
    print_list(leasts)


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
