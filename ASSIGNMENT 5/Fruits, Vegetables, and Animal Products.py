fruits = ("apple", "banana", "mango")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "egg", "cheese")

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

length = len(food_stuff_lt)
middle_index = length // 2

if length % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = food_stuff_lt[middle_index]

print(f"Middle item(s): {middle_items}")

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print(f"First three items: {first_three}")
print(f"Last three items: {last_three}")

del food_stuff_tp
