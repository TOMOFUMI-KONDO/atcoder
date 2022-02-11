A = []
N = 0
pairs = []
used = []


def main():
    global A, N, used
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2 * N - 1)]
    used = [False for _ in range(N * 2)]

    print(search())


def search():
    global pairs

    if len(pairs) == N:
        ans = 0
        for p in pairs:
            ans ^= A[p[0]][p[1] - p[0] - 1]
        return ans

    for i in range(N * 2):
        if not used[i]:
            person1 = i
            break
    used[person1] = True

    ans = 0
    for i in range(N * 2):
        if used[i]:
            continue

        person2 = i
        pairs.append([person1, person2])
        used[person2] = True

        ans = max(ans, search())

        used[person2] = False
        pairs.pop()

    used[person1] = False
    return ans


if __name__ == "__main__":
    main()
