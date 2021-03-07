while True:
 gate = int(input('SELECT 1 FOR MANUAL DIMS INPUT, SELECT 2 FOR TYPE SELECTION: '))
 if gate == '1':
 	 from math import boxmath
 	 boxmath()

 if gate == '2': 
 	 from predef import prefab
 	 prefab()

 if input('REPEAT?(Y/N): ') == 'n':
 
	 break
 
