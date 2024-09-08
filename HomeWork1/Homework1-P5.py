test = True
while(test) :
    print("Please enter the number of lines: ")
    userInput = int(input())

    if(userInput >= 1) :
        for i in range(1, userInput + 1, 1):
            spaces = ' ' * (userInput - i)
            stars = '* ' * i
            print(spaces + stars)
            test = False 
    else :
        print("Invalid Input")
