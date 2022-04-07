import sys

INF = 10 ** 18


def main():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = INF
    for i in range(N):
        for j in range(N):
            ent = A[i]
            exi = B[j]

            distance = 0
            for k in range(N):
                distance += abs(A[k] - ent) + abs(exi - B[k]) + B[k] - A[k]

            ans = min(ans, distance)

    print(ans)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=""):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
