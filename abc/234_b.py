def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = {}
    for i in range(N):
        cnt[i + 1] = 4
    for a in A:
        cnt[a] -= 1
    for k, v in cnt.items():
        if v == 1:
            print(k)
            break


if __name__ == "__main__":
    main()
