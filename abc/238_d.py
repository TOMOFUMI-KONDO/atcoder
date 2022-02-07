# ref. https://atcoder.jp/contests/abc238/editorial/3359

def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        if s >= 2 * a and a & (s - 2 * a) == 0:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
