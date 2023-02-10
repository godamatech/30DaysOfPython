#Exercises: Day 12
#Exercises: Level 1

import string as s
from random import random,randint,choices

def random_user_id(n):
	id="".join(choices(s.digits ,k=n))
	return id

print(random_user_id(6))
print()


def user_id_gen_by_user():
	n_char=int(input(" Enter the number of characters: "))
	n_id=int(input(" Enter the number of IDs: "))
	gen_char = "".join(choices(s.ascii_letters, k=n_char))
	gen_id = "".join(choices(s.digits, k=n_id))
	return gen_char+str(gen_id)
	
print(user_id_gen_by_user())
print()


def rgb_color_gen():
	rgb=[]
	for i in range(3):
		g_num= randint(0,255)
		rgb.append(g_num)
	return  f"rgb{tuple(rgb)}"

print(rgb_color_gen())
print()

#	Exercises: Level 2

def list_of_hexa_colors(n=1):
	sample = "abcdef0123456789"
	arr=[]
	for i in range(n):
		hex="".join(choices(sample,k=6))
		arr.append('#'+hex)
	return f"{arr}" 

print(list_of_hexa_colors(3))
print(list_of_hexa_colors())
print()

def list_of_rgb_colors(n=1):
	rgb=[]
	rgb_list=[]
	for r in range(n):
		rgb=[]
		for i in range(3):
			
			g_num= randint(0,256)
			rgb.append(g_num)
		rgb_list.append(f"rgb{tuple(rgb)}")
	return  rgb_list

print(list_of_rgb_colors(3))
print()

def generate_colors(color_type, num):
	if color_type.startswith("hex"):
		return list_of_hexa_colors(num)
	elif color_type.startswith("rg"):
		return list_of_rgb_colors(num)
	else:return None
	
print(generate_colors('rgb', 2))
print(generate_colors('hex', 2))
print()

#	Exercises: Level 3

def shuffle_list(ls):
	new=[]
	counter=0
	while counter < len(ls):
		ch = choices(ls)
		if ch not in new:
			new.append(ch)
			counter += 1
		else: continue
	return new
print(shuffle_list([9,8,7,6,5]))
print()

def seven_ran_num_arr():
	num=s.digits
	arr=[]
	i=0
	while i < 7:
		item = choices(num, k=1)
		if item not in arr:
			arr.append(item)
			i+=1
	return arr

print(seven_ran_num_arr())
print()
