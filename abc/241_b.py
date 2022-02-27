import sys


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for b in B:
        if b in A:
            A.remove(b)
        else:
            print('No')
            return
    print('Yes')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
