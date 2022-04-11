def calc(A):
    ret, i = 0, 0
    for a in A:
        if a == 0:
            i += 1
        else:
            ret += (i * (i + 1)) // 2
            i = 0

    ret += (i * (i + 1)) // 2
    return ret


def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    all, not_x, not_y, not_xy = [0] * N, [0] * N, [0] * N, [0] * N

    for i in range(N):
        if A[i] < Y or A[i] > X:
            all[i], not_x[i], not_y[i], not_xy[i] = 1, 1, 1, 1
        if A[i] == X:
            not_x[i], not_xy[i] = 1, 1
        if A[i] == Y:
            not_y[i], not_xy[i] = 1, 1

    print(calc(all) - calc(not_x) - calc(not_y) + calc(not_xy))


if __name__ == "__main__":
    main()
