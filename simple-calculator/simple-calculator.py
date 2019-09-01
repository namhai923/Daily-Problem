def eval(expression):
    result = ''
    operations = []
    post_fix = []
    for x in range(0,len(expression)):
        if expression[x].isdigit():
            post_fix.append(expression[x])
        elif expression[x] == ')':
            while(operations[len(operations)-1] != '('):
                post_fix.append(operations[len(operations)-1])
                operations.pop()
            operations.pop()
        else:
            operations.append(expression[x])
    while(len(operations) != 0):
        post_fix.append(operations[len(operations)-1])
        operations.pop()
    x = 0
    while(len(post_fix) > 2):
        if post_fix[x] == '+':
            post_fix[x-2] = str(int(post_fix[x-2]) + int(post_fix[x-1]))
            post_fix.pop(x)
            post_fix.pop(x-1)
            x -= 2
        if post_fix[x] == '-':
            post_fix[x-2] = str(int(post_fix[x-2]) - int(post_fix[x-1]))
            post_fix.pop(x)
            post_fix.pop(x-1)
            x -= 2
        x += 1
    if len(post_fix) == 2:
        result = post_fix[1] + post_fix[0]
    if len(post_fix) == 1:
        result = post_fix[0]
    return result

print(eval('-(3+(2-1))'))