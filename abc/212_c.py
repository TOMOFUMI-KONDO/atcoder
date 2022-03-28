import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=""):
    print(sep.join(l))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    min_diff = 10 ** 9
    index_a = 0
    index_b = 0

    while index_a < N and index_b < M:
        min_diff = min(abs(A[index_a] - B[index_b]), min_diff)

        if index_a == N:
            index_b += 1
        elif index_b == M:
            index_a += 1
        elif A[index_a] <= B[index_b]:
            index_a += 1
        else:
            index_b += 1

    print(min_diff)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
