def check(lst):
    count = 0
    for i in range(0, len(lst) - 1):
        if lst[i] >= lst[i+1]:
            count += 1
    if count == 1:
        return True
    return False

print(check([13, 4, 7]))

print(check([5,1,3,2,5]))