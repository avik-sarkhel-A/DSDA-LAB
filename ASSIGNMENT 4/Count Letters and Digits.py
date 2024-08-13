input_string = "hello world! 123"
letters_count = sum(c.isalpha() for c in input_string)
digits_count = sum(c.isdigit() for c in input_string)

print(f"LETTERS {letters_count}")
print(f"DIGITS {digits_count}")