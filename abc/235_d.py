costs = {}
a = 0


def shift(l):
    tmp = l[0]
    l = l[1:]
    l.append(tmp)
    return l


def cost(current):
    global costs, a
    if current % a == 0:
        nex = current // a
        if nex not in costs or costs[nex] > costs[current] + 1:
            costs[nex] = costs[current] + 1
            cost(nex)

    l = list(str(current))
    if current > 10 and l[1] != "0":
        nex = int(''.join(shift(l)))
        if nex not in costs or costs[nex] > costs[current] + 1:
            costs[nex] = costs[current] + 1
            cost(nex)


def main():
    global costs, a

    a, N = map(int, input().split())
    costs[N] = 0
    cost(N)

    if 1 in costs:
        print(costs[1])
    else:
        print(-1)


if __name__ == "__main__":
    main()
