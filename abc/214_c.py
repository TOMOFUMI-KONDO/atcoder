import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    current = T.index(min(T))
    for i in range(N):
        prev = current
        current = current + 1 if current < N - 1 else 0
        T[current] = min(T[prev] + S[prev], T[current])

    for t in T:
        print(t)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
