import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    included = [False] * 2001
    for a in A:
        included[a] = True
    for i in range(len(included)):
        if not included[i]:
            print(i)
            return


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
