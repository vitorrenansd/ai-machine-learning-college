from vacuum import Vacuum
from environment import Environment

environment = Environment(["Dirty", "Clean", "X", "Dirty", "X", "Dirty", "Dirty", "Clean", "X"])
vacuum = Vacuum()

print('Initial state')
environment.show()

for _ in range(9):
	vacuum.action(environment)

environment.show()
