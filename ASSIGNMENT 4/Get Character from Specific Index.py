input_string = input("Enter a string: ")
index = int(input("Enter the index: "))
if 0 <= index < len(input_string):
    print(f"Character at index {index}: {input_string[index]}")
else:
    print("Index out of range.")