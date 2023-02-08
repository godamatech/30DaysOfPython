#	Exercises: Day 8
dog = { 
"name":"shirwa", "color":"brown", "breed":"dog", "legs":4, "age":10
}

student = {
"first_name":"Abdullahi", 
"last_name":"Bello",
"gender":"Male", 
"age":20, 
"marital_status":"single", "skills":['programming', 'mathematical','problem solving'], "country":"Nigeria", 
"city":"Kaduna", 
"address":"Unguwan Rimi"
}
print(f"Length of Student Dictionary: {len(student)}")
print(student.get("skills"))
print(type(student.get("skills")))

student["skills"].append("Critical Thinking Skills")

#print(student.get('skills'))
#print(student.keys())
#print(student.values())
print(student.items())

del student["skills"]
print(student)
del student
print()

