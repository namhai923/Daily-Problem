def findPythagoreanTriplets(nums):
    list_square = [x*x for x in nums]    
    for target in list_square:
        set_square = set()
        for number in list_square:
            if target - number in set_square:
                return True
            else:
                set_square.add(number)
    return False

print(findPythagoreanTriplets([3,12,5,13]))