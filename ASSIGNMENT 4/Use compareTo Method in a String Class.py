string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string1 < string2:
    print(f"{string1} is less than {string2}.")
elif string1 > string2:
    print(f"{string1} is greater than {string2}.")
else:
    print("Strings are equal.")