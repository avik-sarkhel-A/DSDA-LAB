number = int(input("Enter a number: "))
if number % 7 == 0 or number % 10 == 7:
    print(f"{number} is a Buzz number.")
else:
    print(f"{number} is not a Buzz number.")
