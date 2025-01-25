# import sys

INF = 10**18


def main():
    A = list(map(int, input().split()))
    diff = [0, 0, 0, 0, 0]
    for i in range(5):
        if A[i] != i + 1:
            diff[i] = 1

    if sum(diff) != 2:
        print("No")
        return

    prev = 0
    for d in diff:
        if prev:
            if d:
                print("Yes")
                return
            else:
                print("No")
                return
        prev = d


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
