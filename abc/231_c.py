def main():
    # N = int(input())
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(Q):
        x = int(input())
        ok = -1
        ng = N
        while ok < N - 1 and ng >= 1 and ng - ok != 1:
            mid = (ng + ok) // 2
            if x > A[mid]:
                ok = mid
            else:
                ng = mid
        if ok >= N - 1:
            print(0)
        elif ng < 1:
            print(N)
        else:
            print(N - ok - 1)


if __name__ == "__main__":
    main()
