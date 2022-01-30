def main():
    S = list(input())
    i = 0
    while i < len(S) // 2:
        if S[i] == "a" and S[len(S) - i - 1] == "a":
            i += 1
        else:
            break
    S = S[i:len(S) - i]

    i = 0
    while i < len(S):
        if S[len(S) - i - 1] != "a":
            break
        i += 1
    S = S[:len(S) - i]

    result = True
    i = 0
    while i < len(S) // 2:
        if S[i] == S[len(S) - i - 1]:
            i += 1
        else:
            result = False
            break

    if result:
        print('Yes')
    else:
        print('No')
    # S1 = S[:len(S) // 2]
    # if len(S) % 2 == 1:
    #     S2 = S[:len(S) + 1 // 2]
    # else:
    #     S2 = S[:len(S) // 2]
    #
    # S2.reverse()
    #
    # result = True
    # for i in range(len(S1)):
    #     if S1[i] != S2[i]:
    #         result = False
    #         break


if __name__ == "__main__":
    main()
