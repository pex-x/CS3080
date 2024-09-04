'''
Problem Statement:
▶ Write a Python program that has a function that accepts 3 parameters.
▶ Each parameter represents a side of the three sides of a triangle.
▶ The function returns the largest side.
▶ If the three sides could not possibly make a triangle, return ”Not a
Triangle”.
▶ How do we determine if a triangle is valid based on its 3 sides?
⋆ The sum of two side lengths of a triangle is always greater than the
third side.
Examples:
print(find largest side(4, 7, 5)) # 7
print(find largest side(4, 9, 4)) # Not a Triangle
print(find largest side(1, 2, 3)) # Not a Triangle
Samer Iskander (UCCS) Python Programming Fall 2024 43 / 45
'''


def findLargestSide(x, y, z):
    if((x > y) & (x > z)):
      if(y+z <= x):
         return("Not a Triangle")
      else:
         return(x)
    elif((y > x) & (y > z)):
      if(x+z <= y):
         return("Not a Triangle")
      else:
         return(y)
    elif ((z > x) & (z > y)):
      if(x+y <= z):
         return("Not a Triangle")
      else:
         return(z)
      

print(findLargestSide(4, 7, 5)) # 7
print(findLargestSide(4, 9, 4)) # Not a Triangle
print(findLargestSide(1, 2, 3)) # Not a Triangle