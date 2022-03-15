import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])

    X1 = X // S[N]
    X2 = X % S[N]

    for i in range(N):
        if S[i + 1] > X2:
            print(X1 * N + i + 1)
            break


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
