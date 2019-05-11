class Position(object):
    """
    This is to store the position of the agent
    """
    def __init__(self, position):
        self.position = position

        self.__x = self.position[0]
        self.__y = self.position[1]
    
    def getX(self):
        return self.__x
    def setX(self, x):
    	self.__x = x
    	self.position = (self.__x, self.__y)
    def getY(self):
        return self.__y
    def setY(self, y):
    	self.__y = y
    	self.position = (self.__x, self.__y)

class Movement:
	"""
	This will be used to move the agent
	"""
	def __init__(self, position):
		self.position = position

	def move(self, action):
		if action=="up":
			self.__move_up()
		elif action=="down":
			self.__move_down()
		elif action=="left":
			self.__move_left()
		elif action=="right":
			self.__move_right()
		else:
			print("{} action is not currently known by the agent".format(action))
	def get_coord_if_move(self, action):
		output_position = None
		if action=="up":
			self.__move_up()
			output_position = self.position
			self.__move_down()
		elif action=="down":
			self.__move_down()
			output_position = self.position
			self.__move_up()
		elif action=="left":
			self.__move_left()
			output_position = self.position
			self.__move_right()
		elif action=="right":
			self.__move_right()
			output_position = self.position
			self.__move_left()
		else:
			print("{} action can't be thought".format(action))

		return output_position

	def __move_right(self):
		self.position.setX(self.position.getX() + 1)
	def __move_left(self):
		self.position.setX(self.position.getX() - 1)
	def __move_up(self):
		self.position.setY(self.position.getY() - 1)
	def __move_down(self):
		self.position.setY(self.position.getY() + 1)
		