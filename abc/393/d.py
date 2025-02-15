# import sys

INF = 10**18


def main():
    _ = int(input())
    S = input()

    sizes = [0, 0]
    counts = [0, 0]
    ans = 0
    first = S.index("1")
    last = S.rindex("1")
    if first == last:
        print(0)
        return

    ok_i = first
    ok_j = last
    i = first
    j = last
    while ok_i < ok_j:
        if sizes[0] <= sizes[1]:
            s = S[i]
            if s == "0":
                counts[0] += 1
            elif s == "1":
                ans += sizes[0] * counts[0]
                ok_i = i
                counts[0] = 0
                sizes[0] += 1
            i += 1
        else:
            s = S[j]
            if s == "0":
                counts[1] += 1
            elif s == "1":
                ans += sizes[1] * counts[1]
                ok_j = j
                counts[1] = 0
                sizes[1] += 1
            j -= 1

    print(ans)


def judge(cond, yes="Yes", no="No"):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
