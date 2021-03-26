import math
def cube():
   a = int(input('ENTER X: ')) 
   b = int(input('ENTER Y: '))
   c = int(input('ENTER Z: '))
   d = a / 12
   e = b / 12
   f = c / 12
   resultcf = d * e * f
   resultcf = math.ceil(resultcf)
   print(resultcf)