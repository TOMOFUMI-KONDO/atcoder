# import sys

INF = 10 ** 18


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    len_A = len(A)

    ans = A[K:]
    ans.extend([0] * min(K, len_A))
    print_list(ans)


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
