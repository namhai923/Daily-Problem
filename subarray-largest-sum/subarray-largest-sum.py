def max_subarray_sum(arr):
    max_sum = 0
    result = 0
    for number in arr:
        max_sum += number
        if max_sum < 0:
            max_sum = 0
        result = max(result, max_sum)
    return result

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))