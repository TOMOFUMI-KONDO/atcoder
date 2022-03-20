import sys
import heapq


# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
#
# class BinarySearchTree:
#     def __init__(self, key):
#         self.root = Node(key)
#
#     def search(self, key):
#         node = self.root
#         while node:
#             if node.key == key:
#                 return node
#             elif node.key > key:
#                 node = node.left
#             else:
#                 node = node.right
#         return None
#
#     def insert(self, key):
#         node = self.root
#         while node:
#             parent = node
#             if node.key > key:
#                 node = node.left
#                 flag = "left"
#             else:
#                 node = node.right
#                 flag = "right"
#         new = Node(key)
#         if flag == "left":
#             parent.left = new
#         else:
#             parent.right = new


def main():
    A = []
    Q = int(input())
    heapq.
    for _ in range(Q):
        query = list(input())
        if query[0] == '1':
            A.append()
        elif query[0] == '2':
            pass
        elif query[0] == '3':
            pass


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
