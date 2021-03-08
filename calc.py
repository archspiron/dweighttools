from eq import boxmath
from predef import prefab

while True:
	gate = int(input('SELECT 1 FOR MANUAL DIMS INPUT, SELECT 2 FOR TYPE SELECTION: '))
	if gate == 1:
 		boxmath()

	if gate == 2:
 		prefab()

	if input('REPEAT?(Y/N): ') == 'n':
		break

