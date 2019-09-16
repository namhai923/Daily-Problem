class Solution:
    def buddyStrings(self, A, B):
        swap_index = []
        A = list(A)
        B = list(B)
        if len(A) == len(B):
            for i in range(0, len(A)):
                if A[i] != B[i]:
                    swap_index.append(i)
            if len(swap_index) == 2:
                A[swap_index[0]], A[swap_index[1]] = A[swap_index[1]], A[swap_index[0]]
            for i in range(0, len(A)):
                if A[i] != B[i]:
                    return False
            return True
        return False
        

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))