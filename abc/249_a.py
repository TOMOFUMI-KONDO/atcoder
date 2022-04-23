# import sys

INF = 10 ** 18


def main():
    a, b, c, d, e, f, x = map(int, input().split())

    t = x // (a + c)
    t_d = b * a * t
    t_r = t_d + min((x - t * (a + c), a)) * b

    ao = x // (d + f)
    ao_d = e * d * ao
    ao_r = ao_d + min((x - ao * (d + f), d)) * e

    if t_r == ao_r:
        print("Draw")
    elif t_r > ao_r:
        print("Takahashi")
    else:
        print("Aoki")


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
