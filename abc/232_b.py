def main():
    S = list(input())
    T = list(input())
    ans = True
    for i in range(1, len(S)):
        if diff(S[i - 1], S[i]) != diff(T[i - 1], T[i]):
            ans = False
            break
    if ans:
        print('Yes')
    else:
        print('No')


def diff(a, b):
    code_a = ord(a)
    code_b = ord(b)
    if code_a <= code_b:
        return code_b - code_a
    else:
        return ord("z") - code_a + code_b - ord("a") + 1


if __name__ == "__main__":
    main()
