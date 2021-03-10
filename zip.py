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
        print(txzi)
