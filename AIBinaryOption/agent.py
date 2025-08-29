class Agent:
	def __init__(self, state=None, agentTask=None):
		self.state = state
		self.agentTask = agentTask
		self.history = []

	def show_state():
		return str(self.state)

	def perception(self):
		entrance = input('Value: ')
		self.history.append(entrance)
