conditionOne = True
while(conditionOne) :
    print("Please enter a Calendar Year (In YYYY format...):  ")
    calYear = int(input())

    if(calYear % 4 == 0) :
        print("This is a Leap Year")
        conditionOne = False
    else :
        print("This is not a Leap Year")