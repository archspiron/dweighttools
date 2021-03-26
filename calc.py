from eq import boxmath
from cf import cube
from predef import prefab
from zip import ziplook
from lookup import look
from convert import inchToCM
from convert import cmToInch
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
	mainMenu = int(input("""
OPTION 1: CACLULATOR TOOLS
OPTION 2: FEDEX GROUND TRANSIT TIMES
OPTION 3: PART NUMBER LOOKUP
"""))
	if mainMenu == 1:
		cMenu = int(input("""
OPTION 1: D-WEIGHT BY XYZ INPUT
OPTION 2: D-WEIGHT BY GOVERNOR BOX TYPE
OPTION 3: CUBIC FOOT CALCULATOR
OPTION 4: INCHES TO CENTIMENTERS
OPTION 5: CENTIMETERS TO INCHES
"""))
		if cMenu == 1:
			boxmath()
		elif cMenu == 2:
			prefab()
		elif cMenu == 3:
			cube()
		elif cMenu == 4:
			inchToCM()
		elif cMenu == 5:
			cmToInch()
	elif mainMenu == 2:
		ziplook()
	elif mainMenu == 3:
		look()
	if input('REPEAT?(Y/N): ') in ('n', 'N'):
		break

