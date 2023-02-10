# Exercises - Day 3


age = 20
height = 1.69
complex_number = 1 - 1j

# base = float(input("Enter base of the triangle: "))
# height = float(input("Enter height of the triangle: "))
# area_of_triangle = 0.5 * base * height
# print(f"The area of the triangle is {area_of_triangle}")

# a = float(input("Enter side 'a' of the triangle: "))
# b = float(input("Enter side 'b' of the triangle: "))
# c = float(input("Enter side 'c' of the triangle: "))
# perimeter_of_triangle = a + b + c
# print(f"The perimeter of the triangle is {perimeter_of_triangle}")

length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print(f"The area of the rectangle is {area_of_rectangle}")
print(f"The perimeter of the rectangle is {perimeter_of_rectangle}")
 
r_of_circle = float(input("Enter Radius of a circle: "))
pi = 3.14
area_of_circle = pi * r_of_circle * r_of_circle
c_of_circle = 2 * pi * r_of_circle
print(f"The area of circle is {area_of_circle}")
print(f"The Circumference of circle is {c_of_circle}")

# intercept 
x_intercept = int(input("Enter x of intercept: "))
y_intercept = (2 * x_intercept) - 2
print(f"The slope of intercept is {y_intercept}")

#  Euclidean distance between point (2, 2) and point (6,10)
# x1,y1,x2,y2 = 2, 2, 6, 10 
# x1,y1,x2,y2 = eval(input("Enter 4 values in this format 'x1,y1,x2,y2' separated by comma ',': "))
# m = (y2-y1)/(x2-x1)
# print(f"The Euclidean Slope is {m}")

# Compare the slopes
# print(f"The result when the two slopes are compared is {y_intercept==m}")

# (y = x^2 + 6x + 9)
# x_of_equation = float(input("Enter the value of x for which the equation 'y = x^2 + 6x + 9' will be zero: "))
# y_of_equation = (x_of_equation**2) + (6*x_of_equation) + 9
# print(f"The Result is {y_of_equation}")

#  length of 'python' and 'dragon
# print((len("python")) != (len("dragon")))

# check if 'on' is found in both 'python' and 'dragon'
# print(f"'on' in 'python': {'on' in 'python'}")
# print(f"'on' in 'dragon': {'on' in 'dragon'}")

# sentence = "I hope this course is not full of jargon"
# print('jargon' in sentence)


# print(f"There is no 'on' in both dragon and python: {'on' not in 'dragon' and 'on' not in 'python'}")

# print(f"The float value of length of the word 'python': {float(len('python'))}")
# print(f"The String value of length of the word 'python': {str(len('python'))}")

n = 3
print(n%2==0)

print( (7//3) == 2.7)

print( '10' == 10)

print( int(9.8) == 10)

#hours = float(input("Enter# Hours: "))
#rate_per_hours=float(input("Enter Rate per Hour: "))
#print(f"Your weekly earning is {hours*rate_per_hours}")


# num_of_years_lived =float(input(f"Enter number of years you have lived: "))

# print(f"You have lived for {60*60*24*365} seconds.")

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)