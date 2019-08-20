class Solution:
    def getRange(self, arr, target):
        result = []
        start = 0
        end = 0
        try:
            start = arr.index(target)
        except ValueError:
            start = -1
        i = len(arr) - 1
        while i >=0:
            if arr[i] == target:
                end = i
                break
            end = -1
            i -= 1
        result.append(start)
        result.append(end)
        return result

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr,x))