# import sys

INF = 10**18


def main():
    D = input()
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))

    if D == "N":
        print("S")
    elif D == "S":
        print("N")
    elif D == "E":
        print("W")
    elif D == "W":
        print("E")
    elif D == "NE":
        print("SW")
    elif D == "NW":
        print("SE")
    elif D == "SE":
        print("NW")
    elif D == "SW":
        print("NE")


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
