# import sys

INF = 10 ** 18

M = -1
E = []


def main():
    global M, E

    N, M = map(int, input().split())
    C = []
    P = []
    S = []
    for _ in range(N):
        CPS = list(map(int, input().split()))
        C.append(CPS[0])
        P.append(CPS[1])
        S.append(CPS[2:])

    for i in range(N):
        new_S = []
        for j in range(P[i]):
            if S[i][j] != 0:
                new_S.append(S[i][j])
        cnt_zero = P[i] - len(new_S)
        C[i] = C[i] * P[i] / (P[i] - cnt_zero)
        P[i] = len(new_S)
        S[i] = new_S

    E = [-1 for _ in range(M)]
    for i in range(M - 1, -1, -1):
        min_ = 10 ** 7
        for j in range(N):
            min_ = min(C[j] + sum([e(i + S[j][k]) for k in range(P[j])]) / P[j], min_)
        E[i] = min_

    print(E[0])


def e(i):
    if i >= M:
        return 0
    else:
        return E[i]


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
