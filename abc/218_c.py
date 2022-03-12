import copy
import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    T = trim([list(input()) for _ in range(N)])

    for _ in range(4):
        trimmed = trim(S)
        if same(trimmed, T):
            print("Yes")
            return

        S = rotate(S)

    print("No")


def trim(S):
    trimmed = copy.deepcopy(S)
    while len(trimmed) > 0:
        if "#" in trimmed[0]:
            break
        trimmed.pop(0)
    while len(trimmed):
        if "#" in trimmed[-1]:
            break
        trimmed.pop(-1)

    trimmed = rotate(trimmed)
    while len(trimmed) > 0:
        if "#" in trimmed[0]:
            break
        trimmed.pop(0)
    while len(trimmed):
        if "#" in trimmed[-1]:
            break
        trimmed.pop(-1)

    for _ in range(3):
        trimmed = rotate(trimmed)

    return trimmed


def same(S, T):
    if len(S) != len(T):
        return False

    for i in range(len(S)):
        if len(S[i]) != len(T[i]):
            return False

        for j in range(len(S[0])):
            if S[i][j] != T[i][j]:
                return False

    return True


def rotate(S):
    N = len(S)
    M = len(S[0])

    new_S = []
    for i in range(M):
        row = []
        for j in range(len(S)):
            row.append(S[N - 1 - j][i])
        new_S.append(row)
    return new_S


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
