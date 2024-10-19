chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

#print(chess_board)
"""""
print(chess_board[0], "\n")
print(chess_board[1], "\n")
# así hasta el 8
print(chess_board[8], "\n")
# o mejor con for
"""""
for fila in chess_board:
    print(fila, "\n")
print("\n")
print("\n")

# y así con while
i = 0
while i < len(chess_board):
    print(chess_board[i], "\n")
    i += 1

print(chess_board[5][0])
print(chess_board[5][2])
print(chess_board[6][3])