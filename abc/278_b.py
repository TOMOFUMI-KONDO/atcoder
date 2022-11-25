# import sys

INF = 10 ** 18


def main():
    H, M = map(int, input().split())

    for _ in range(60 * 24):
        H_str = str(H) if H > 9 else "0" + str(H)
        M_str = str(M) if M > 9 else "0" + str(M)

        H_ = int(H_str[0] + M_str[0])
        M_ = int(H_str[1] + M_str[1])

        if H_ <= 23 and M_ <= 59:
            print(f"{H} {M}")
            return

        M += 1
        if M == 60:
            H += 1
            M = 0
        if H == 24:
            H = 0


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
