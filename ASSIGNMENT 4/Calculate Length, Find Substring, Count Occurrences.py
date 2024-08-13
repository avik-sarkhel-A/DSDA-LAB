input_string = "India is my motherland. I love my country. Capital of India is New Delhi."
length = len(input_string)
substring_count = input_string.count("country")
word_count = {word: input_string.split().count(word) for word in set(input_string.split())}

print(f"Length of string: {length}")
print(f"Occurrences of 'country': {substring_count}")
print("Word occurrences:", word_count)