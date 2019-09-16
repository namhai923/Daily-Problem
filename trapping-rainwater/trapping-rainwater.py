def capacity(arr):
    max_height = 0
    rainwater = 0
    left_max = []
    right_max = []
    for height in arr:
        if height >= max_height:
            max_height = height
        left_max.append(max_height)
    max_height = 0
    for i in range(len(arr)-1, 0-1, -1):
        if arr[i] >= max_height:
            max_height = arr[i]
        right_max.insert(0, max_height)
    for i in range(0, len(arr)):
        rainwater += min(left_max[i], right_max[i]) - arr[i]
    return rainwater

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))