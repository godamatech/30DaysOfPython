# Exercises: Day 13
# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i<=0]
print(negative_and_zero)
print()

# 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list1 = [col for row in list_of_lists for col in row]
list2=[i for row in list1 for  i in row]

print(list2)
print()

# 3
numbers=[f"({s},{1},{s},{s**2},{s**3},{s**4},{s**5})" for s in range(11)]
print(numbers)
print()

# # 4
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

print()

# 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_ls=[]
for row in countries:
    for coun_list in row:
        d={}
        for i in range(len(coun_list)):
            if i==0:
                d['country'] = coun_list[0]
            else:
                d['city'] = coun_list[1]
        new_ls.append(d)
for c in new_ls:
    print(c)

print()

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst = [ n[0] +" "+n[1] for name in names for n in name]
print(lst)
print()

# 7 
y_intercept = lambda x_intercept :f"The slope of interception is {(2 * x_intercept) - 2}"
print(y_intercept(5))
print()


# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened_list = [ number for row in list_of_lists for number in row]
# print(flattened_list)