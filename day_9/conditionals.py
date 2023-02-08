#Exercises: Day 9
#Exercises: Level 1

#while True:
#	user_input=int(input("Enter your age: "))
#	if user_input >= 18:
#		print("You are old enough to drive.")
#	elif user_input<18:
#		print(f"You need {18-user_input} more years to learn to drive.")
#		break
		
		
#my_age = int(input("Enter my age: "))
#your_age = int(input("Enter your age: "))
#age_diff = your_age - my_age
#if (age_diff) ==1:
#	print("Year")
#elif age_diff > 1:
#	print("Years")
#elif age_diff ==0:
#	print("Years")
	

#a = int(input("Enter number one:  "))
#b = int(input("Enter number two: "))
#if a > b:
#	print(f"{a} is greater than {b}")
#elif a < b:
#	print(f"{a} is less than {b}")
#else:
#	print(f"{a} is equal to {b}")


#score = int(input("Enter your score:  "))
#g = ""
#if score <= 49:
#	g = "F"
#elif score <= 59:
#	g = "D"
#elif score <= 69:
#	g = "C"
#elif score <= 89:
#	g = "B"
#elif score <= 100:
#	g = "A"
#else:
#	g = "Invalid Score"
#print(f"Grade: {g}")

#m = input("Enter Month: ").title()
#if m == "September" or m == "October" or m =="November":
#	print("The Season  is Autumn")
#elif m == "December" or m == "January" or m =="February":
#	print("The Season  is Winter")
#elif m == "March" or m == "April" or m =="May":
#	print("The Season  is Spring")
#elif m == "June" or m == "July" or m =="August":
#	print("The Season  is Summer")
#else:
#	print("{m} is an Invalid Month")


#fruits = ['banana', 'orange', 'mango', 'lemon']
#fruit = input("Fruit Name: ").lower()
#if fruit in fruits:
#	print('That fruit already exist in the list')
#else:
#	fruits.append(fruit)
#	print(f'The Modified list of fruits is {fruits}')
	

#Exercises: Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210' }
        }
print('skills' in person)
print(f"The middle skill in the skills list is '{ person['skills'][len(person['skills'])//2] }'")

print('Python' in  person["skills"])
print(person["skills"][-1])
	

if 'Node' in person['skills']:
	if 'React' in person['skills'] and 'MongoDB' in person['skills']:
		print('He is a fullstack developer')
	elif 'Python' in person['skills'] and 'MongoDB' in person['skills']:
		print('He is a backend developer')
elif  'React' in person['skills'] and 'JavaScript' in person['skills']:
	print('He is a front end developer')
else:
	print('unknown title') 
	
if person['is_marred'] and person['country']=='Finland':
	print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")

