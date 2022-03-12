import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    S = list(input())
    S.sort()
    print("".join(S))


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
