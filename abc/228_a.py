import sys


def main():
    S, T, X = map(int, input().split())
    if S <= X < T or (S > T and (X >= S or X < T)):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
