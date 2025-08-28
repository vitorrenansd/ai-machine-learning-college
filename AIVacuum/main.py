from vacuum import Vacuum
from ambient import Ambient

ambient = Ambient()
vacuum = Vacuum()

print('Initial state')
ambient.show()

for _ in range(4):
	vacuum.action(ambient)

print('Show state')
ambient.show()

