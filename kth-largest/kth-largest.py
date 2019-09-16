def findKthLargest(nums, k):
    while len(nums) > k:
        nums.remove(min(nums))
    return min(nums)

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))