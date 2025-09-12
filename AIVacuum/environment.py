class Environment:
	def __init__(self, state):
		self.state = state

	def get_room_size(self):
		return len(self.state)
	
	def show(self):
		return self.state
