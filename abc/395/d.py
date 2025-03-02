# import sys


INF = 10**18


def main():
    n, q = map(int, input().split())
    # A = list(map(int, input().split()))

    where = {i: i for i in range(n)}
    su_ptr = {i: i for i in range(n)}
    su_ptr_rev = {i: i for i in range(n)}
    for _ in range(q):
        op = input().split()
        if op[0] == "1":
            a, b = int(op[1]), int(op[2])
            where[a - 1] = su_ptr_rev[b - 1]
        elif op[0] == "2":
            a, b = int(op[1]), int(op[2])
            su_a = su_ptr_rev[a - 1]
            su_b = su_ptr_rev[b - 1]

            su_ptr_rev[a - 1] = su_b
            su_ptr_rev[b - 1] = su_a

            su_ptr[su_a], su_ptr[su_b] = su_ptr[su_b], su_ptr[su_a]
        else:
            a = int(op[1])
            print(su_ptr[where[a - 1]] + 1)


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
