from itertools import permutations


def main():
    # N = int(input())
    N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    AB = {}
    for i in range(N):
        AB.setdefault(i, {})
        for j in range(N):
            AB.setdefault(j, {})
            AB[i][j] = False
            AB[j][i] = False
    for _ in range(M):
        a, b = map(int, input().split())
        AB[a - 1][b - 1] = True
        AB[b - 1][a - 1] = True
    CD = {}
    for i in range(N):
        CD.setdefault(i, {})
        for j in range(N):
            CD.setdefault(j, {})
            CD[i][j] = False
            CD[j][i] = False
    for _ in range(M):
        c, d = map(int, input().split())
        CD[c - 1][d - 1] = True
        CD[d - 1][c - 1] = True
    for p in permutations(range(N), N):
        ans = True
        for i in range(N):
            if not ans:
                break
            for j in range(N):
                if AB[i][j] != CD[p[i]][p[j]]:
                    ans = False
                    break
        if ans:
            print('Yes')
            return
    print('No')


if __name__ == "__main__":
    main()
