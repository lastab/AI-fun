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
		print()
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
		print()
	def check_number_already_present(self, i, j, number):
		if (not self.board[i][j] == 0):
			return True
		return self.check_row_already_present(i, number) or self.check_column_already_present(j, number) or self.check_square(i, j, number)

	def check_row_already_present(self, i, number):
		j = 0
		while j < self.SIZE:
			if(self.board[i][j] == number):
				return True
			j +=1
		return False
	def check_column_already_present(self, j, number):
		i = 0
		while i < self.SIZE:
			if(self.board[i][j] == number):
				return True
			i += 1
		return False
	def check_square(self, i, j, number):
		temp_i = i//3 * 3
		temp_j = j//3 * 3
		limit_i = temp_i + 3
		limit_j = temp_j + 3
		while temp_i < limit_i:
			while temp_j < limit_j:
				if(self.board[temp_i][temp_j] == number):
					return True
				temp_j += 1
			temp_i += 1
		return False

	def set_number(self, i, j, number):
		self.board[i][j] = number 

	# def board_filled(self):
	# 	count = 0
	# 	i = 0
	# 	while i < self.size:
	# 		j = 0
	# 		while j < self.size:
	# 			if(self.board[i][j] == 0):
	# 				count +=1
	# 			j += 1

	# 		i += 1
	# 	return count == 0

	def find_empty(self):
		i = 0
		while i < self.SIZE:
			j = 0
			while j < self.SIZE:
				if(self.board[i][j] == 0):
					return [i, j]
				j += 1
			i += 1
		return None



initial_data = \
	[\
		0, 0, 0, 2, 6, 0, 7, 0, 1,\
		6, 8, 0, 0, 7, 0, 0, 9, 0,\
		1, 9, 0, 0, 0, 4, 5, 0, 0,\
		8, 2, 0, 1, 0, 0, 0, 4, 0,\
		0, 0, 4, 6, 0, 2, 9, 0, 0,\
		0, 5, 0, 0, 0, 3, 0, 2, 8,\
		0, 0, 9, 3, 0, 0, 0, 7, 4,\
		0, 4, 0, 0, 5, 0, 0, 3, 6,\
		7, 0, 3, 0, 1, 8, 0, 0, 0\
	]
s1 = Suduku(initial_data)
s1.printBoard()
# initializeBoard(board, initial_data)

def solve(s1):
	find = s1.find_empty()

	if not find:
		return True
	i, j = find

	ja = j
	
	possible_numbers = []
	number = 1

	
	while number < 10:

		if(not s1.check_number_already_present(i, j, number) == True):
			s1.set_number(i, j, number)
			
			if solve(s1):
				return True

		s1.set_number(i, j, 0) # reset value to empty
		number += 1

	return False


solve(s1)
s1.printBoard()


