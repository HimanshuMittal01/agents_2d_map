from position import Position

class Terrain:
	def __init__(self, terrain, intial_tile_values):
		"""
		terrain: terrain must be a rectangular two dimensional lilst
		"""
		self.terrain = terrain
		self.initial_tile_values = intial_tile_values

		self.__rows = self.__get_number_of_rows()
		self.__columns = self.__get_number_of_columns()

		#Initializing state values
		self.state_values = []
		self.__initialize_state_values()

		#define your goal
		#in our case goal is static/fixed
		self.goal_pos = self.__find_exit_position()

	def update_state(xpos, ypos, new_state_value):
		#update the particular state
		#called by agent
		state_values[xpos][ypos] = new_state_value

	#TODO: Remove the self keyword.
	def __get_number_of_rows(self):
		return len(self.terrain)
	def __get_number_of_columns(self):
		#FUTURE: when we have to change the pattern of terrain,
		# then we need to change or remove this
		return len(self.terrain[0])
	def __initialize_state_values(self):
		#FUTURE: when we have to change the pattern of terrain,
		# then we need to change or remove this
		for i in range(self.__rows):
			self.state_values.append([])
			self.state_values[i] = [self.initial_tile_values[self.terrain[i][j]] for j in range(self.__columns)]
	def __find_exit_position(self):
		#Required to do find goal and specify exit
		for i, row in enumerate(self.terrain):
			for j, tile in enumerate(row):
				if tile=="goal":
					return Position((i, j))

	def get_rows(self):
		return self.__rows
	def get_columns(self):
		return self.__columns
