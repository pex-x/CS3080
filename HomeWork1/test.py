conditionOne = True
while(conditionOne) :
    print("Please enter a Calendar Year (In YYYY format...):  ")
    calYear = input()
    splitList = calYear.split()
    yearVal = int(splitList[0]) % 4


    if(yearVal  != 0) :
        yearFixed = calYear.replace('is', 'is not')
        print(calYear)
    else :
        yearFixed = calYear.replace('is not', 'is')
        print(yearFixed)