import sys
from collections import deque


def main():
    N = int(input())
    A = list(map(int, input().split()))

    stack = deque()
    stack_cnt = 0

    for a in A:
        if stack_cnt == 0:
            stack.append([a, 1])
            stack_cnt += 1
            print(1)
            continue

        last, consecutive = stack.pop()
        if a == last:
            if consecutive == a - 1:
                stack_cnt -= consecutive
            else:
                stack.append([last, consecutive + 1])
                stack_cnt += 1

        else:
            stack.append([last, consecutive])
            stack.append([a, 1])
            stack_cnt += 1

        print(stack_cnt)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
