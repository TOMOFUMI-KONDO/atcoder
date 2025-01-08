# import sys

INF = 10**18


def main():
    L, R = map(int, input().split())
    
    print(f(R) - f(L-1))
    
def f(R):
    n = len(str(R))
    d = []
    for i in range(n):
        d.append(int(str(R)[i]))

    count = 0

    R_is_hebi = True
    for i in range(1, n):
        if int(d[i]) >= d[0]:
            R_is_hebi = False
            break
    if R_is_hebi:
        count += 1

    for k in range(n-1):
        if k>=1:
            zero = False
            for i in range(1,k+1):
                if int(d[0]) <= int(d[i]):
                    zero = True
                    break
            if zero:
                continue

        count += min(d[0], d[k+1]) * d[0] ** (n-k-2)

    for i in range(1, d[0]):
        count += i ** (n-1)

    for k in range(1, n):
        for i in range(1, 10):
            count += i ** (k-1)

    return count


        
    

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
