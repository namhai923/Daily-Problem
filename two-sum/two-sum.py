def twoSum(nums, target):
    s = set()
    for i in nums:
        temp = target - i
        if(temp in s):
            return True
        s.add(i)
    return False


print(twoSum([4,7,1,-3,2], 5))