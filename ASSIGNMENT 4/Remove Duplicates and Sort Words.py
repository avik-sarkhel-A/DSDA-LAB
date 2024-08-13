input_string = "hello world and practice makes perfect and hello world again"
unique_sorted_words = sorted(set(input_string.split()))
output = ' '.join(unique_sorted_words)
print(output)