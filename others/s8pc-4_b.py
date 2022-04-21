# import sys

INF = 10 ** 18


def bit_count(b):
    ret = 0

    while b > 0:
        ret += 1 if b & 1 == 1 else 0
        b >>= 1

    return ret


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = INF

    for bit in range(0, 1 << N):
        if bit_count(bit) != K:
            continue

        bills = []
        for i in range(N):
            if 1 << i & bit > 0:
                bills.append(i)

        tmp_ans = 0
        a_max = 0

        for i in range(N):
            if i not in bills:
                a_max = max(a_max, A[i])
                continue

            if a_max < A[i]:
                a_max = A[i]
            else:
                tmp_ans += a_max - A[i] + 1
                a_max += 1

        ans = min(ans, tmp_ans)

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
