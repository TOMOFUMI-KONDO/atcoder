# import sys

INF = 10 ** 18


def main():
    N, Q = map(int, input().split())
    A = sorted(list(map(int, input().split())))

    # subs = [A[i] - A[i - 1] for i in range(1, N)]
    comsub = [0]
    for a in A:
        comsub.append(comsub[-1] + a)

    # print(A)
    # print(comsub)
    for _ in range(Q):
        x = int(input())
        # print()
        # print(x)

        ok, ng = -1, N
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A[mid] <= x:
                ok = mid
            else:
                ng = mid

        # x以下の1番大きいなAの数

        index = ok

        ans = 0

        # print(index)
        if index >= 0:
            ans += x * (index + 1) - comsub[index + 1]
            # ans += x - A[index]
            # prev = x - A[index]
            # for i in range(index - 1, -1, -1):
            #     ans += prev + subs[i]
            #     prev = prev + subs[i]

        # print(ans)
        if index < N - 1:
            ans += comsub[N] - comsub[index + 1] - x * (N - 1 - index)
            # ans += A[index + 1] - x
            # prev = A[index + 1] - x
            # # print(ans, prev)
            # for i in range(index + 1, N - 1):
            #     ans += prev + subs[i]
            #     prev = prev + subs[i]

        print(ans)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
