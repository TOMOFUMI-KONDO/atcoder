import sys
from collections import deque

INF = 10 ** 18


def main():
    Q = int(input())

    d = deque()
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            d.append([query[1], query[2]])
        else:
            sum_ = 0

            c = query[1]
            while c > 0:
                head = d.popleft()
                if c <= head[1]:
                    d.appendleft([head[0], head[1] - c])
                    sum_ += head[0] * c
                    break
                else:
                    c -= head[1]
                    sum_ += head[0] * head[1]

            print(sum_)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
