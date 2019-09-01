def witnesses(heights):
    count = 0
    for i in range(0, len(heights)-1):
        witness = True
        for j in range(i+1, len(heights)):
            if heights[i] <= heights[j]:
                witness = False
                break
        if witness:
            count += 1
    return count + 1 

# def witnesses(heights):
#     count = 0
#     while True:
#         count += 1
#         highest = max(heights)
#         highest_index = heights.index(highest)
#         heights = heights[highest_index+1:]
#         if len(heights) == 1:
#             break
#     return count + 1      

print(witnesses([3, 6, 3, 4, 1]))