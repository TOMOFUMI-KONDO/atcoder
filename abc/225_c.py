import sys


def main():
    N, M = map(int, input().split())
    current_row = -1
    start_col = -1
    for _ in range(N):
        B = list(map(int, input().split()))

        if current_row == -1:
            current_row = (B[0] - 1) // 7
            start_col = B[0] - 7 * current_row - 1

        for i in range(start_col, start_col + M):
            if i > 6 or B[i - start_col] != 7 * current_row + i + 1:
                print('No')
                return

        current_row += 1
    print('Yes')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
