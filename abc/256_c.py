# import sys

INF = 10 ** 18


def main():
    HW = list(map(int, input().split()))
    h1, h2, h3 = HW[:3]
    w1, w2, w3 = HW[3:]

    ans = 0
    for i in range(1, 29):
        for j in range(1, 29):
            for k in range(1, 29):
                for l in range(1, 29):
                    m3 = h1 - i - j
                    m6 = h2 - k - l
                    m7 = w1 - i - k
                    m8 = w2 - j - l
                    m9_h = h3 - m7 - m8
                    m9_w = w3 - m3 - m6

                    if 0 < m3 and 0 < m6 and 0 < m7 and 0 < m8 and m9_h > 0 and m9_w > 0 and m9_h == m9_w:
                        ans += 1

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
