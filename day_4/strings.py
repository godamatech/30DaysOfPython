# Exercises - Day 4

print("Thirty " + " Days " + " of " + " Python")

print("Coding " + "For " + "All")

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[:6])
print(company.index("Coding"))
print(company.find("Coding"))
print(company.replace("Coding", "Python"))

#  to Python for All
python_everyone = "Python for Everyone"
print(python_everyone.replace("Everyone", "All"))
print(company.split(" "))

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

print(company[0])
print(company[-1])
print(company[10])

pfe_dict = {'pfe':'Python For Everyone'}
print(pfe_dict['pfe'])


cfa_dict = {'cfa':'Coding For All'}
print(cfa_dict['cfa'])

print(company.index('C'))
print(company.index('F'))

print(company.rfind('l'))

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

print('You cannot end a sentence with because because because is a conjunction'.split('because because because'))

print('You cannot end a sentence with because because because is a conjunction'.index('because'))

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

print(company.startswith('Coding'))
print(company.endswith('coding'))

print('   Coding For All      '.strip())

print('thirty_days_of_python'.isidentifier())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libraries))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 8 + 6 = 14
print(f"{8} + {6} = {8+6}")
# 8 - 6 = 2
print(f"{8} - {6} = {8-6}")
# 8 * 6 = 48
print(f"{8} * {6} = {8*6}")
# 8 / 6 = 1.33
print("8 / 6 = {:.2f}".format(8/6))
# 8 % 6 = 2
print(f"{8} % {6} = {8%6}")
# 8 // 6 = 1
print(f"{8} // {6} = {8//6}")
# 8 ** 6 = 262144
print(f"{8} ** {6} = {8**6}")
