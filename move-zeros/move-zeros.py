class Solution:
    def moveZeros(self, nums):
        curr_len = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                curr_len += 1
            if nums[i] != 0:
                nums[i], nums[i - curr_len] = nums[i - curr_len], nums[i]
        
nums = [0,1,0,3,12]
Solution().moveZeros(nums)
print(nums)