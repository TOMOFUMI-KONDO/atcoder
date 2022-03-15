all: main.py

define TEMPLATE
import sys

INF = 10**18

def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()
endef
export TEMPLATE

main.py:
	echo "$$TEMPLATE" > main.py

clean:
	rm -f main.py