def findSequence(seq):
    my_set = set()
    longest = 0
    count = 0
    for x in range(0, len(seq)):
        my_set.add(seq[x])
        count += 1 
        if len(my_set) > 2:
            my_set = set()
            if count > longest:
                longest = count
            count = 0
    return longest - 1 

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))