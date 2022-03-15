import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    S = list(input())
    i = 0
    prev = ''
    while i < N:
        if prev == 'B' and S[i] == 'A':
            print('A', end='')
            prev = 'B'
        elif prev == 'B' and S[i] == 'B':
            prev = 'A'
        else:
            print(prev, end='')
            prev = S[i]
        i += 1
    print(prev)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
