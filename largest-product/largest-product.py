def maximum_product_of_three(lst):
    lst = sorted(lst)
    return max(lst[0]*lst[1]*lst[-1], lst[-1]*lst[-2]*lst[-3])

print(maximum_product_of_three([-4,-4,2,8]))