INF = 10 ** 18

S = []


def search(x, n):
    ok = -1
    ng = len(S[x])
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if S[x][mid] <= n:
            ok = mid
        else:
            ng = mid

    return ok


def main():
    global S

    N = int(input())
    A = list(map(int, input().split()))

    S = [[-1] for _ in range(N)]
    for i in range(N):
        a = A[i] - 1
        S[a].append(i)
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        L -= 2
        R -= 1
        X -= 1
        print(search(X, R) - search(X, L))


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10 ** 6)
    main()
