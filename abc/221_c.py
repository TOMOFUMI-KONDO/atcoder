import itertools
import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = list(map(int, list(input())))
    indices = [i for i in range(len(N))]
    ans = 0
    for i in range(1, len(N) // 2 + 1):
        for c in itertools.combinations(indices, i):
            if len(c) == 0 or len(c) == len(N):
                continue

            left, right = [], []
            for j in range(len(N)):
                if j in c:
                    left.append(N[j])
                else:
                    right.append(N[j])

            left.sort(reverse=True)
            right.sort(reverse=True)
            if left[0] == 0 or right[0] == 0:
                continue

            left_num = int("".join([str(integer) for integer in left]))
            right_num = int("".join([str(integer) for integer in right]))

            ans = max(ans, left_num * right_num)
    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
