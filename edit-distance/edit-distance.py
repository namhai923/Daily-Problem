def distanceDynamicProgram(s1, s2):
    edit_num = [[0 for j in range(0,len(s2)+1)]for i in range(0,len(s1)+1)]
    for i in range(0,len(s1)+1):
        for j in range(0,len(s2)+1):
            if i == 0:
                edit_num[i][j] = j
            if j == 0:
                edit_num[i][j] = i
            if i != 0 and j != 0:
                if s1[i-1] != s2[j-1]:
                    edit_num[i][j] = 1 + min(edit_num[i][j-1],
                                                edit_num[i-1][j], 
                                                edit_num[i-1][j-1])
                else:
                    edit_num[i][j] = edit_num[i-1][j-1]
    return edit_num[len(s1)][len(s2)]  

# def distanceRecursive(s1, s2):
#     if len(s1) == 0:
#         return len(s2)
#     if len(s2) == 0:
#         return len(s1)
#     if s1[len(s1)-1] == s2[len(s2)-1]:
#         distanceRecursive(s1[:-1],s2[:-1])
#     return 1 + min(distanceRecursive(s1[:-1],s2),
#                     distanceRecursive(s1,s2[:-1]), 
#                     distanceRecursive(s1[:-1], s2[:-1]))

print(distanceDynamicProgram('biting', 'sitting'))
# print(distanceRecursive('horse', 'ros'))
