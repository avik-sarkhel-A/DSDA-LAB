def print_list(lst):
    for item in lst:
        print(item)
lst = input("Enter a list of items separated by commas: ").split(',')
print("The list items are:")
print_list(lst)