# import sys

INF = 10**18


def main():
    # n = int(input())
    # n, m = map(int, input().split())
    # A = list(map(int, input().split()))
    s1, s2 = input().split()

    if s1 == "sick" and s2 == "sick":
        print(1)
    elif s1 == "sick" and s2 == "fine":
        print(2)
    elif s1 == "fine" and s2 == "sick":
        print(3)
    else:
        print(4)


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
