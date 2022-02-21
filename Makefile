all: main.py

define TEMPLATE
import sys

sys.setrecursionlimit(10**6)

N = int(input())
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
endef
export TEMPLATE

main.py:
	echo "$$TEMPLATE" > main.py

clean:
	rm -f main.py