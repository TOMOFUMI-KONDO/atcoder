# import sys
import math

INF = math.inf


def vote(a, b, c):
    if a == "0":
        if b == "0":
            return "0"
        else:
            return c
    else:
        if b == "1":
            return "1"
        else:
            return c


B = []


def f(k, i):
    if k == 0:
        return 1

    equal = []
    for j in range(3):
        if B[k - 1][i * 3 + j] == B[k][i]:
            equal.append(j)

    if len(equal) == 2:
        return min(f(k - 1, 3 * i + equal[0]), f(k - 1, 3 * i + equal[1]))
    else:
        return sum(sorted([f(k - 1, 3 * i), f(k - 1, 3 * i + 1), f(k - 1, 3 * i + 2)])[:2])


def main():
    n = int(input())
    # n, m = map(int, input().split())
    A = list(input())

    global B
    B = [A.copy()]
    i = 0
    while len(B[i]) > 1:
        b = B[i]
        B.append([])
        for j in range(len(b) // 3):
            B[i + 1].append(vote(b[j * 3], b[j * 3 + 1], b[j * 3 + 2]))
        i += 1

    print(f(n, 0))


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
