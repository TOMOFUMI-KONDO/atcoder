.PHOYNY: all
all: main.py main.cpp

define TEMPLATE_PYTHON
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
export TEMPLATE_PYTHON

main.py:
	echo "$$TEMPLATE_PYTHON" > main.py

define TEMPLATE_CPP
#include <bits/stdc++.h>
using namespace std;

#define INF 1e18
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
  int N;
  cin >> N;
  /* int N, M; */
  /* cin >> N >> M; */
  /* vector<int> A(N); */
  /* rep(i, N) cin >> A[i]; */
}
endef
export TEMPLATE_CPP

main.cpp:
	echo "$$TEMPLATE_CPP" > main.cpp

.PHONY: runcpp
runcpp:
	clang++ main.cpp && ./a.out
	rm -f a.out

.PHONY: clean
clean:
	rm -f main.{py,cpp}
