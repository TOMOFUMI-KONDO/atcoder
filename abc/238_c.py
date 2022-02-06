mod = 998244353


def main():
    N_str = input()
    N = int(N_str)
    digits = len(N_str)
    ans = 0
    for i in range(1, digits + 1):
        if i != digits:
            k = 9 * 10 ** (i - 1)
        else:
            k = N - 10 ** (i - 1) + 1
        ans = ans + (k * (k + 1)) // 2
    print(ans % mod)


if __name__ == "__main__":
    main()
