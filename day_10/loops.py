#Exercises: Day 10
#  Exercises: Level 1

#from MXShare.data import countries

print("For Loop 0 to 10")
for i in range(10+1):
	print(i, end=", ")
	
print()
print("While Loop 0 to 10")
i=0
while i <= 10:
	print(i, end=", ")
	i+=1
print()
print("For Loop 10 to 0")
for i in range(10,-1,-1):
	print(i, end=", ")
	
print()
print("While Loop 10 to 0")
i=10
while i >= 0:
	print(i, end=", ")
	i-=1

for i in range(10+1):
	print(i*"#")
	
print()
for i in range(8):
	for j in range(8):
		print('# ', end="")
	print()
		
print('Multiplication Times Table')
for i in range(11):
	print(f'{i} X {i} = {i*i}')
	
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for l in lst:
	print(l)
	
print()
print("Even Numbers from 0 to 100")
for x in range(101):
	if x%2 == 0:
		print(x, end=", ")
		
print()
print("Odd Numbers from 0 to 100")
for x in range(101):
	if x%2 == 1:
		print(x, end=", ")

#  Exercises: Level 2
print()
sum =0
for x in range(101):
	sum +=x
print(f"Sumation of Numbers from 0 to 100 is: {sum}")

print()
sum_even =0
sum_odd =0
for x in range(101):
	if x%2==0:
		sum_even +=x
	else:
		sum_odd +=x

print(f"Summation of Even Numbers is: {sum_even}\nSummation of Odd Numbers is:  {sum_odd}")


#  Exercises: Level 3
#for c in countries:
#	if 'land' in c:
#		print(c)

f_list = ['banana', 'orange', 'mango', 'lemon']
reverse_f_list = [ ]
for i in range(1, len(f_list) +1):
	reverse_f_list.append(f_list[-i])
print(reverse_f_list)


#print()
#tot_langs = 0
#for lang in count_data:
#	tot_langs += len(lang.get('languages'))
#print(f'Total Langauges are: {tot_langs}')

#

#


#leng=0
#n_of_leng = []
#for i in my_list:
#	#print(i.get('population'))
#	leng =i.get('population')
#	n_of_leng.append(leng)
#	
#sorted_list=sorted(set(n_of_leng), reverse=True)
#max_10 =[]
#for i in range(10):
#	 max_10.append(sorted_list[i])

#print(f'The 10 most populated countries in the world: {max_10}')




