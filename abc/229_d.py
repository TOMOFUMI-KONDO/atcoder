import sys


def main():
    S = list(input())
    K = int(input())

    sum = [0]
    for i in range(len(S)):
        sum.append(sum[i] + (1 if S[i] == "." else 0))

    ans, r = 0, 0
    for l in range(len(S)):
        while r < len(S) and sum[r + 1] - sum[l] <= K:
            r += 1
        ans = max(r - l, ans)
    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
