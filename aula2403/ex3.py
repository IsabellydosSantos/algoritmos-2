def rec(n):
    if n == 10:
        return 1
    return 1 + rec(n+1)


n = 6
print(rec(n))