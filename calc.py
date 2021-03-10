from eq import boxmath
from cf import cube
from predef import prefab
from zip import ziplook

while True:
	gate = int(input('OPTION 1 FOR D-WEIGHT, OPTION 2 FOR CUBIC FOOT CALC., OPTION 3 FOR ZIP TRANSIT TIME '))

	if gate == 1:
		gated = int(input('1 FOR MANUAL INPUT, 2 FOR GOVERNOR BOX TYPE '))

		if gated == 1:
			boxmath()
		
		elif gated == 2:
			prefab()

	elif gate == 2:
	    cube()

	elif gate == 3:
		ziplook()

	if input('REPEAT?(Y/N): ') in ('n', 'N'):
		break

