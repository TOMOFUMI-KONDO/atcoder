def bit_full_search(n):
    """
    bit_full_search returns all subsets of list having n elements.
    """

    subsets = []

    for mask in range(1 << n):
        subset = []

        for i in range(n):
            if 1 << i & mask > 0:
                subset.append(i)

        subsets.append(subset)

    return subsets


if __name__ == "__main__":
    print(bit_full_search(3))
