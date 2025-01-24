# import sys

INF = 10**18


def main():
    cards = list(map(int, input().split()))
    cards.sort()

    if cards[0] == cards[1] == cards[2] == cards[3]:
        print("No")
    elif cards[0] == cards[1] == cards[2] and cards[3] != cards[0]:
        print("Yes")
    elif cards[0] != cards[1] and cards[1] == cards[2] == cards[3]:
        print("Yes")
    elif cards[0] == cards[1] and cards[2] == cards[3] and cards[0] != cards[2]:
        print("Yes")
    else:
        print("No")


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
