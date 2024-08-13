from itertools import combinations
input_string = input("Enter a string: ")
length = int(input("Enter the length of subsets: "))
subsets = [''.join(comb) for comb in combinations(input_string, length)]
print(f"All possible subsets of length {length}: {subsets}")