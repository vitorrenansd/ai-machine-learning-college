from vacuum import Vacuum
from environment import Environment

environment = Environment()
vacuum = Vacuum()

print('Initial state')
environment.show()

for _ in range(4):
	vacuum.action(environment)

print('Show state')
environment.show()

