conditionOne = True
while(conditionOne) :
    print("Please enter the number of lines: ")
    userInput = int(input())

    if(userInput >= 1) :
        for i in range(1, userInput + 1, 1):
            print((' ' * (userInput - i) + '*' * (2 * i - 1)))
            conditionOne = False 
    else :
        print("Invalid Input")
