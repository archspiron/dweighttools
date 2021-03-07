import math

gate = int(input('SELECT 1 FOR MANUAL DIMS INPUT, SELECT 2 FOR TYPE SELECTION: '))

while True:

 if gate == '1':

	 x = int(input('ENTER X : '))
	 y = int(input('ENTER Y : '))
	 z = int(input('ENTER Z : '))

	 result = x * y * z
	 result = math.ceil(result/139.0)
	 print(result)
 if input('REPEAT?(Y/N): ') == 'n':
	 break


while True:

 if gate == '2':
 
     print('TG D-WEIGHT IS 19LBS')
     print('UG D-WEIGHT IS 31LBS')
     print('PG D-WEIGHT IS TBD')
	 
 if input('REPEAT?(Y/N): ') == 'n':
	 break
 