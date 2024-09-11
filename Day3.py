'''
Write a Python program to reverse a list.
For example:
▶ Input: [10, 50, 75, 83, 98, 84, 32]
▶ Output: [32, 84, 98, 83, 75, 50, 10]
Samer Iskander (UCCS) Python Programming Fall 2024 31 / 36

'''


list1 = [10, 50, 75, 83, 98, 84, 32]
output = list1[::-1]
print(output)

'''
Write a Python program to get the second maximum value in this list.
For example:
▶ Input: [100, 100, 10, 20, 4, 45, 99]
▶ Output: 99
Samer Iskander (UCCS) Python Programming Fall 2024 33 / 36
'''

list2 = [100, 100, 10, 20, 4, 45, 99]
highest = 0
secondHighest = 0
for i in range(len(list2)):
    if list2[i] > highest:
        secondHighest = highest
        highest = list2[i]
    elif list2[i] > secondHighest and list2[i] != highest:
        secondHighest = list2[i]
print(secondHighest)


'''
Write a Python program to check if each number is prime in a given
list of numbers.
Return True if all numbers are prime otherwise False.
For example

'''

listNotPrime = [0, 3, 4, 7, 9]
listPrime = [3, 5, 7, 13] 
true = 1
false = 1

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(len(listPrime)):
    if is_prime(listPrime[i]):
        true += 1
    else:
        false += 1

if true == 5:
    print(True)
else:
    print(False)