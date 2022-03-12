import sys

S = []


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def word(s, n):
    n %= 3
    for _ in range(n):
        if s == "A":
            s = "B"
        elif s == "B":
            s = "C"
        else:
            s = "A"

    return s


def f(t, k):
    if t == 0:
        return S[k]

    if k == 0:
        return word(S[0], t)

    return word(f(t - 1, k // 2), k % 2 + 1)


def main():
    global S
    S = list(input())
    Q = int(input())

    for i in range(Q):
        t, k = map(int, input().split())
        print(f(t, k - 1))


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
