import sys

sys.setrecursionlimit(10 ** 6)


def dfs(n):
    for a in A[n - 1]:
        if not skills[a - 1]:
            skills[a - 1] = True
            dfs(a)


N = int(input())
skills = [False] * N
skills[N - 1] = True
T = []
A = []
for _ in range(N):
    in_ = list(map(int, input().split()))
    T.append(in_[0])
    A.append(in_[2:])

dfs(N)

ans = 0
for i in range(N):
    if skills[i]:
        ans += T[i]

print(ans)
