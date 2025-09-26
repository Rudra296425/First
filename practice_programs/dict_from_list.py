# Build dict from list of (name, marks) tuples
def create_dict(arr):
    d = {}
    for name, marks in arr:
        d[name] = marks
    return d
