from math import sqrt
# 30DaysOfPython Challenge
# Exercises - Day 1 (Level 2)



# 1. Checking my python version

# 2.
print(3 + 4)             # addition(+)
print(3 - 4)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(3 / 4)             # division(/)
print(3 ** 4)            # exponential(**)
print(3 % 4)             # modulus(%)
print(3 // 4)            # Floor division operator(//)

# 3.
print("Abdullahi")
print("Bello")
print("Nigeria")
print("I am enjoying 30 days of python")

# 4. Checking data types
print(type(10))          # Int
print(type(9.8))         # Float
print(type(3.14))        # Float
print(type(4 - 4j))      # Complex number
print(type(['Abdullahi', 'Python', 'Nigeria']))      # List
print(type('Abdullahi')) # String
print(type('Bello'))     # String
print(type('Nigeria'))   # String

# Exercises - Day 1 (Level 3)
0,3,99                  # Integer Number
10.3,3.0,9.9            # Float Number
#2j,i,9j                 # Complex Number
"Saleh",'Ali',"Abba"    # String
True, False             # Bolean
(5, True, 'Abdullahi')     # Tuples
{'apple','bread','grapes'}             # set
{'apple':3,'bread':5,'grapes':9}            # Dictionary

x1,y1,x2,y2 = 2,-1,-2,2
Euclidian_distance = sqrt( (x1-y1)**2 + (x2-y2)**2 )
print(f"Euclidian_distance is: {Euclidian_distance}")