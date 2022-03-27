import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    prev = [True, True]
    for i in range(1, N):
        _next = [False, False]

        if prev[0]:
            _next[0] = abs(A[i] - A[i - 1]) <= K
            _next[1] = abs(B[i] - A[i - 1]) <= K

        if prev[1]:
            _next[0] = _next[0] or abs(A[i] - B[i - 1]) <= K
            _next[1] = _next[1] or abs(B[i] - B[i - 1]) <= K

        if not _next[0] and not _next[1]:
            print("No")
            return

        prev[0] = _next[0]
        prev[1] = _next[1]

    print('Yes')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
