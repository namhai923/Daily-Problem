def staircaseRecursively(n):
    if n == 0 or n == 1:
        return 1
    else:
        return staircaseRecursively(n-1) + staircaseRecursively(n-2)
    
def staircaseIteratively(n):
    a = 1
    b = 1
    if n == 0 or n == 1:
        return 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
        

print(staircaseIteratively(4))
print(staircaseRecursively(5))