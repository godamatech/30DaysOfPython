from math import sqrt,pow
from statistics import *



# Exercises: Level 1

def add_two_numbers(n1,n2):
	return n1+n2
	
print(add_two_numbers(2,3))

def area_of_circle(r):
	pi=3.142
	return f"Area of Circle: {pi * r**2}"
	
print(area_of_circle(7))

def add_all_nums(*args):
	sum=0
	for i in args:
		if type(i) != int:
			print(i," not int")
		else:
			sum+=i
	return f"The summation of the entered numbers is {sum}"
	
print(add_all_nums(10,11,11))


def convert_celsius_to_fahrenheit(cel):
	farh= (cel * (9/5)) + 32
	return f"{cel}°C in farenheit is {farh}°F"

print(convert_celsius_to_fahrenheit(100))


def check_season(month):
	m=month.title()
	if m == "September" or m == "October" or m =="November":
		return ("The Season  is Autumn")
	elif m == "December" or m == "January" or m =="February":
		return ("The Season  is Winter")
	elif m == "March" or m == "April" or m =="May":
		return ("The Season  is Spring")
	elif m == "June" or m == "July" or m =="August":
		return ("The Season  is Summer")
	else:
		return ("{m} is an Invalid Month")

print(check_season("march"))

# print(f"The Euclidean Slope is {m}")

def calculate_slope(x1,y1,x2,y2):
	m = (y2-y1)/(x2-x1)
	return f"The slope of a linear equation is: {m}"

print(calculate_slope(2,1,4,2))

def solve_quadratic_eqn(a=2,b=6,c=3):
	squart_root = sqrt(pow(b,2) - 4*a*c)
	x1 = (-b + squart_root)/(2*a)
	x2 = (-b - squart_root)/(2*a)
	return f"x1 = {x1}\nx2 = {x2}"
	

print(solve_quadratic_eqn())


def print_list(ls):
	for i in ls:
		print(i)
	
print_list([3,5,7,9])

def reverse_list(ls):
	reversed_list=[]
	for i in range(1,len(ls)+1):
		reversed_list.append(ls[-i])
	return reversed_list

print(reverse_list([3,5,7,9]))
print(reverse_list(['A','B','C','D','E']))


def capitalize_list_items(ls):
	for i in range(len(ls)):
		ls.append(ls[i].title())
	return ls

print(capitalize_list_items(["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]))


def add_item(ls, item):
	ls.append(item)
	return ls

print(add_item(['A','B','C','D','E'], 'Alphabets'))

# Exercises: Level 2

def even_or_odd(n):
	num_of_even = 0
	num_of_odd = 0
	for i in range(n+1):
		if i%2==0:
			num_of_even+=1
		else:
			num_of_odd+=1
	return f"Number of Evens: {num_of_even}\nNumber of Odds: {num_of_odd} "

print(even_or_odd(100))

#************************************
#12
def remove_item(ls, item):
	ls.remove(item)
	return f"The List is: {ls} after {item} was removed"
	
print(remove_item([1,2,3,4,5,6], 4))

def sum_of_numbers(n):
	sum=0
	for i in range(n+1):
		sum += i
	return f"Sum of Numbers: {sum}"

print(sum_of_numbers(3))


def sum_of_odds(n):
	sum=0
	for i in range(n+1):
		if i%2==1:
			sum += i
	return f"Sum of Odds: {sum}"

print(sum_of_odds(3))


def sum_of_even(n):
	sum=0
	for i in range(n+1):
		if i%2==0:
			sum += i
	return f"Sum of Evens: {sum}"

print(sum_of_even(3))

#	Exercises: Level 2

def evens_and_odds(n):
	evens=0
	odds=0
	for i in range(n+1):
		if i%2==0:
			evens += 1
		else:
			odds+=1
	return f"Num of Evens: {evens} \nNum of Odds: {odds}"

print(evens_and_odds(3))

def factorial(n):
	res=1
	for i in range(1, n+1):
		res *= i
	return f"Factorial of {n} is: {res}"
	
print(factorial(4))

def is_empty(ls):
	if len(ls)==0:
		return f"The input: {ls} is empty: True"
	else:
		return f"The input: {ls} is empty: False"
	
print(is_empty([ 1,2,3 ]))

def calculate_mean(ls):
	sum=0
	for i in ls:
		sum+=i
	return sum/(len(ls))
print(f"Mean = {calculate_mean([ 1,2,3 ])}")
	
	
def calculate_median(ls):
	return ls[len(ls)//2]
print(f"Median = {calculate_median([ 1,2,3 ])}")

def calculate_range(ls):
	mx=max(ls)
	mn=min(ls)
	return (mx - mn)
print(f"The Range is: {calculate_range([ 1,2,3 ])}")

def calculate_mode(ls):
	d={}
	for i in ls:
	       if i not in d:
	       	d[i] =1
	       else:
	       	d[i] += 1
	for j in ls:
		if d[j] == max(d.values()):
			return j
			break

			
print("Mode",calculate_mode([ 1,3,3,3, 2,2]))

def calculate_variance(ls):
	sum_x_minus_mean = 0
	x_minus_mean = []
	m = calculate_mean(ls)
	for i in ls:
		x_minus_mean.append((i-m)**2)
		sum_x_minus_mean += ( (i-m)**2 )
	variance = sum_x_minus_mean/(len(ls)-1)
	return variance

print(f"variance: {calculate_variance([ 1,3,3,3, 2,2])}")

def calculate_std(ls):#(standard deviation)
	v = calculate_variance(ls)
	return sqrt(v)

print(f"standard deviation: {calculate_std([ 1,3,3,3, 2,2])}")


# Exercises: Level 3
def is_prime(n):
	l=[]
	res =False 
	if n==2:
		return True
	else:
		for i in range(2,(n//2)):
			if n%i==0:
				return False
				break
			else:
				res = True
		return res

print(f"Is prime: {is_prime(2)}")

def is_unique(ls):
	new=[]
	for i in ls:
		if i not in new:
			new.append(i)
	print(ls)
	print(new)
	if new == ls:
		return(f"All items are unique")
	else:return(f"All items are NOT unique")
		
print(is_unique(["a", "b", "c", "d"]))
print(is_unique(["a", "b", "c", "d", "c", "d"]))


def is_thesame_data_type(ls):
	list_type=type(ls[1])
	for i in ls:
		if type(i) !=list_type:return False
		else:return True

print(is_thesame_data_type([ ["a", "b"],"a", "b", "c", "d"]))
print(is_thesame_data_type([ "a", "b", "c", "d" ]))

def is_valid_variable(variable):
	return variable.isidentifier()

print(is_valid_variable("e1asa"))


def access_countries_data():
	from data.countries_data import my_list
	return my_list
print(access_countries_data())


#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages():
	from data.countries_data import my_list
	1111111111111111111111111

	return most_spoken_langs

print(most_spoken_languages())

def mode_test(ls):
	d={}
	for i in ls:
	       if i not in d:
	       	d[i] =1
	       else:
	       	d[i] += 1
	for j in ls:
		if d[j] == max(d.values()):
			return j
			break
			








