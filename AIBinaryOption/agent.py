class Agent:
	def __init__(self, state=None, gent_task=None):
		self.state = state
		self.agent_task = gent_task
		self.history = []

	def show_state(self):
		return str(self.state)

	def perception(self):
		entrance = input('Value: ')
		self.history.append(entrance)
