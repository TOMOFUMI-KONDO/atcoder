def main():
    N, M = in_ints()
    S = in_strs()
    T = in_strs()

    ans = []
    cnt = 0
    for s in S:
        if s == T[cnt]:
            ans.append('Yes')
            cnt += 1
        else:
            ans.append('No')

    for a in ans:
        print(a)


def in_int():
    return int(input())


def in_ints():
    return map(int, input().split())


def in_strs():
    return input().split()


if __name__ == "__main__":
    main()
