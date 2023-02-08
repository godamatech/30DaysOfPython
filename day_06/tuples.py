# Exercises: Day 6
# Exercises: Level 1

empty_tuple = ()

brothers = ("Hassan", "Safiyanu", "Abubakar", "Hussaini")
sisters = ("Surayyah", "Harira", "Bilkisu", "Aisha")
siblings = brothers + sisters
print(siblings)

print(f"Number of siblings: {len(siblings)}")

family_members = brothers+sisters+("Muhammad Bello","Fa'iz") 

# Exercises: Level 2
# unpack
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Meat','Milk','Skin')
food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = food_stuff_tp
print(food_stuff_lt)

print(f"Midian Item: {food_stuff_lt[len(food_stuff_lt)//2]}")

print(food_stuff_lt)
print(food_stuff_lt[:3])

print(food_stuff_lt[:3] + food_stuff_lt[-3:])

del food_stuff_tp
# print(food_stuff_tp) #This trows an error because food_stuff_tp was deleted

print('mango' in food_stuff_lt)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


