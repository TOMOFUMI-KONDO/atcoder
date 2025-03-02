# import sys

INF = 10**18


def main():
    n = int(input())
    A = list(map(int, input().split()))

    index_map = {}
    for i in range(n):
        a = A[i]
        index_map.setdefault(a, [])
        index_map[a].append(i)

    start, end = -1, n
    for indexes in index_map.values():
        for i in range(0, len(indexes) - 1):
            if indexes[i + 1] - indexes[i] < end - start:
                start = indexes[i]
                end = indexes[i + 1]

    if start == -1:
        print(-1)
    else:
        print(end - start + 1)


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
