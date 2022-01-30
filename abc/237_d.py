from collections import deque


def main():
    N = int(input())
    A = deque([N])
    S = list(input())

    for i in range(N - 1, -1, -1):
        if S[i] == "L":
            A.append(i)
        else:
            A.appendleft(i)

    A = [str(n) for n in A]
    print(" ".join(A))


if __name__ == "__main__":
    main()
