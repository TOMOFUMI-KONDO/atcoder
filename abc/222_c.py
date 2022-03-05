import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def janken(a, b):
    if a == b:
        return 0
    if (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 1
    else:
        return -1


def main():
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(N * 2)]

    ranking = [{"id": i, "cnt": 0} for i in range(N * 2)]
    for i in range(M):
        for j in range(N):
            result = janken(A[ranking[2 * j]["id"]][i], A[ranking[2 * j + 1]["id"]][i])
            if result == 1:
                ranking[2 * j]["cnt"] += 1
            elif result == -1:
                ranking[2 * j + 1]["cnt"] += 1

        ranking.sort(key=lambda x: x["id"])
        ranking.sort(key=lambda x: x["cnt"], reverse=True)

    for r in ranking:
        print(r["id"] + 1)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
