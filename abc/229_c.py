import sys


def main():
    # N = int(input())
    N, W = map(int, input().split())
    # A = list(map(int, input().split()))
    cheeses = []
    for _ in range(N):
        cheeses.append(list(map(int, input().split())))
    cheeses.sort(key=lambda x: x[0], reverse=True)
    i = 0
    weight = 0
    ans = 0
    while weight < W and i < N:
        w = min(cheeses[i][1], W - weight)
        ans += cheeses[i][0] * w
        weight += w
        i += 1
    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
