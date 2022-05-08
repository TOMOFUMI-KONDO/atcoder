# import sys

INF = 10 ** 18


def sieve_of_eratosthenes(x):
    nums = [i for i in range(x + 1)]

    root = int(pow(x, 0.5))
    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x + 1):
                if i * j >= x + 1:
                    break
                nums[i * j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


def main():
    N = int(input())
    primes = sieve_of_eratosthenes(int(N ** (1 / 3)))
    l = len(primes)

    ans = 0
    for i in range(l):
        n = N // (primes[i] ** 3)

        # n以下の最大の数のindex
        ok = -1
        ng = i
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if primes[mid] <= n:
                ok = mid
            else:
                ng = mid

        ans += ok + 1

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
