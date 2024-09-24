def capSecondHalf(text):
    lengthOfText = len(text)

    if lengthOfText % 2 == 0:
        middlePoint = lengthOfText // 2
        text = text[:middlePoint] + text[middlePoint:].upper()
        print(text)
    else:
        middlePoint = lengthOfText // 2 + 1
        text = text[:middlePoint] + text[middlePoint:].upper()
        print(text)
    
print("Please, enter a text: ")
userInput = input()
capSecondHalf(userInput)