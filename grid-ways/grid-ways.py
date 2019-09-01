import math

def num_ways(n, m):
    n = n - 1
    m = m - 1
    return int(math.factorial(n+m)/(math.factorial(n)*math.factorial(m)))

print(num_ways(2, 2))