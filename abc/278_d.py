# import sys

INF = 10 ** 18


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    B = {}
    x_q = -1

    for _ in range(Q):
        q = input().split()

        if q[0] == "1":
            x_q = int(q[1])
            B = {}
        if q[0] == "2":
            i_q = int(q[1]) - 1
            B.setdefault(i_q, 0)
            B[i_q] += int(q[2])
        if q[0] == "3":
            i_q = int(q[1]) - 1
            B.setdefault(i_q, 0)
            if x_q != -1:
                print(x_q + B[i_q])
            else:
                print(A[i_q] + B[i_q])


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
