# import sys

INF = 10 ** 18


def main():
    N, M = map(int, input().split())
    S = input()
    C = list(map(int, input().split()))

    C_with_count = []
    color_index = {i: [] for i in range(M)}
    color_count = {i: 0 for i in range(M)}
    for i in range(N):
        c = C[i] - 1
        C_with_count.append((c, color_count[c]))
        color_index[c].append(i)
        color_count[c] += 1

    for i in range(N):
        cnt = C_with_count[i][1]
        if cnt == 0:
            print(S[color_index[C[i] - 1][-1]], end="")
        else:
            print(S[color_index[C[i] - 1][cnt - 1]], end="")

    print()


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
