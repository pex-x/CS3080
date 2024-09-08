test = True
while(test) :
    print("Please enter the number of lines: ")
    userInput = int(input())

    if(userInput >= 1) :
        for i in range(userInput, 0, -1):
            print('*' * i)
            test = False 
    else :
        print("Invalid Input")