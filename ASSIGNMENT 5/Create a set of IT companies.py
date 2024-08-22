it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

length_of_it_companies = len(it_companies)

it_companies.add('Twitter')

it_companies.update({'Snapchat', 'LinkedIn'})

it_companies.remove('Oracle')

print(f"Length of IT Companies: {length_of_it_companies}")
print(f"IT Companies after addition: {it_companies}")