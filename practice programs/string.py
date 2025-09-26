# Print n copies of a string (no spaces)
s, n = "hello", 4
print(s * n)

# Reverse a string without slicing / built-ins
def reverse_manual(s: str) -> str:
    out = ""
    for ch in s:
        out = ch + out
    return out

# Palindrome (case-insensitive) returning bool
def is_palindrome(s: str) -> bool:
    s = s.lower()
    t = ""
    for ch in s:
        t = ch + t
    return s == t

# Index of substring (manual, no find)
def find_pattern(s: str, p: str) -> int:
    n, m = len(s), len(p)
    for i in range(n - m + 1):
        ok = True
        for j in range(m):
            if s[i + j] != p[j]:
                ok = False
                break
        if ok:
            return i
    return -1
