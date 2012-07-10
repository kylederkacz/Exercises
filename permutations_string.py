def permutations(original, partial=''):
    if len(partial) == len(original):
        print partial
        return

    for c in original:
        if c in partial:
            continue
        permutations(original, partial + c)


if __name__ == "__main__":
    permutations('ABCDE')
