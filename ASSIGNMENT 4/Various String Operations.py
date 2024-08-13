input_string = "hello"
reversed_string = input_string[::-1]
is_palindrome = input_string == input_string[::-1]
ends_with = input_string.endswith("lo")
capitalized_words = input_string.title()
another_string = "olelh"
is_anagram = sorted(input_string) == sorted(another_string)
vowels = "aeiou"
no_vowels = ''.join([char for char in input_string if char not in vowels])
sentence = "This is a sample sentence"
longest_word_length = max(len(word) for word in sentence.split())

print(f"Reversed: {reversed_string}")
print(f"Is Palindrome: {is_palindrome}")
print(f"Ends with 'lo': {ends_with}")
print(f"Capitalized: {capitalized_words}")
print(f"Is Anagram: {is_anagram}")
print(f"No Vowels: {no_vowels}")
print(f"Length of Longest Word: {longest_word_length}")