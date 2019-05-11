class Trainer:
	def __init__(self):
		"""
		Trainer is going to define methods to train agent
		Also he will be responsible for his perfomance evaluation
		"""
		pass
	def train(self, agent, episodes=2000):
		for i in range(episodes):
			while not(agent.hasReached()):
				agent.make_action()
				agent.step_size -= 0.001
			if (i+1)%100==0:
				print("I have completed {} go".format(i+1))
			agent.reset_step_size()
			agent.reset_to_random_position()
		print(agent.environment.state_values)