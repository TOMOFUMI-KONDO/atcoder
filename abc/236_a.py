def main():
    S = list(input())
    a, b = map(int, input().split())
    tmp = S[a - 1]
    S[a - 1] = S[b - 1]
    S[b - 1] = tmp
    print("".join(S))


if __name__ == "__main__":
    main()
