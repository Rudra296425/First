# Generator: even numbers up to n
def evens(n):
    x = 0
    while x <= n:
        yield x
        x += 2
