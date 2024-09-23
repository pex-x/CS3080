list1 = [0, 7, 9, 12]
list2 = [0, 1, 2, 3, 4, 7, 12]


def sortLists(array1, array2):
   tempArrray = []
   count1 = 0
   count2 = 0

   sizeArray1 = len(array1)
   sizeArray2 = len(array2)

   while count1 < sizeArray1 and count2 < sizeArray2:
        if array1[count1] < array2[count2]:
           tempArrray.append(array1[count1])
           count1 += 1
        else:
           tempArrray.append(array2[count2])
           count2 += 1
   #Getting the last elemnt in the array. to add onto it.        
   tempArrray = tempArrray + array1[count1: ] + array2[count2:]
   print(tempArrray)


sortLists(list1, list2)