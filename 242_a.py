import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    elif x <= b:
        print(c / (b - a))
    else:
        print(0)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
