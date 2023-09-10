def nearestInteger(n, m):
    r = n % m
    if r <= m // 2:
        value = n - r
    else:
        value = n + (m - r)
    return value

n = 7
m = 4
value = nearestInteger(n, m)
print(value)
