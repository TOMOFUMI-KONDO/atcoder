# import sys
import bisect
import math

INF = math.inf


def main():
    N, M, Sx, Sy = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    X, Y = {}, {}
    for x, y in XY:
        X.setdefault(x, set())
        X[x].add(y)
        Y.setdefault(y, set())
        Y[y].add(x)
    for i in X.keys():
        X[i] = set(sorted(X[i]))
    for i in Y.keys():
        Y[i] = set(sorted(Y[i]))

    memo = set()
    pos_x, pos_y = Sx, Sy
    for _ in range(M):
        d, c_str = input().split()
        c = int(c_str)
        if d == "U":
            if pos_x in X:
                left = bisect.bisect_left(list(X[pos_x]), pos_y)
                right = bisect.bisect_right(list(X[pos_x]), pos_y + c)
                for _ in range(left, right):
                    y = list(X[pos_x])[left]
                    memo.add(tuple([pos_x, y]))
                    X[pos_x].remove(y)
                    if y in Y:
                        Y[y].discard(pos_x)
            pos_y += c
        if d == "D":
            if pos_x in X:
                left = bisect.bisect_left(list(X[pos_x]), pos_y - c)
                right = bisect.bisect_right(list(X[pos_x]), pos_y)
                for _ in range(left, right):
                    y = list(X[pos_x])[left]
                    memo.add(tuple([pos_x, y]))
                    X[pos_x].remove(y)
                    if y in Y:
                        Y[y].discard(pos_x)
            pos_y -= c
        if d == "L":
            if pos_y in Y:
                left = bisect.bisect_left(list(Y[pos_y]), pos_x - c)
                right = bisect.bisect_right(list(Y[pos_y]), pos_x)
                for _ in range(left, right):
                    x = list(Y[pos_y])[left]
                    memo.add(tuple([x, pos_y]))
                    Y[pos_y].remove(x)
                    if x in X:
                        X[x].discard(pos_y)
            pos_x -= c
        if d == "R":
            if pos_y in Y:
                left = bisect.bisect_left(list(Y[pos_y]), pos_x)
                right = bisect.bisect_right(list(Y[pos_y]), pos_x + c)
                for _ in range(left, right):
                    x = list(Y[pos_y])[left]
                    memo.add(tuple([x, pos_y]))
                    Y[pos_y].remove(x)
                    if x in X:
                        X[x].discard(pos_y)
            pos_x += c

    count = len(memo)
    print(f"{pos_x} {pos_y} {count}")


def judge(cond: bool, yes="Yes", no="No"):
    print(yes if cond else no)


def print_list(l: list, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l: list):
    for i in range(len(l)):
        print_list(l[i])


def print_dict(d: dict):
    for k, v in d.items():
        print(f"{k} {v}")


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
