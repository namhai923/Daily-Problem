# def buy_and_sell(arr):
#     result = 0
#     for i in range(len(arr)-1, 0-1, -1):
#         for x in range(i-1, 0-1, -1):
#             result = max(result, arr[i]-arr[x])
#     if result <= 0:
#         return 0 
#     return result

def buy_and_sell(arr):
    max_index = 0
    min_index = 0
    result = 0
    for i in range(0,len(arr)):
        if(arr[i] >= arr[max_index]):
            max_index = i
        if(arr[i] <= arr[min_index]):
            min_index = i
            max_index = i
        if min_index <= max_index:
            result = max(result, arr[max_index] - arr[min_index])
    return result

print(buy_and_sell([9, 11, 8, 5, 7, 10]))