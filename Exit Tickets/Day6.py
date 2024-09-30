with open("data.txt", "r") as file:
    data = file.read()

wrong_info = "There can be no more than 4 football team players on the field at once. 2 players on offense and 2 players on defense can be on the field at one time."
correct_info = "There can be no more than 22 football team players on the field at once. 11 players on offense and 11 players on defense can be on the field at one time."

corrected_data = data.replace(wrong_info, correct_info)

with open("data.txt", "w") as file:
    file.write(corrected_data)

print("The file has been updated with the correct information.")
print()
print()
print()


'''-------------------------------------------------------------------------------------------------------------------'''

paragraphs = [
    "This essay is concerned with a comparison between the first generation vs. the fifth generation of computers.",
    "The first generation (1946-1959) computers were slow, huge, and expensive. In these computers, vacuum tubes were used as the basic components of CPU and memory.",
    "In the fifth generation (1980-till date) of computers, the VLSI technology was replaced with ULSI (Ultra Large Scale Integration). It made possible the production of microprocessor chips with ten million electronic components."
]

with open("/essay.txt", "w") as file:
    for paragraph in paragraphs:
        file.write(paragraph + "\n\n")  

with open("essay.txt", "r") as file:
    content = file.read().strip().split("\n\n")

    for i, paragraph in enumerate(content, start=1):
        print(f"This is paragraph number {i}:")
        print(paragraph)
        print()  
