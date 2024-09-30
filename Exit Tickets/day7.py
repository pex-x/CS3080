def reverse_string_generator(s):
    for i in range(len(s) - 1, -1, -1):
        yield s[i]
input_string = "I love vegitables12345!"
reverse_gen = reverse_string_generator(input_string)
reversed_string = ''.join([char for char in reverse_gen])
print("Reversed String: ", reversed_string)


class RangeIterator:
    def __init__(self, n):
        self.current = 4  
        self.n = n        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.n:
            current_value = self.current
            self.current += 1
            return current_value
        else:
            raise StopIteration  

try:
    n = int(input("Enter a number greater than 4: "))
    
    if n <= 4:
        print("Invalid input, n must be greater than 4.")
    else:
        range_iter = RangeIterator(n)

        print(f"Numbers from 4 (inclusive) to {n} (exclusive):")
        for number in range_iter:
            print(number)

except ValueError:
    print("Please enter a valid integer.")
