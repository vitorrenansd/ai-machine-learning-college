from vacuum import Vacuum
from environment import Environment

environment = Environment(["Dirty", "Clean", "X", "Dirty", "X", "Dirty", "Dirty", "Clean", "X"])
vacuum = Vacuum()

room_size = environment.get_room_size()
print(f'Initial state: {environment.show()}')

for _ in range(room_size):
	vacuum.action(environment)

environment.show()
