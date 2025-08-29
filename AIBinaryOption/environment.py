class Environment:
	def __init__(self, initialState=None):
		self.state = initialState
		self.environmentObj = []
		self.agents = []

	def perception(self, agent):
		return None

	def add_agent(self, agent):
		self.agents.append(agent)
