import sys


class UF(object):
    def __init__(self, n):
        self.n = n
        self.roots = [i for i in range(n)]

    def root(self, n):
        if self.roots[n] == n:
            return n
        else:
            self.roots[n] = self.root(self.roots[n])
            return self.roots[n]

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def merge(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return

        self.roots[a] = b


def main():
    sys.setrecursionlimit(1000000)
    # N = int(input())
    N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    cnt = [0] * N
    uf = UF(N)
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        cnt[a] += 1
        cnt[b] += 1

        if uf.same(a, b):
            print('No')
            return

        uf.merge(a, b)

    if max(cnt) > 2:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
