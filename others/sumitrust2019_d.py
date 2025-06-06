import sys
from collections import defaultdict

INF = 10 ** 18


def main():
    N = int(input())
    S = list(map(int, list(input())))

    nums = [[N] * 10 for _ in range(N)]
    nums[N - 1][S[N - 1]] = N - 1
    for i in range(N - 2, -1, -1):
        for j in range(10):
            nums[i][j] = nums[i + 1][j]
        nums[i][S[i]] = i

    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                first = nums[0][i]
                if first >= N - 2:
                    continue

                second = nums[first + 1][j]
                if second >= N - 1:
                    continue

                ans += 1 if nums[second + 1][k] < N else 0

    print(ans)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=""):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


class BinaryTrie:
    def __init__(self, bit_depth=60):
        self.root = [None, None, 0]  # [0-child, 1-child, count]
        self.bit_start = 1 << (bit_depth - 1)

    def insert(self, x):
        """xを格納"""
        b = self.bit_start
        node = self.root
        node[2] += 1
        # print(self.root)
        while b:
            i = bool(x & b)
            if node[i] is None:
                node[i] = [None, None, 1]
            else:
                node[i][2] += 1
            node = node[i]
            b >>= 1

    def pop_min(self, mask=0):
        """xor_mask適用後の最小値を取得し、木からは削除"""
        b = self.bit_start
        node = self.root
        m = mask
        node[2] -= 1
        ret2 = 0
        while b:
            i = bool(m & b)
            ret2 = ret2 << 1
            if node[i] is None:
                i ^= 1
                ret2 += 1

            if node[i][2] > 1:
                node[i][2] -= 1
                node = node[i]
            else:
                tmp = node[i]
                node[i] = None
                node = tmp
            b >>= 1
        return ret2

    def get_min(self, mask=0):
        """xor_mask適用後の最小値を取得"""
        b = self.bit_start
        node = self.root
        m = mask
        ret2 = 0
        while b:
            i = bool(m & b)
            ret2 = ret2 << 1
            if node[i] is None:
                i ^= 1
                ret2 += 1
            node = node[i]
            b >>= 1
        return ret2

    def get_kth_min(self, k=1):
        """k番目に小さい値を取得"""
        b = self.bit_start
        node = self.root
        ret2 = 0
        while b:
            # print(b)
            ret2 = ret2 << 1
            b >>= 1
            if node[0] is None:
                node = node[1]
                ret2 += 1
                continue
            if node[1] is None:
                node = node[0]
                continue
            if k <= node[0][2]:
                node = node[0]
                continue
            else:
                k -= node[0][2]
                node = node[1]
                ret2 += 1
                continue
        return ret2

    def erase(self, x):
        """xを削除"""
        b = self.bit_start
        node = self.root
        node[2] -= 1
        # print(self.root)
        while b:
            i = bool(x & b)
            if node[i][2] > 1:
                node[i][2] -= 1
                node = node[i]
            else:
                tmp = node[i]
                node[i] = None
                node = tmp
            b >>= 1

    def lower_bound(self, bound=0):
        """boundより大きい値での最小値を取得。存在しない場合はNoneを返す。"""
        ans = self.get_kth_min(self.less_x(bound + 1) + 1)
        if ans > bound:
            return ans

    def upper_bound(self, bound=0):
        """boundより小さい値での最大値を取得。存在しない場合はNoneを返す。"""
        ans = self.get_kth_min(self.less_x(bound))
        if ans < bound:
            return ans

    def merge(self, trie):
        """2つのbinatytrie木を合成"""

        def merges(x, y):
            if (not x):
                return y
            if (not y):
                return x
            return [merges(x[0], y[0]), merges(x[1], y[1]), x[2] + y[2]]

        self.root = merges(self.root, trie.root)

    def less_x(self, x):
        """xより小さい値の数を出力"""
        if x < 0:
            return 0
        b = self.bit_start
        node = self.root
        ans = 0
        # print(self.root)
        while b:
            i = bool(x & b)
            if node[i] is None:
                if i == 1:
                    ans += node[0][2]
                return ans
            if i == 1:
                if node[0] is not None:
                    ans += node[0][2]
            node = node[i]
            b >>= 1
        return ans

    def less_x_mask(self, x, mask=0):
        """xormask適用後,xより小さい値の数を出力"""
        if x < 0:
            return 0
        b = self.bit_start
        node = self.root
        ans = 0
        m = mask
        # print(self.root)
        while b:
            i = bool(x & b)
            mm = bool(m & b)
            imm = i ^ mm
            if node[imm] is None:
                if i == 1:
                    ans += node[imm ^ 1][2]
                return ans
            if i == 1:
                if node[imm ^ 1] is not None:
                    ans += node[imm ^ 1][2]
            node = node[imm]
            b >>= 1
        return ans

    def is_exist(self, x):
        """xが存在するか判定"""
        b = self.bit_start
        node = self.root
        node[2] -= 1
        # print(self.root)
        while b:
            i = bool(x & b)
            if node[i] is None:
                return False
            node = node[i]
            b >>= 1
        return True


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
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
