# Frequency map & most frequent element (mode)
def mode(arr):
    freq = {}
    best_v, best_c = None, 0
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] > best_c:
            best_v, best_c = x, freq[x]
    return best_v, best_c
