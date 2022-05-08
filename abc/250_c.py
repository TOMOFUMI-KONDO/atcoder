# import sys

INF = 10 ** 18


def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N + 1)]
    index = {i: i for i in range(1, N + 1)}

    for _ in range(Q):
        x = int(input())

        if index[x] == N:
            index[A[N - 2]] = N
            index[x] = N - 1
            A[N - 1] = A[N - 2]
            A[N - 2] = x
        else:
            index[A[index[x]]] = index[x]
            index[x] += 1
            A[index[x] - 2] = A[index[x] - 1]
            A[index[x] - 1] = x

    print_list(A)


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
