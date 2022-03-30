import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=""):
    print(sep.join(l))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


def main():
    S = input().split()
    mapping = {S[0]: 0, S[1]: 1, S[2]: 2}
    t1, t2, t3 = map(lambda t: mapping[t], input().split())

    if t1 == 0 and t2 == 1 and t3 == 2:
        print("Yes")
    elif t1 == 0 and t2 == 2 and t3 == 1:
        print("No")
    elif t1 == 1 and t2 == 0 and t3 == 2:
        print("No")
    elif t1 == 1 and t2 == 2 and t3 == 0:
        print("Yes")
    elif t1 == 2 and t2 == 0 and t3 == 1:
        print("Yes")
    else:  # 2 1 0
        print("No")


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
