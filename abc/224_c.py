import sys


def main():
    N = int(input())
    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (X[i] - X[k]) * (Y[i] - Y[j]) != (X[i] - X[j]) * (Y[i] - Y[k]):
                    cnt += 1

    print(cnt)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
