nested_comprehention = [[1 if item_idx == row_idx else 0 for item_idx in range(0, 3)] for row_idx in range(0, 3)]

if __name__ == "__main__":
    print nested_comprehention