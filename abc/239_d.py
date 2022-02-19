import sys


def is_prime(num):
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    return not flag


def main():
    # N = int(input())
    A, B, C, D = map(int, input().split())
    # A = list(map(int, input().split()))
    for i in range(A, B + 1):
        prime_exist = False
        for j in range(C, D + 1):
            if is_prime(i + j):
                prime_exist = True
                break
        if not prime_exist:
            print('Takahashi')
            return
    print('Aoki')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
