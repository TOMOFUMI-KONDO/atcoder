# import sys
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


INF = 10**18


def main():
    n, m = map(int, input().split())
    groups = UnionFind(n)
    cables = []
    for i in range(1, m + 1):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a

        if groups.same(a - 1, b - 1):
            cables.append([i, a, b])
        else:
            groups.union(a - 1, b - 1)

    roots = groups.roots()
    group_cables = {r + 1: [] for r in roots}
    for c in cables:
        group = groups.find(c[1] - 1)
        group_cables[group + 1].append(c)
    group_cables = sorted(group_cables.items(), key=lambda x: len(x[1]), reverse=True)
    cables = []
    for i in range(len(group_cables)):
        for j in range(len(group_cables[i][1])):
            cables.append(group_cables[i][1][j])

    print(len(roots) - 1)
    for i in range(len(roots) - 1):
        cable = cables[i]
        print(cable[0], cable[1], group_cables[i + 1][0])


def judge(cond, yes="Yes", no="No"):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
