# import sys

INF = 10 ** 18


def main():
    N, K = map(int, input().split())
    A = [False for _ in range(N)]
    for i in list(map(int, input().split())):
        A[i - 1] = True
    XY = [list(map(int, input().split())) for _ in range(N)]

    minimum_distances = []
    for i in range(N):
        if A[i]:
            continue

        minimum_distance = INF
        for j in range(N):
            if i == j or not A[j]:
                continue
            minimum_distance = min(minimum_distance, (XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2)

        minimum_distances.append(minimum_distance)

    print(max(minimum_distances) ** (1 / 2))


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
