# import sys

INF = 10 ** 18


def make_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisor = [i]

            if i != n // i:
                divisor.append(n // i)
            else:
                divisor.append(i)

            divisors.append(divisor)
        i += 1
    return divisors


def main():
    N = int(input())
    A = list(map(int, input().split()))

    cnt = {i: 0 for i in range(2 * 10 ** 5 + 1)}
    for a in A:
        cnt[a] += 1

    ans = 0

    for a in A:
        divs = make_divisors(a)
        for d in divs:
            if d[0] != d[1]:
                ans += cnt[d[0]] * cnt[d[1]] * 2
            else:
                ans += cnt[d[0]] * cnt[d[1]]

    print(ans)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
