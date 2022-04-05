def binary_search(l, n):
    ok = 0
    ng = len(l)

    while ng - ok > 1:
        mid = (ok + ng) // 2
        if l[mid] <= n:
            ok = mid
        else:
            ng = mid

    if l[ok] == n:
        return ok
    else:
        return -1


if __name__ == "__main__":
    list_ = [1, 4, 34, 67, 73, 665, 252345]
    target = 73
    print(binary_search(list_, 73))  # want 4
