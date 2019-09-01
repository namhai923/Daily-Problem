def word_search(matrix, word):
    count = 0
    for i in range(0, len(matrix)):
        if matrix[0][i] == word[0]:
            for x in range(0,len(matrix)):
                if matrix[x][i] == word[x]:
                    count += 1
                else:
                    count = 0
                    break
            if count == 4:
                return True
        if matrix[i][0] == word[0]:
            for x in range(0,len(matrix)):
                if matrix[i][x] == word[x]:
                    count += 1
                else:
                    count = 0
                    break
            if count == 4:
                return True
    return False

matrix = [['F','A','C','T'],
          ['O','B','Q','P'], 
          ['A','N','O','B'],
          ['M','A','S','S']]

print(word_search(matrix, 'FOAM'))