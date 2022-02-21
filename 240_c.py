import sys

sys.setrecursionlimit(10 ** 6)

N, X = map(int, input().split())
max_ = 2 ** (X + 1) - 1
reachable = 1
for _ in range(N):
    a, b = map(int, input().split())
    reachable = (reachable << a | reachable << b) & max_
print('Yes' if reachable >> X == 1 else 'No')
