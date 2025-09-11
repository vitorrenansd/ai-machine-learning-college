class Vacuum:
	def __init__(self):
		self.position = 0

	def state_i_am(self, ambient):
		return ambient.state[self.position]

	def action(self, ambient):
		perception = self.state_i_am(ambient)
		if perception == "Dirty":
			ambient.state[self.position] = "Clean"
			print(f'Cleaning position {self.position}')
		else:
			print(f'This place is already cleaned')
		self.move()

	def move(self):
		if self.position < 8:
			self.position += 1
			print(f'Moving to position {self.position}')
