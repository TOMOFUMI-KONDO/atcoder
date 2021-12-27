x = 0
n = 0
A = []
L = []
ans = 0


def dfs(position, product):
    global ans

    for i in range(L[position]):
        next_product = product * A[position][i]

        if position == n - 1:
            if next_product == x:
                ans += 1

            continue

        if product * A[position][i] > x:
            continue

        dfs(position + 1, next_product)


def main():
    global n, x, A, L

    n, x = map(int, input().split())

    for _ in range(n):
        i = list(map(int, input().split()))
        L.append(i[0])
        A.append(i[1:])

    dfs(0, 1)

    print(ans)


if __name__ == '__main__':
    main()
