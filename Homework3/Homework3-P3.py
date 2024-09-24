def count_characters(text):
    count = 0  
    
    for char in text:  
        if char != ' ':  
            count += 1
    return count

print("Please, enter a text: ")
user_input = input()
result = count_characters(user_input)
print(result)