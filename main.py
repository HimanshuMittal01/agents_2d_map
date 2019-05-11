"""
This program is used to bring concepts of reinforcement learning roughly into code without using gym library.
I will implement temporal difference learning but not exactly.
"""

#Import files and libraries
from agent import Agent
from terrain import Terrain
from trainer import Trainer

terrain = [["land","land","land","goal"],
["land","fire","land","land"],
["land","land","land","land"],
["land","land","land","fire"]]

initial_values = {"land": 0.5, "fire": 0, "goal": 1}

actions = ["up", "down", "left", "right"]


#Create agent and environment
env = Terrain(terrain, initial_values)
agent = Agent(env, actions)

def main():
	trainer = Trainer()
	trainer.train(agent)

	#agent.reset_to_random_position()
	#print(agent.position.position)
	#while not(agent.hasReached()):
	#	agent.move_normally()

	#testing over

#This is the main file
if __name__=='__main__':
	main()