def ziplook():
    print('***TRANSIT TIMES ARE ACCURATE FOR BUSINESS ADDRESSES ONLY***')
    print('***IF ZIP CODE STARTS WITH 0, PLEASE OMIT FIRST 0***')
    dc = str(input('INPUT LOCATION: CA, CC OR TX '))
    t12 = str('1-2 DAY TRANSIT TIME')
    t2 = str('2 DAY TRANSNIT TIME')
    t23 = str('2-3 DAY TRANSIT TIME')
    t3 = str('3 DAY TRANSIT TIME')
    t34 = str('3-4 DAY TRANSIT TIME')
    t4 = str('4 DAY TRANSIT TIME')
    t45 = str('4-5 DAY TRANSIT TIME')
    t5 = str('5 DAY TRANSIT TIME')
    t6 = str('6 DAY TRANSIT TIME')
    t7 = str('7+ DAY TRANSIT TIME') 
    if dc in ('ca', 'CA'):
        cazi = int(input('INPUT DESTINATION ZIP '))
        #ALABAMA
        if 35004 <= cazi <= 36925:
            print(t4)
        #ALASKA
        elif 99501 <= cazi <= 99950:
            print(t7)
        #ARKANSAS
        elif 71601 <= cazi <= 72959:
            print(t34)
        #ARIZONA
        elif 85001 <= cazi <= 86556:
            print(t2)
        #CALIFORNIA
        elif 90001 <= cazi <= 96162:
            print(t12)
        #COLORADO
        elif 80001 <= cazi <= 81658:
            print(t23)
        #CONNECTICUT
        elif 6001 <= cazi <= 6927:
            print(t45)
        #DELAWARE
        elif 19701 <= cazi <= 19980:
            print(t4)
        #FLORIDA
        elif 32003 <= cazi <= 34997:
            print(t4)
        #GEORGIA
        elif 30002 <= cazi <= 39901:
            print(t4)
        #HAWAII
        elif 96701 <= cazi <= 96898:
            print(t45)
        #IOWA
        elif 50001 <= cazi <= 52809:
            print(t4)
        #IDAHO
        elif 83201 <= cazi <= 83877:
            print(t23)
        #ILLINOIS
        elif 60002 <= cazi <= 62999:
            print(t4)
        #INDIANA
        elif 46001 <= cazi <= 47997:
            print(t4)
        #KANSAS
        elif 66002 <= cazi <= 67954:
            print(t4)
        #KENTUCKY
        elif 40003 <= cazi <= 42788:
            print(t4)
        #LOUISIANA
        elif 70001 <= cazi <= 71497:
            print(t34)
        #MASSACHUSETTS
        elif 1001 <= cazi <= 2791:
            print(t5)
        #MARYLAND
        elif 20588 <= cazi <= 21930:
            print(t4)
        #MAINE
        elif 3901 <= cazi <= 4992:
            print(t5)
        #MICHIGAN
        elif 48001 <= cazi <= 49971:
            print(t4)
        #MINNESOTA
        elif 55001 <= cazi <= 56763:
            print(t4)
        #MISSOURI
        elif 63005 <= cazi <= 65899:
            print(t34)
        #MISSISSIPPI
        elif 38601 <= cazi <= 39776:
            print(t34)
        #MONTANA
        elif 59001 <= cazi <= 59937:
            print(t34)
        #NORTH CAROLINA
        elif 27006 <= cazi <= 28909:
            print(t4)
        #NORTH DAKOTA
        elif 58001 <= cazi <= 58856:
            print(t34)
        #NEBRASKA
        elif 68001 <= cazi <= 69367:
            print(t34)
        #NEW HAMPSHIRE
        elif 3031 <= cazi <= 3897:
            print(t5)
        #NEW JERSEY
        elif 7001 <= cazi <= 8989:
            print(t4)
        #NEW MEXICO
        elif 87001 <= cazi <= 88439:
            print(t23)
        #Nevada
        elif 88901 <= cazi <= 89883:
            print(t12)
        #NEW YORK
        elif 10001 <= cazi <= 14905:
            print(t45)
        #OHIO
        elif 43001 <= cazi <= 45999:
            print(t4)
        #OKLAHOMA
        elif 73001 <= cazi <= 74966:
            print(t34)
        #OREGON
        elif 97001 <= cazi <= 97920:
            print(t23)
        #PENNSYLVANIA
        elif 15001 <= cazi <= 19612:
            print(t45)
        #RHODE ISLAND
        elif 2801 <= cazi <= 2940:
            print(t5)
        #SOUTH CAROLINA
        elif 29001 <= cazi <= 29945:
            print(t4)
        #SOUTH DAKOTA
        elif 57001 <= cazi <= 57799:
            print(t34)
        #TENNESSEE
        elif 37010 <= cazi <= 38589:
            print(t34)
        #TEXAS(YEE HAW)
        elif 73301 <= cazi <= 79999:
            print(t3)
        #UTAH
        elif 84001 <= cazi <= 84791:
            print(t23)
        #VIRGINIA
        elif 20101 <= cazi <= 24658:
            print(t4)
        #VERMONT
        elif 5001 <= cazi <= 5907:
            print(t5)
        #WASHINGTON
        elif 98001 <= cazi <= 99403:
            print(t3)
        #WISCONSIN
        elif 53001 <= cazi <= 54986:
            print(t4)
        #WEST VIRGINIA
        elif 24701 <= cazi <= 26886:
            print(t4)
        #WYOMING
        elif 82001 <= cazi <= 83414:
            print(t23)
    if dc in ('cc', 'CC'):
        cczi = int(input('INPUT DESTINATION ZIP '))
        #ALABAMA
        if 35004 <= cczi <= 36925:
            print(t23)
        #ALASKA
        elif 99501 <= cczi <= 99950:
            print(t7)
        #ARKANSAS
        elif 71601 <= cczi <= 72959:
            print(t2)
        #ARIZONA
        elif 85001 <= cczi <= 86556:
            print(t3)
        #CALIFORNIA
        elif 90001 <= cczi <= 96162:
            print(t3)
        #COLORADO
        elif 80001 <= cczi <= 81658:
            print(t3)
        #CONNECTICUT
        elif 6001 <= cczi <= 6927:
            print(t34)
        #DELAWARE
        elif 19701 <= cczi <= 19980:
            print(t3)
        #FLORIDA
        elif 32003 <= cczi <= 34997:
            print(t3)
        #GEORGIA
        elif 30002 <= cczi <= 39901:
            print(t3)
        #HAWAII
        elif 96701 <= cczi <= 96898:
            print(t6)
        #IOWA
        elif 50001 <= cczi <= 52809:
            print(t23)
        #IDAHO
        elif 83201 <= cczi <= 83877:
            print(t34)
        #ILLINOIS
        elif 60002 <= cczi <= 62999:
            print(t3)
        #INDIANA
        elif 46001 <= cczi <= 47997:
            print(t3)
        #KANSAS
        elif 66002 <= cczi <= 67954:
            print(t2)
        #KENTUCKY
        elif 40003 <= cczi <= 42788:
            print(t23)
        #LOUISIANA
        elif 70001 <= cczi <= 71497:
            print(t12)
        #MASSACHUSETTS
        elif 1001 <= cczi <= 2791:
            print(t4)
        #MARYLAND
        elif 20588 <= cczi <= 21930:
            print(t3)
        #MAINE
        elif 3901 <= cczi <= 4992:
            print(t4)
        #MICHIGAN
        elif 48001 <= cczi <= 49971:
            print(t3)
        #MINNESOTA
        elif 55001 <= cczi <= 56763:
            print(t3)
        #MISSOURI
        elif 63005 <= cczi <= 65899:
            print(t23)
        #MISSISSIPPI
        elif 38601 <= cczi <= 39776:
            print(t2)
        #MONTANA
        elif 59001 <= cczi <= 59937:
            print(t34)
        #NORTH CAROLINA
        elif 27006 <= cczi <= 28909:
            print(t3)
        #NORTH DAKOTA
        elif 58001 <= cczi <= 58856:
            print(t3)
        #NEBRASKA
        elif 68001 <= cczi <= 69367:
            print(t23)
        #NEW HAMPSHIRE
        elif 3031 <= cczi <= 3897:
            print(t4)
        #NEW JERSEY
        elif 7001 <= cczi <= 8989:
            print(t3)
        #NEW MEXICO
        elif 87001 <= cczi <= 88439:
            print(t23)
        #Nevada
        elif 88901 <= cczi <= 89883:
            print(t3)
        #NEW YORK
        elif 10001 <= cczi <= 14905:
            print(t34)
        #OHIO
        elif 43001 <= cczi <= 45999:
            print(t3)
        #OKLAHOMA
        elif 73001 <= cczi <= 74966:
            print(t2)
        #OREGON
        elif 97001 <= cczi <= 97920:
            print(t34)
        #PENNSYLVANIA
        elif 15001 <= cczi <= 19612:
            print(t34)
        #RHODE ISLAND
        elif 2801 <= cczi <= 2940:
            print(t4)
        #SOUTH CAROLINA
        elif 29001 <= cczi <= 29945:
            print(t3)
        #SOUTH DAKOTA
        elif 57001 <= cczi <= 57799:
            print(t3)
        #TENNESSEE
        elif 37010 <= cczi <= 38589:
            print(t23)
        #TEXAS(YEE HAW)
        elif 73301 <= cczi <= 79999:
            print(t12)
        #UTAH
        elif 84001 <= cczi <= 84791:
            print(t3)
        #VIRGINIA
        elif 20101 <= cczi <= 24658:
            print(t3)
        #VERMONT
        elif 5001 <= cczi <= 5907:
            print(t4)
        #WASHINGTON
        elif 98001 <= cczi <= 99403:
            print(t4)
        #WISCONSIN
        elif 53001 <= cczi <= 54986:
            print(t3)
        #WEST VIRGINIA
        elif 24701 <= cczi <= 26886:
            print(t3)
        #WYOMING
        elif 82001 <= cczi <= 83414:
            print(t3)
    if dc in ('tx', 'TX'):
        txzi = int(input('INPUT DESTINATION ZIP '))
        #ALABAMA
        if 35004 <= txzi <= 36925:
            print(t2)
        #ALASKA
        elif 99501 <= txzi <= 99950:
            print(t7)
        #ARKANSAS
        elif 71601 <= txzi <= 72959:
            print(t2)
        #ARIZONA
        elif 85001 <= txzi <= 86556:
            print(t23)
        #CALIFORNIA
        elif 90001 <= txzi <= 96162:
            print(t3)
        #COLORADO
        elif 80001 <= txzi <= 81658:
            print(t23)
        #CONNECTICUT
        elif 6001 <= txzi <= 6927:
            print(t3)
        #DELAWARE
        elif 19701 <= txzi <= 19980:
            print(t3)
        #FLORIDA
        elif 32003 <= txzi <= 34997:
            print(t23)
        #GEORGIA
        elif 30002 <= txzi <= 39901:
            print(t23)
        #HAWAII
        elif 96701 <= txzi <= 96898:
            print(t6)
        #IOWA
        elif 50001 <= txzi <= 52809:
            print(t23)
        #IDAHO
        elif 83201 <= txzi <= 83877:
            print(t34)
        #ILLINOIS
        elif 60002 <= txzi <= 62999:
            print(t2)
        #INDIANA
        elif 46001 <= txzi <= 47997:
            print(t23)
        #KANSAS
        elif 66002 <= txzi <= 67954:
            print(t2)
        #KENTUCKY
        elif 40003 <= txzi <= 42788:
            print(t23)
        #LOUISIANA
        elif 70001 <= txzi <= 71497:
            print(t12)
        #MASSACHUSETTS
        elif 1001 <= txzi <= 2791:
            print(t3)
        #MARYLAND
        elif 20588 <= txzi <= 21930:
            print(t3)
        #MAINE
        elif 3901 <= txzi <= 4992:
            print(t34)
        #MICHIGAN
        elif 48001 <= txzi <= 49971:
            print(t3)
        #MINNESOTA
        elif 55001 <= txzi <= 56763:
            print(t3)
        #MISSOURI
        elif 63005 <= txzi <= 65899:
            print(t2)
        #MISSISSIPPI
        elif 38601 <= txzi <= 39776:
            print(t2)
        #MONTANA
        elif 59001 <= txzi <= 59937:
            print(t34)
        #NORTH CAROLINA
        elif 27006 <= txzi <= 28909:
            print(t3)
        #NORTH DAKOTA
        elif 58001 <= txzi <= 58856:
            print(t3)
        #NEBRASKA
        elif 68001 <= txzi <= 69367:
            print(t23)
        #NEW HAMPSHIRE
        elif 3031 <= txzi <= 3897:
            print(t3)
        #NEW JERSEY
        elif 7001 <= txzi <= 8989:
            print(t3)
        #NEW MEXICO
        elif 87001 <= txzi <= 88439:
            print(t23)
        #Nevada
        elif 88901 <= txzi <= 89883:
            print(t3)
        #NEW YORK
        elif 10001 <= txzi <= 14905:
            print(t34)
        #OHIO
        elif 43001 <= txzi <= 45999:
            print(t3)
        #OKLAHOMA
        elif 73001 <= txzi <= 74966:
            print(t12)
        #OREGON
        elif 97001 <= txzi <= 97920:
            print(t34)
        #PENNSYLVANIA
        elif 15001 <= txzi <= 19612:
            print(t34)
        #RHODE ISLAND
        elif 2801 <= txzi <= 2940:
            print(t3)
        #SOUTH CAROLINA
        elif 29001 <= txzi <= 29945:
            print(t3)
        #SOUTH DAKOTA
        elif 57001 <= txzi <= 57799:
            print(t3)
        #TENNESSEE
        elif 37010 <= txzi <= 38589:
            print(t23)
        #TEXAS(YEE HAW)
        elif 73301 <= txzi <= 79999:
            print(t12)
        #UTAH
        elif 84001 <= txzi <= 84791:
            print(t3)
        #VIRGINIA
        elif 20101 <= txzi <= 24658:
            print(t3)
        #VERMONT
        elif 5001 <= txzi <= 5907:
            print(t3)
        #WASHINGTON
        elif 98001 <= txzi <= 99403:
            print(t4)
        #WISCONSIN
        elif 53001 <= txzi <= 54986:
            print(t3)
        #WEST VIRGINIA
        elif 24701 <= txzi <= 26886:
            print(t3)
        #WYOMING
        elif 82001 <= txzi <= 83414:
            print(t23)
        

