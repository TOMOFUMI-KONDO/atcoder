# import sys

INF = 10 ** 18


def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]

    # ranges={i:[-1,-1] for i in range(1,2*10**5)}
    ranges = {}

    for l, r in LR:
        ranges.setdefault(l, r)
        ranges[l] = max(ranges[l], r)

    ans = []
    keys = sorted(ranges.keys())
    i = 0
    l = keys[0]
    r = ranges[l]
    while True:
        if i > len(keys) - 1:
            break

        r = max(r, ranges[keys[i]])
        if i == len(keys) - 1:
            ans.append([l, r])
            break

        if r < keys[i + 1]:
            # print(i, l, r)
            ans.append([l, r])
            i += 1
            l = keys[i]
            continue

        while True:
            i += 1

            r = max(r, ranges[keys[i]])
            if i == len(keys) - 1:
                ans.append([l, r])
                i += 1
                break

            if keys[i + 1] > r:
                # print(i, l, r)
                ans.append([l, r])
                i += 1
                l = keys[i]
                break

    print_2d_list(ans)


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
