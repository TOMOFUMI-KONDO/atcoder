reachable = []
C = []
H = 0
W = 0


def main():
    global C, reachable, H, W
    # N = int(input())
    H, W = map(int, input().split())
    # A = list(map(int, input().split()))
    C = [list(input()) for _ in range(H)]
    reachable = [[False] * W for _ in range(H)]
    check(0, 0)
    ans = 0
    for i in range(H):
        for j in range(W):
            if reachable[i][j]:
                ans = max(i + j + 1, ans)
    print(ans)


def check(i, j):
    global reachable
    reachable[i][j] = True
    if i < H - 1 and C[i + 1][j] == "." and not reachable[i + 1][j]:
        check(i + 1, j)
    if j < W - 1 and C[i][j + 1] == "." and not reachable[i][j + 1]:
        check(i, j + 1)


if __name__ == "__main__":
    main()
