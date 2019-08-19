class Solution:
    def isValid(self, s):
        result = []
        if len(s) % 2 != 0:
            return False
        else:
            for char in list(s):
                try:
                    if char == "(" or char =="{" or char =="[":
                        result.append(char)
                    else:
                        if char ==")" and result[len(result) - 1] == "(":
                            result.remove(result[len(result) - 1])
                        if char =="]" and result[len(result) - 1] == "[":
                            result.remove(result[len(result) - 1])
                        if char =="}" and result[len(result) - 1] == "{":
                            result.remove(result[len(result) - 1])
                except ValueError:
                    return False
            print(result)
            if result == []:
                return True
            else:
                return False

s = "()(){(())"
print(Solution().isValid(s))

s = ""
print(Solution().isValid(s))

s = "([{}])()"
print(Solution().isValid(s))
