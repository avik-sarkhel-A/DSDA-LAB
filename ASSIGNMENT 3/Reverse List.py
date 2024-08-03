def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
arr = input("Enter a list of items separated by commas: ").split(',')
print("The reversed list is:", reverse_list(arr))