import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    takahashi = "Takahashi"
    aoki = "Aoki"

    a, b, c, d = map(int, input().split())

    if a < c:
        print(takahashi)
    elif a == c:
        if b <= d:
            print(takahashi)
        else:
            print(aoki)
    else:
        print(aoki)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
