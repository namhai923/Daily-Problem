def matrix_spiral_print(M):
    right = len(M[1])
    left = 0
    top = 0
    bottom = len(M)
    while(top < bottom and left < right):
        for x in range(left, right):
            print(M[top][x], end = ' ')
        top += 1
        for x in range(top, bottom):
            print(M[x][right-1], end = ' ')
        right -= 1
        for x in range(right-1,left-1,-1):
            print(M[bottom-1][x],end = ' ')
        bottom -= 1
        for x in range(bottom-1,top-1,-1):
            print(M[x][left], end = ' ')
        left += 1

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)