import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N, M = map(int, input().split())
    A = list(reversed(list(map(int, input().split()))))
    C = list(reversed(list(map(int, input().split()))))

    B = [0] * (M + 1)
    for i in range(M + 1):
        tmp = C[i]
        for j in range(i):
            if i - j > N:
                continue
            tmp -= A[i - j] * B[j]

        B[i] = tmp // A[0]

    B = map(str, reversed(B))
    print(" ".join(B))


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
