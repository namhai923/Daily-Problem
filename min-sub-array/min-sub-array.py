class Solution:
    def minSubArrayLen(self, nums, s):
        min_len = []
        for x in range(0, len(nums)):
            result = 0
            count = 0
            while x < len(nums):
                result += nums[x]
                count += 1
                x += 1
                if result >= s:
                    min_len.append(count)
                    break
        if len(min_len) == 0:
            return 0
        return min(min_len)

print(Solution().minSubArrayLen([2,3,1,2,4,3],7))