# import sys

INF = 10**18


def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            ok = True

            for k in range(M):
                if not ok:
                    break
                for m in range(M):
                    if T[k][m] == S[i + k][j + m]:
                        continue
                    else:
                        ok = False
                        break

            if ok:
                print("%d %d" % (i + 1, j + 1))


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
