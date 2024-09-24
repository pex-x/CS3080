def duplicates(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    duplicates = []
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)

    if duplicates:
        print(" ".join(duplicates))
    else:
        print("")

print("Please, enter a text: ")
userInput = input()
duplicates(userInput)