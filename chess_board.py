# write an algorithm to print a chessboard pattern('b' for black square, 'w' for white squares) the input consists of an integer inputNum, representing the size of the chessboard(N) output print N lines of N space -seperated characters 'B' or  'W' where each line corresponds to one row of the board
# Here is an algorithm to print a chessboard pattern:

# Read the size of the chessboard N from the user.
# Create a variable color and initialize it to 'B'.
# Loop through each row of the chessboard:
# Loop through each column of the chessboard:
# Print the value of color.
# If color is 'B', change it to 'W'. Otherwise, change it to 'B'.
# Print a newline character to move to the next row.
# Exit the program.
# Here is the algorithm in pseudo-code:


# Input: inputNum (size of the chessboard)
def chess_board(N):
    color = 'B'

    for row in range(N):
        for col in range(N):
            print(color, end=' ')
            if color == 'B':
                color = 'W'
            else:
                color = 'B'
       
        print()

# Note: This algorithm assumes that the chessboard has square dimensions (i.e., N rows and N columns). If the dimensions are not square, the algorithm will produce an incomplete or irregular chessboard pattern.

chess_board(8)

def chess_board(N):
    color = 'B'
    result = ""

    for row in range(N):
        for col in range(N):
            result += color + " "
            if color == 'B':
                color = 'W'
            else:
                color = 'B'
        result += "\n"

    return result


