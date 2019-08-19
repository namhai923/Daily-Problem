class Solution:
    def lengthOfLongestSubstring(self,s):
        longest = 0
        substring = []
        letter_index = 0
        while letter_index < len(s):
            substring.append(s[letter_index])
            if(len(set(substring)) < len(substring)):
                letter_index -= 1
                if(len(set(substring)) > longest):
                    longest = len(set(substring))
                substring = []
            letter_index += 1
        return longest


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))