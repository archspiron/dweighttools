import math
def boxmath():
	x = int(input('ENTER X : '))
	y = int(input('ENTER Y : '))
	z = int(input('ENTER Z : '))
	result = x * y * z
	result = math.ceil(result/139.0)
	print(result)