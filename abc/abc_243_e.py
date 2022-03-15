import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append([a - 1, b - 1, c])

    distances = [[INF] * N for _ in range(N)]
    for i in range(N):
        distances[i][i] = 0
    for a, b, c, in edges:
        distances[a][b] = c
        distances[b][a] = c

    for i in range(N):
        for j in range(N):
            for k in range(N):
                distances[j][k] = min(distances[j][k], distances[j][i] + distances[i][k])

    ans = 0
    for a, b, c, in edges:
        unused = 0
        if c > distances[a][b]:
            unused = 1
        else:
            for i in range(N):
                if i == a or i == b:
                    continue
                if c == distances[a][i] + distances[i][b]:
                    unused = 1
                    break
        ans += unused

    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
