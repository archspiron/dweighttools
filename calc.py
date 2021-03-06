import math

while True:
 if input('1 FOR MANUAL INPUT, 2 FOR BOXTYPE') == '1':
    x = int(input("Enter X:"))
    y = int(input("Enter Y:"))
    z = int(input("Enter Z:"))

    result = x * y * z
    result = math.ceil(result/139.0)
    print(result)

 if input ('1 FOR MANUAL INPUT, 2 FOR BOXTYPE') == '2':
    print('TG D-WEIGHT IS 19LBS')
    print('UG D-WEIGHT IS 31LBS')
    print('PG D-WEIGHT IS TBD')
 if input('Do you want to repeat(y/n)') == 'n':
        break
