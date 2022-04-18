# import sys
import copy

INF = 10 ** 18


def main():
    R, C = map(int, input().split())
    sides = [list(map(int, input().split())) for _ in range(R)]

    ans = INF

    for bit in range(1 << R):
        rows = []

        for i in range(R):
            if 1 << i & bit > 0:
                rows.append(i)

        sides_tmp = copy.deepcopy(sides)
        for r in rows:
            for i in range(C):
                sides_tmp[r][i] ^= 1

        ans_tmp = 0

        for i in range(C):
            col_sum = 0
            for j in range(R):
                col_sum += sides_tmp[j][i]
            ans_tmp += min(col_sum, R - col_sum)

        ans = min(ans, ans_tmp)

    print(R * C - ans)


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
