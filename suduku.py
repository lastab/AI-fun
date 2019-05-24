class Suduku:
	SIZE = 9
	def __init__(self, inputs):
		self.board =[[0 for x in range(self.SIZE)] for y in range(self.SIZE)]
		i = 0
		j = 0
		for index, data in enumerate(inputs):
			i = index // 9
			j = index % 9
			self.board[i][j] = data
	def printBoard(self):
		i = 0
		while i < self.SIZE:
			row = ""
			j = 0
			while j < self.SIZE:
				row += '|' if (j % 3  == 0) else ' '
				row += '-'  if (self.board[i][j] == 0) else str(self.board[i][j])
				j += 1
			row+=  '|'
			if(i % 3 == 0 ):
				print('-------------------')
			print(row)
			i += 1

	# def check_number(self, i, j, number):


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
s1 = Suduku(initial_data)
s1.printBoard()
# initializeBoard(board, initial_data)

# printBoard(board)