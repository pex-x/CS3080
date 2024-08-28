'''
Write a program to ask the user to enter a secret password. As long
as they don’t enter scuba, tell them that they did not enter the
correct password and ask for the password again. Once they enter the
correct password, tell them that they can come to the party.

Example:
Please, enter the secret password: Fred
That is not the right password
Please, enter the secret password: scuba
You can come to the party
'''

password = 'scuba'
t = True

while t:
    print("Please, enter the secret password: ")
    userInput = input()
    if(userInput != password):
        print("That is not the right password")
    else:
        print("You can come to the party")
        t = False
print('---------------------')

'''
Print each of the following series (both endpoints are inclusive):
▶ 1 to 10
▶ -5 to 5
▶ 15 to 35 by step size = 4
▶ 35 to -15 by step size = -5
'''

for i in range(1,11):
    print(i)
print('---------------------')

for x in range(-5, 7):
    print(x)
print('---------------------')

for y in range(15, 36, 4):
    print(y)
print('---------------------')

for z in range(35, -15, -5):
    print(z)
print('---------------------')

