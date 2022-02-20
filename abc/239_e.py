import sys
from copy import copy

tree = []
leaves = []
orders = []


def remove_parent(child, parent):
    global tree, leaves

    if child != 0:
        tree[child][2] = parent
        tree[child][1].remove(parent)

    if len(tree[child][1]) == 0:
        leaves.append(child)
        return

    for c in tree[child][1]:
        remove_parent(c, child)


def set_order(n):
    global orders

    children = tree[n][1]
    child_orders = [[tree[n][0]]]
    for c in children:
        if orders[c] is None:
            set_order(c)
        child_orders.append(copy(orders[c]))
    parent_order = []
    for i in range(20):
        if len(child_orders) == 0:
            break

        max_ = 0
        max_i = 0
        for i in range(len(child_orders)):
            co = child_orders[i]
            if co[0] > max_:
                max_ = co[0]
                max_i = i
        parent_order.append(max_)
        child_orders[max_i].pop(0)
        if len(child_orders[max_i]) == 0:
            child_orders.pop(max_i)

    orders[n] = parent_order


def main():
    global tree, orders

    N, Q = map(int, input().split())
    X = list(map(int, input().split()))

    tree = [[x, [], None] for x in X]  # value, children, parent
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        tree[a][1].append(b)
        tree[b][1].append(a)

    remove_parent(0, None)

    orders = [None] * N
    set_order(0)

    for _ in range(Q):
        v, k = map(int, input().split())
        print(orders[v - 1][k - 1])


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
