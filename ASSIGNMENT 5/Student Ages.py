ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = min(ages)
max_age = max(ages)

ages.append(min_age)
ages.append(max_age)

n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]

average_age = sum(ages) / len(ages)

age_range = max_age - min_age

min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)

print(f"Sorted Ages: {ages}")
print(f"Min Age: {min_age}, Max Age: {max_age}")
print(f"Median Age: {median_age}")
print(f"Average Age: {average_age}")
print(f"Age Range: {age_range}")
print(f"Difference (Min - Avg): {min_avg_diff}, Difference (Max - Avg): {max_avg_diff}")
