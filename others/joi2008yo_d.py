import sys

INF = 10 ** 18


def main():
    M = int(input())
    XY_M = [list(map(int, input().split())) for _ in range(M)]
    XY_M.sort(key=lambda x: x[1])
    XY_M.sort()

    N = int(input())
    XY_N = [list(map(int, input().split())) for _ in range(N)]
    XY_N.sort(key=lambda x: x[1])
    XY_N.sort()

    ans = []
    for i in range(N):
        diff = [XY_N[i][0] - XY_M[0][0], XY_N[i][1] - XY_M[0][1]]
        index = 0
        for j in range(i, N):
            xy_n = XY_N[j]
            xy_m = XY_M[index]
            if xy_n[0] - xy_m[0] == diff[0] and xy_n[1] - xy_m[1] == diff[1]:
                index += 1
            if index >= M:
                break
        if index == M:
            ans = diff
            break

    print_list(ans)


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
