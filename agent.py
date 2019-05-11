from random import randint, choice
from position import Position, Movement
class Agent:
	def __init__(self, environment, actions, position=[0,0]):
		"""
		position: this must be a 2-valued list
		"""
		self.environment = environment
		self.__check_input(position)

		#FUTURE: game manager is supposed to give names
		self.name = "Agent-01"
		self.__actions = actions
		self.position = Position(position)

		#Movement object
		self.movement = Movement(self.position)
		#step-size required to update the state-value appropriately
		self.step_size = 0.05

	def hasReached(self):
		return self.position.getX()==self.environment.goal_pos.getX() and self.position.getY()==self.environment.goal_pos.getY()

	#Ofcourse it is possible that he gets stuck
	def choose_wisely(self):
		list_of_available_actions = self.__get_available_actions()

		move_values = []
		for move in list_of_available_actions:
			new_pos = self.movement.get_coord_if_move(move)
			move_values.append(self.environment.state_values[new_pos.getX()][new_pos.getY()])
		index_max = max(range(len(move_values)), key=move_values.__getitem__)

		#Little bit wiser action
		chosen_action = list_of_available_actions[index_max]

		return chosen_action
	def __choose_action_randomly(self):
		list_of_available_actions = self.__get_available_actions()

		#Random action
		chosen_action = choice(list_of_available_actions)

		return chosen_action
	def move_normally(self):
		action = self.choose_wisely()
		print(action)
		self.movement.move(action)
	def make_action(self):
		action = self.__choose_action_randomly()

		prevX = self.position.getX()
		prevY = self.position.getY()

		self.movement.move(action)

		currentX = self.position.getX()
		currentY = self.position.getY()

		self.environment.state_values[prevX][prevY] = self.environment.state_values[prevX][prevY] + self.step_size * (self.environment.state_values[currentX][currentY] - self.environment.state_values[prevX][prevY])
	
	#Resetting some variables
	def reset_to_random_position(self):
		self.position.setX(randint(0,self.environment.get_rows()-1))
		self.position.setY(randint(0,self.environment.get_columns()-1))
	def reset_step_size(self):
		self.step_size = 0.05

	def __get_available_actions(self):
		list_of_available_actions = self.__actions.copy()
		if self.position.getY()==0:
			list_of_available_actions.remove("up")
		elif self.position.getY()==self.environment.get_columns()-1:
			list_of_available_actions.remove("down")
		if self.position.getX()==0:
				list_of_available_actions.remove("left")
		elif self.position.getX()==self.environment.get_rows()-1:
			list_of_available_actions.remove("right")

		return list_of_available_actions
	def __check_input(self, pos):
		if len(pos)!=2:
			raise Exception("Position must be 2-valued list not {}-valued list".format(len(pos)))

	def getActions(self):
		return self.actions