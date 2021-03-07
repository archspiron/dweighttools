import math

while True:
 gate = int(input('SELECT 1 FOR MANUAL DIMS INPUT, SELECT 2 FOR TYPE SELECTION: '))
 if gate == '1':

	 x = int(input('ENTER X : '))
	 y = int(input('ENTER Y : '))
	 z = int(input('ENTER Z : '))

	 result = x * y * z
	 result = math.ceil(result/139.0)
	 print(result)

 if gate == '2':
 
     option = str(input('INPUT TYPE : '))
	 
     if option == 'tg' or 'TG':
	     print('TG D-WEIGHT IS 19LBS')
	
     if option == 'ug' or 'UG':
		 print('UG D-WEIGHT IS 31LBS')
	
	 if option == 'pg' or 'PG':
		 print('PG D-WEIGHT IS TBD')
	 
 if input('REPEAT?(Y/N): ') == 'n':
 
	 break
 