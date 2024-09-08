test = True
while(test) :
    print("Please enter the number of lines: ")
    userInput = int(input())

    if(userInput >= 1) :
        for i in range(1, userInput + 1, 1):
            print(' ' * (userInput - i) + '*' * i)
            test = False 
    else :
        print("Invalid Input")