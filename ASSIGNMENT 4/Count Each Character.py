input_string = "abcdefgabc"
char_count = {char: input_string.count(char) for char in set(input_string)}
for char, count in char_count.items():
    print(f"{char},{count}")