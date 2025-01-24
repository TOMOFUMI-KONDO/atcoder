# import sys

INF = 10**18


def main():
    _ = int(input())
    S = list(input())
    T = list(input())

    if abs(len(S) - len(T)) >= 2:
        print("No")
        return

    diff = 0
    if len(S) == len(T):
        for i in range(len(S)):
            if S[i] != T[i]:
                diff += 1
        if diff > 1:
            print("No")
            return
        print("Yes")
        return

    if len(S) > len(T):
        S, T = T, S

    s, t = 0, 0
    diff = 0
    for i in range(len(S)):
        if S[s] == T[t]:
            s += 1
            t += 1
            continue
        elif diff > 0:
            print("No")
            return
        else:
            t += 1
            diff += 1

    print("Yes")


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
