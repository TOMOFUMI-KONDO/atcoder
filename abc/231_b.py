def main():
    N = int(input())
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    cnt = {}
    for _ in range(N):
        s = input()
        cnt.setdefault(s, 0)
        cnt[s] += 1
    print(max(cnt.items(), key=lambda x: x[1])[0])


if __name__ == "__main__":
    main()
