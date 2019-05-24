SIZE = 9

board =[[0 for x in range(SIZE)] for y in range(SIZE)]

def initializeBoard(board, inputs):
	i = 0
	j = 0
	for index, data in enumerate(inputs):
		i = index // 9
		j = index % 9
		board[i][j] = data

def printBoard(board):
	i = 0
	while i < SIZE:
		row = ""
		j = 0
		while j < SIZE:
			row += '|' if (j % 3  == 0) else ' '
			row += '-'  if (board[i][j] == 0) else str(board[i][j])
			j += 1
		row+=  '|'
		if(i % 3 == 0 ):
			print('-------------------')
		print(row)
		i += 1


initial_data = \
	[\
		0, 0, 1, 9, 8, 4, 7, 6, 0,\
		6, 0, 0, 0, 5, 7, 0, 0, 0,\
		8, 0, 7, 0, 1, 0, 0, 0, 0,\
		9, 6, 0, 3, 0, 8, 1, 0, 5,\
		1, 8, 5, 0, 2, 0, 0, 7, 3,\
		3, 0, 0, 0, 0, 0, 2, 0, 8,\
		2, 1, 0, 0, 0, 0, 0, 3, 6,\
		0, 0, 0, 1, 0, 0, 0, 0, 4,\
		0, 9, 6, 0, 0, 2, 5, 1, 0\
	]
initializeBoard(board, initial_data)

printBoard(board)