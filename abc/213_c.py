import sys

INF = 10 ** 18


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=""):
    print(sep.join(l))


def print_2d_list(l):
    for x in l:
        print_list(x)


def main():
    H, W, N = map(int, input().split())
    X, Y = [], []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    x_dict = {x: i + 1 for i, x in enumerate(sorted(list(set(X))))}
    y_dict = {y: i + 1 for i, y in enumerate(sorted(list(set(Y))))}

    for i in range(N):
        print(x_dict[X[i]], y_dict[Y[i]])


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
