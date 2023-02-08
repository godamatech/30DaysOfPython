from math import *
# Day 2: 30 Days of python programming

# Exercises - Day 2 (  Level 1 )

first_name = "Abdullahi"
last_name = "Bello"
full_name = "Abdullahi Bello"
country = "Nigeria"
city = "Kaduna"
age = 20
year  = 2023
is_married  = False
is_true = True
is_light_on = True
a,b,c = 2,4,6

# Exercises - Day 2 (  Level 2 )
# 1.
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2.
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(country))
print(len(city))
#print(len(age)) #int does not have length
#print(len(year)) #int does not have length
print(len(str(is_married)))
print(len(str(is_true)))
print(len(str(is_light_on)))

# 3.
print( (len(first_name))==(len(last_name)) )

# 4.
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder =  num_two % num_one
exp = num_one ** num_two
floor_division = floor(num_one / num_two)

# 5.
radius = 30
area_of_circle = pi * (radius**2)
circum_of_circle = 2 * pi * radius
r = float(input("Radius: "))
area = pi * (r**2)

# 6.
first_name = input("First Name: ")
last_name = input("Last Name: ")
country = input("Country: ")
age = int(input("Age: "))

# Run help('keywords')
