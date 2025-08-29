class Environment:
	def __init__(self, initial_state=None):
		self.state = initial_state
		self.environment_obj = []
		self.agents = []

	def perception(self, agent):
		return None

	def add_agent(self, agent):
		self.agents.append(agent)
