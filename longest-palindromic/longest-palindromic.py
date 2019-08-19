class Solution:
    def longestPalindrome(self, s):
        longest_pal = ""
        result = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(0, len(s)):
            result[i][i] = 1
        for curr_len in range(2, len(s) + 1) :
            for start in range(0, len(s)):
                end = start + curr_len - 1
                if end >= len(s):
                    break
                else:
                    if curr_len == 2:
                        if s[start] == s[end]:
                            result[start][end] = curr_len
                        else:
                            result[start][end] = 0
                    else:
                        if result[start+1][end-1] != 0 and s[start] == s[end]:
                            result[start][end] = curr_len
                            longest_pal = s[start:end+1:1]
                        else:
                            result[start][end] = 0
        return longest_pal
                
s = "million banana"
print(str(Solution().longestPalindrome(s)))