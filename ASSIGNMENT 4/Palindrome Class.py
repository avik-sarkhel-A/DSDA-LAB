class Palindrome:
    def __init__(self, string):
        self.string = string

    def is_palindrome(self):
        return self.string == self.string[::-1]

input_string = input("Enter a string to check if it's a palindrome: ")
palindrome_checker = Palindrome(input_string)
if palindrome_checker.is_palindrome():
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")