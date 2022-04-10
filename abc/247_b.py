import sys

INF = 10 ** 18


def main():
    N = int(input())
    S, T = [], []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)

    for i in range(N):
        s_idx = -1
        for j in range(N):
            if i == j:
                continue
            if S[i] == S[j] or S[i] == T[j]:
                s_idx = j

        t_idx = -1
        for j in range(N):
            if i == j:
                continue
            if T[i] == S[j] or T[i] == T[j]:
                t_idx = j

        if (s_idx != -1) and (t_idx != -1):
            print('No')
            return

    print('Yes')


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
