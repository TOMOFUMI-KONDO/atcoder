# import sys
import math

INF = math.inf


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int, input().split()))

        positions = {}
        for i in range(2 * n):
            positions.setdefault(A[i], [])
            positions[A[i]].append(i)

        ans = set()
        for i in range(2 * n - 1):
            a, b = A[i], A[i + 1]
            pa1, pa2, pb1, pb2 = positions[a][0], positions[a][1], positions[b][0], positions[b][1]
            if pa1 + 1 == pa2 or pb1 + 1 == pb2:
                continue

            s = sorted([pa1, pa2, pb1, pb2])
            if s[0] + 1 == s[1] and s[2] + 1 == s[3]:
                if a > b:
                    a, b = b, a
                ans.add((a, b))

        print(len(ans))


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
