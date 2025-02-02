# import sys

INF = 10**18


def main():
    N, Q = map(int, input().split())

    where = {i + 1: i + 1 for i in range(N)}
    count = {i + 1: 1 for i in range(N)}
    multi = 0
    for _ in range(Q):
        query = input()
        if query == "2":
            print(multi)
        else:
            _, P, H = map(int, query.split())
            if count[where[P]] == 2:
                multi -= 1
            if count[H] == 1:
                multi += 1
            count[where[P]] -= 1
            count[H] += 1
            where[P] = H


def judge(cond, yes="Yes", no="No"):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
