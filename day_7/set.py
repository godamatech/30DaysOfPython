# Exercises: Day 7
# Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f"length it_companies set: {len(it_companies)}")

it_companies.add('Twitter')

it_companies.update(["Telegram","Whatsap"])
# print(it_companies)

it_companies.pop()
# print(it_companies)

it_companies.remove("Twitter")  #returns 'error' when the item is not found in the set
it_companies.discard("Google")  #does not returns 'error' when the item is not found in the set
print(it_companies)

# Exercises: Level 2

print(f"A U B: {A.union(B)}")
print(f"A n B: {A.intersection(B)}")

print(f"is A subset of B: {A.issubset(B)}")
print(f"Are A and B disjoint sets: {A.isdisjoint(B)}")

print(f"A U B: {A.union(B)} and B U A: {B.union(A)}")

print(f"Symmetric difference between A and B: {A.symmetric_difference(B)}")

del A
del B

# Exercises: Level 3
age_set = set(age)
print(len(age_set) == len(age))

# string is any collection of one or more characters whithin a single or double qouotes
# list is a mutable collection of one or more items refferenced using a single variable name
# tuple is a unmutable collection of one or more items refferenced using a single variable name
# set is an unordered collection of one or more unique items refferenced using a single variable name

sentence="I am a teacher and I love to inspire and teach people."
unique = set(sentence.split())
print(f"How many unique words have been used in the sentence? {len(unique)}")

