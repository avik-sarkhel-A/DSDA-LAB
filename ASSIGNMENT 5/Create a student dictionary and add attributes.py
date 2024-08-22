student = {
    'first_name': 'AVIK',
    'last_name': 'SARKHEL',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Java', 'C++'],
    'country': 'INDIA',
    'city': 'KOLKATA',
    'address': 'RAJA SC MULLICK ROAD'
}

print("Length of student dictionary:", len(student))

skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))

student['skills'].extend(['JavaScript', 'HTML'])

keys_list = list(student.keys())
print("Keys:", keys_list)

values_list = list(student.values())
print("Values:", values_list)

items_list = list(student.items())
print("Items as list of tuples:", items_list)

del student['marital_status']

del student