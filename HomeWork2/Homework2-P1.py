list1 = [12, 12, 12, 12, 5, 5, 5, 2, 2]

def numsList(arrayOfNums):
    counter = 0
    temp = arrayOfNums[0]
    for i in range(1, len(arrayOfNums)):
        if temp == arrayOfNums[i]:
            temp = arrayOfNums[i]
            counter = counter + 1
        else:
            if counter < 3:
                counter = 0
            temp = arrayOfNums[i]
    if counter >= 3:
        print(True)
    else:
        print(False)

numsList(list1)