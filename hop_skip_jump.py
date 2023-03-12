# Lucy loves to play Hop,Skip, abd jump game. Given an N*M matrix and starting from cell(1,2) here challenge is to hop in an anti-clockwise direction and skip alternate cells, the goal is to find out the last cell she would hop onto.
# write an algorithem to find the last cell lucy would hop onto after moving anti-clockwise and skipping alternate cells.
# input : martrix_row and matrix_col ,representing the number of rows (N) and the number of columns(M) in the matrix, respectively the next M lines consist of N space-sepatated integers representing the elements in each cell of the matrix
# output print an integer representing the last cell Lucy would hop onto after follwing the given instructions

# Example
# input

# 3 3
# 29 8 37
# 15 41 3
# 1 10 14

# Output: 41

# Explanation: Lucy starts with 29, skip 15, hop onto 1, skip 10, hop onto 14
# skip 3, hop onto 37, skip 8 and finally hops onto 41,
# so the output is 41

def hop_skip_jump(matrix_row, matrix_col, matrix):
    i, j, row, col = 1, 2, matrix_row, matrix_col
    count = 0
    skip = False

    while count < row*col:
        if skip:
            skip = False
            continue

        print(matrix[i-1][j-1], end=' ')
        count += 1

        if count == row*col:
            break

        if i == 1 and j < col:
            direction = 'right'
        elif i == 1 and j == col:
            direction = 'down'
        elif i > 1 and j == col:
            direction = 'left'
        elif i == row and j > 2:
            direction = 'up'
        elif i == row and j == 2:
            break
        elif j % 2 == 0:
            if i == 2:
                direction = 'left'
            else:
                direction = 'right'
        else:
            if i == row-1:
                direction = 'up'
            else:
                direction = 'down'

        if direction == 'right':
            j += 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        elif direction == 'up':
            i -= 1

        if i < 1 or i > row or j < 1 or j > col or matrix[i-1][j-1] == -1:
            if direction == 'right':
                j -= 1
                i += 1
            elif direction == 'down':
                i -= 1
                j -= 1
            elif direction == 'left':
                j += 1
                i -= 1
            elif direction == 'up':
                i += 1
                j += 1

            direction = ''

        if direction != '':
            skip = True

    print(matrix[i-1][j-1])

# Sample Input:
matrix_row, matrix_col = 3, 3
matrix = [[29, 8, 37], [15, 41, 3], [1, 10, 14]]

# Function call
hop_skip_jump(matrix_row, matrix_col, matrix)

# Output: 41