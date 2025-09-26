# Average of non-negative numbers in a list
def avg_nonneg(arr):
    total = 0
    cnt = 0
    for v in arr:
        if v >= 0:
            total += v
            cnt += 1
    return 0.0 if cnt == 0 else total / cnt
