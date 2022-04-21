import math


def main():
    A, B, C, D = map(int, input().split())
    print(math.ceil(A / (C * D - B)) if C * D > B else -1)


if __name__ == "__main__":
    main()
