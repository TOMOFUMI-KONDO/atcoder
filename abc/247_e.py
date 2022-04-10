import sys

INF = 10 ** 18


def calc(B, X, Y):
    l, r, cnt_x, cnt_y, ans = 0, 0, 0, 0, 0

    while l < len(B):
        while r < len(B) and (cnt_x == 0 or cnt_y == 0):
            if B[r] == X:
                cnt_x += 1
            if B[r] == Y:
                cnt_y += 1
            r += 1

        if cnt_x > 0 and cnt_y > 0:
            ans += len(B) - r + 1

        if B[l] == X:
            cnt_x -= 1
        if B[l] == Y:
            cnt_y -= 1
        l += 1

    return ans


def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    i, ans = 0, 0
    while i < N:
        B = []
        while i < N and Y <= A[i] <= X:
            B.append(A[i])
            i += 1
        if len(B) > 0:
            ans += calc(B, X, Y)
        else:
            i += 1

    print(ans)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
