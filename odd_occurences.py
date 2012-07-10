
def find_odd_occurrences(l):
    l_count = {}
    for item in l:
        if item not in l_count:
            l_count[item] = 0
        l_count[item] += 1

    for key, count in l_count.iteritems():
        if count % 2 != 0:
            return key


def find_odd_occurrences_sort(l):
    l.sort()
    prev = None
    current_count = 0
    for item in l:
        if item != prev and prev is not None:
            if current_count % 2 != 0:
                return prev
            current_count = 0
        current_count += 1
        prev = item

    if current_count % 2 != 0:
        return prev

    return None


def find_odd_occurrences_xor(l):
    c = 0
    for item in l:
        c = item ^ c
    return c

if __name__ == "__main__":
    print find_odd_occurrences([1, 2, 2, 3, 3, 4, 4, 4, 1])
    print find_odd_occurrences_sort([1, 2, 2, 3, 3, 4, 4, 4, 1])
    print find_odd_occurrences_xor([1, 2, 2, 3, 3, 3, 4, 4, 1])
