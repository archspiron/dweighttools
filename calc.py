from eq import boxmath
from cf import cube
from predef import prefab
from zip import ziplook
print("""
  /$$$$$$ /$$$$$$$                      /$$$$$$$$/$$$$$$  /$$$$$$ /$$       /$$$$$$ 
 /$$__  $| $$__  $$                    |__  $$__/$$__  $$/$$__  $| $$      /$$__  $$
| $$  \__| $$  \ $$                       | $$ | $$  \ $| $$  \ $| $$     | $$  \__/
|  $$$$$$| $$$$$$$/       /$$$$$$         | $$ | $$  | $| $$  | $| $$     |  $$$$$$ 
 \____  $| $$__  $$      |______/         | $$ | $$  | $| $$  | $| $$      \____  $$
 /$$  \ $| $$  \ $$                       | $$ | $$  | $| $$  | $| $$      /$$  \ $$
|  $$$$$$| $$  | $$                       | $$ |  $$$$$$|  $$$$$$| $$$$$$$|  $$$$$$/
 \______/|__/  |__/                       |__/  \______/ \______/|________/\______/ 
""")
while True:
	mainMenu = int(input('OPTION 1 FOR D-WEIGHT, OPTION 2 FOR CUBIC FOOT CALC., OPTION 3 FOR FXG TRANSIT TIME '))

	if mainMenu == 1:
		dMenu = int(input('1 FOR MANUAL INPUT, 2 FOR GOVERNOR BOX TYPE '))

		if dMenu == 1:
			boxmath()
		
		elif dMenu == 2:
			prefab()

	elif mainMenu == 2:
	    cube()

	elif mainMenu == 3:
		ziplook()

	if input('REPEAT?(Y/N): ') in ('n', 'N'):
		break

