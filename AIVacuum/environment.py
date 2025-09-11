class Environment:
	def __init__(self):
		self.state = ["Dirty", "Clean", "Dirty", "Dirty", "Dirty", "Dirty", "Dirty", "Clean", "Clean"]

	def show(self):
		print(f'Environment: {self.state}')
