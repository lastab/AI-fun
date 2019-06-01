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
	def check_number_already_present(self, i, j, number):
		return self.__check_row_already_present(i, number) or self.__check_column_already_present(j, number) or self.__check_square(i, j, number)
	def __check_row_already_present(self, i, number):
		j = 0
		while j < self.SIZE:
			if(self.board[i][j] == number):
				return True
			j +=1
		return False
	def __check_column_already_present(self, j, number):
		i = 0
		while i < self.SIZE:
			if(self.board[i][j] == number):
				return True
			i +=1
		return False
	def __check_square(self, i, j, number):
		temp_i = i//3
		temp_j = j//3
		limit_i = temp_i + 3
		limit_j = temp_j + 3
		while temp_i < limit_i:
			while temp_j < limit_j:
				if(self.board[temp_i][temp_j] == number):
					return True
				temp_j += 1
			temp_i += 1
		return False


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
i=1
while i < 10:
	print(s1.check_number_already_present(0,0,i))
	i  += 1