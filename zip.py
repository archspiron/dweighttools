def ziplook():

    dc = str(input('INPUT LOCATION: CA, CC OR TX '))
    
    if dc in ('ca', 'CA'):
        cazi = int(input('INPUT DESTINATION ZIP '))
        print(cazi)

    if dc in ('cc', 'CC'):
        cczi = int(input('INPUT DESTINATION ZIP '))
        print(cczi)

    if dc in ('tx', 'TX'):
        txzi = int(input('INPUT DESTINATION ZIP '))
        
        if 70000 <= txzi <= 79999:
            print('1-2 DAY TRANSIT TIME')

        elif 80000 <= txzi <= 89999:
            print('2-3 DAY TRANSIT TIME')

        elif 90000 <= txzi <= 96162:
            print('3 DAY TRANSIT TIME')

        elif 97000 <= txzi <= 99403:
            print('3-4 DAY TRANSIT TIME')
        
        #ALASKA
        elif 99501 <= txzi <= 99950:
            print('7+ DAY TRANSIT TIME')

        #HAWAII
        elif 96701 <= txzi <= 96898:
            print('6 DAY TRANSIT TIME')
