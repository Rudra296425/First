def two_sum(arr, k):
    seen = {}
    for i, x in enumerate(arr):
        if k - x in seen:
            return (seen[k - x], i)
        seen[x] = i
    return -1
