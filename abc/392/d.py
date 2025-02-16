# import sys

INF = 10**18


def main():
    n = int(input())
    # n, m = map(int, input().split())
    K = []
    A = []
    for _ in range(n):
        ka = list(map(int, input().split()))
        K.append(ka[0])
        A.append(ka[1:])

    counts = [{} for _ in range(n)]
    for i in range(n):
        for a in A[i]:
            counts[i].setdefault(a, 0)
            counts[i][a] += 1

    ans = -1
    for i in range(n):
        for j in range(i + 1, n):
            p = 0
            for k1, v1 in counts[i].items():
                if k1 in counts[j]:
                    p += (v1 / K[i]) * (counts[j][k1] / K[j])
            ans = max(ans, p)

    print(ans)


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
