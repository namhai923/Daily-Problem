def first_missing_positive(nums):
    nums = list(set(nums))
    check_num = 0
    for i in range(0, len(nums)-1):
        if nums[i] > 0:
            check_num += 1 
            if nums[i] != check_num:
                return check_num
    return nums[-1] + 1

print(first_missing_positive([1,2,0]))