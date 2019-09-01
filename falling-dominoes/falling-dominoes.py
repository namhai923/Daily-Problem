class Solution:
    def pushDominoes(self, dominoes):
        result = list(dominoes)
        for i in range(0,len(dominoes)):
            if dominoes[i] == '.':
                left_count = 0
                right_count = 0
                left_temp = i
                right_temp = i
                while left_temp >= 0:
                    left_count += 1
                    if dominoes[left_temp] == 'R':
                        break
                    if dominoes[left_temp] == 'L':
                        left_count = 0
                        break
                    left_temp -= 1
                    if left_temp < 0:
                        left_count = 0
                        break
                while right_temp < len(dominoes):
                    right_count += 1
                    if dominoes[right_temp] == 'L':
                        break
                    if dominoes[right_temp] == 'R':
                        right_count = 0
                        break
                    right_temp += 1
                    if right_temp > len(dominoes)-1:
                        right_count = 0
                        break
                if right_count == 0 and left_count != 0:
                    result[i] = 'R'
                if left_count == 0 and right_count != 0:
                    result[i] = 'L'
                elif right_count != 0 and left_count != 0:
                    if left_count > right_count:
                        result[i] = 'L'
                    if left_count < right_count:
                        result[i] = 'R'
        return ''.join(result)

print(Solution().pushDominoes('..R...L..R.'))