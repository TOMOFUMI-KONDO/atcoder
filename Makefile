all: main.py

define TEMPLATE
# import sys

INF = 10**18


def main():
    N = int(input())
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))


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
endef
export TEMPLATE

main.py:
	echo "$$TEMPLATE" > main.py

clean:
	rm -f main.py