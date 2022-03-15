import sys


def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(6):
                if i + k >= N:
                    cnt = 0
                    break
                if S[i + k][j] == '#':
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                return

            cnt = 0
            for k in range(6):
                if j + k >= N:
                    cnt = 0
                    break
                if S[i][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                return

            cnt = 0
            for k in range(6):
                if i + k >= N or j + k >= N:
                    cnt = 0
                    break
                if S[i + k][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                return

            cnt = 0
            for k in range(6):
                if i + k >= N or N - 1 - j - k < 0:
                    cnt = 0
                    break
                if S[i + k][N - 1 - j - k] == '#':
                    cnt += 1
            if cnt >= 4:
                print('Yes')
                return
    print('No')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
