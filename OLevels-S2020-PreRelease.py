#Declaration of Variables#
Day = str
ArrivalHour = int
HoursStay = int
ParkingNo = int

#INITIALISATION OF VARIABLES#
LeaveTime = 0
TotalPrice = 0
DailyTotal = 0
Hours = 0

#Code#

Day = ["Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday"]
ParkPrice = [2.00 , 10.00 , 10.00 , 10.00 , 10.00 , 10.00 , 3.00]
MaxStay = [8 , 2 , 2 , 2 , 2 , 2 , 4]
choice = input("Enter 'Y' to continue as new user or 'N' to end the day")

while (choice=="Y") or (choice=="y"):
    day = int(input("Enter the day 0-Sunday 1-Monday 2-Tuesday 3-Wednesday 4-Thursday 5-Friday 6-Saturday"))
    ArrivalHour = int(input("Enter hour of arrival excluding minutes"))
    
    while (ArrivalHour < 8) or (ArrivalHour > 23):
        print ("Invalid input, no parking is allowed at this time")
        ArrivalHour = int(input("Enter hour of arrival excluding minutes"))
    HoursStay = int(input("Enter the duration of your stay in hours"))
    LeaveTime = LeaveTime + (ArrivalHour + HoursStay)
    
    while (LeaveTime > 24):
        print ("You cannot stay past midnight")
        HoursStay = int(input("Enter the duration of your stay"))
        LeaveTime = LeaveTime - (ArrivalHour + HoursStay)
        
    if (ArrivalHour >= 8) and (ArrivalHour <= 15):
        while (HoursStay > MaxStay[day]):
            print ("You cannot stay that long")
            HoursStay = int(input("Enter the duration of your stay in hours"))
            
    elif (ArrivalHour > 15) and (ArrivalHour < 23):
        while (HoursStay > 8):
            print ("You cannot stay that long")
            HoursStay = int(input("Enter the duration of your stay in hours"))
            
    if (LeaveTime > 16):
        Hours = Hours + (16 - ArrivalHour)
    ParkingNo = int(input("Enter your parking number"))
    
    while (ParkingNo < 1000) or (ParkingNo > 9999):
        print ("Please re-enter your parking number")
        ParkingNo = int(input("Enter your parking number"))
    FreqParkNo = ParkingNo%11
    
    if (ArrivalHour >= 8) and (ArrivalHour < 15):
        if (FreqParkNo==0):
            TotalPrice = float(TotalPrice + (HoursStay*ParkPrice[day]*0.9))
            print ("Day:" , Day[day] , "Hour of Arrival:" , ArrivalHour , "Duration of stay"  , HoursStay, "hours")
            print ("You have to pay: $", TotalPrice)
            
        else:
            TotalPrice = float(TotalPrice + (HoursStay*ParkPrice[day]))
            print ("Day:" , Day[day] , "Hour of Arrival:" , ArrivalHour , "Duration of stay:" , HoursStay, "hours")
            print ("You have to pay: $",TotalPrice)
            
    elif (ArrivalHour > 15) and (ArrivalHour < 23):
        if (FreqParkNo==0):
            TotalPrice = float(TotalPrice + (HoursStay*2*0.5))
            print ("Day:" , Day[day] , "Hour of Arrival:" , ArrivalHour , "Duration of stay:" , HoursStay, "hours")
            print ("You have to pay :$", TotalPrice)
            
        else:
            TotalPrice = float(TotalPrice + (HoursStay*2))
            print ("Day:" , Day[day] , "Hour of Arrival:" , ArrivalHour , "Duration of stay:" , HoursStay, "hours")
            print ("You have to pay: $",TotalPrice)
            
    elif (LeaveTime > 16):
        if (FreqParkNo==0):
            TotalPrice = float(TotalPrice + (((Hours*ParkPrice[day]) + 2)*0.9))
            print ("Day:" , Day[day] , "Hour of Arrival:" , ArrivalHour , "Duration of stay:" , HoursStay, "hours")
            print ("You have to pay: $",TotalPrice)
            
        else:
            TotalPrice = float(TotalPrice + ((Hours*ParkPrice[day]) + 2))
            print ("Day:" , Day[day] , "Hour of Arrival:" , ArrivalHour , "Duration of stay:" , HoursStay, "hours")
            print ("You have to pay: $",TotalPrice)
    AmountPaid = float(input("Enter the amount you have to pay"))
    
    while (AmountPaid < TotalPrice):
        print ("You have not paid enough yet, please pay the full amount")
        AmountPaid = float(input("Enter the amount you have to pay"))
    DailyTotal = DailyTotal + AmountPaid
    LeaveTime = 0
    TotalPrice = 0
    Hours = 0

    choice = input("Enter 'Y' to continue as new user or 'N' to end the day")
if (choice=="N") or (choice=="n"):
    print ("The Daily Total is: $" , DailyTotal)
