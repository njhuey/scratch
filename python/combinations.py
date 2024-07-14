def combinations(n):
    row = [[i] for i in range(n)]
    results = []
    results += row
    for _ in range(n - 1):
        new_row = []
        for combination in row:
            for i in range(combination[-1] + 1, n):
                new_row.append(combination + [i])
        results += new_row
        row = new_row

    return results


if __name__ == "__main__":
    print(combinations(5))
