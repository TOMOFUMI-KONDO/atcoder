import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    numbers = [i + 1 for i in range(2 * N + 1)]
    while True:
        print(numbers.pop(0))
        n = int(input())
        if n == 0:
            break
        numbers.remove(n)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
