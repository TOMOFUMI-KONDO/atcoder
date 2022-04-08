def main():
    N, M = map(int, input().split())
    known = []
    for i in range(N):
        known.append([False] * (N - i - 1))
    for _ in range(M):
        x, y = map(int, input().split())
        known[x - 1][y - x - 1] = True
    # print(known)
    ans = 0
    for mask in range(1 << N):
        subset = []
        for i in range(N):
            if 1 << i & mask > 0:
                subset.append(i)

        ok = True
        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                if not known[subset[i]][subset[j] - subset[i] - 1]:
                    ok = False
                    break
            if not ok:
                break

        if ok and len(subset) > ans:
            # print(bin(mask))
            ans = len(subset)

    print(ans)


if __name__ == "__main__":
    main()
