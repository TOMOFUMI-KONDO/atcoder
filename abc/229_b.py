import sys


def main():
    # N = int(input())
    A, B = map(int, input().split())
    # A = list(map(int, input().split()))
    if A > B:
        A, B = B, A
    A = list(map(int, list(str(A))))
    B = list(map(int, list(str(B))))
    for i in range(len(A)):
        a = A[-(i + 1)]
        b = B[-(i + 1)]
        if a + b > 9:
            print("Hard")
            return
    print('Easy')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
