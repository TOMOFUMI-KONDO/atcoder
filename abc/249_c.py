# import sys

INF = 10 ** 18


def main():
    N, K = map(int, input().split())
    S = [list(input()) for _ in range(N)]

    ans = 0

    for bit in range(1 << N):
        words = []
        for i in range(N):
            if 1 << i & bit > 0:
                words.append(S[i])

        cnt = {}
        for word in words:
            for w in word:
                cnt.setdefault(w, 0)
                cnt[w] += 1

        tmp_ans = 0
        for v in cnt.values():
            if v == K:
                tmp_ans += 1

        ans = max(ans, tmp_ans)

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
