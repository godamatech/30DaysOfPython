Regular Expressions
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
em=[]
lengths=[]

for i in paragraph.split():
    if i not in em:
        em.append(i)

for j in em:
    lengths.append(paragraph.count(j))

for j in em:
    if max(lengths)==paragraph.count(j):
        print(paragraph.count(j), j)


#2
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4)


# Level 2
def is_valid_variable(var):
    pattern=r'^[@|#|!|~|<|>|{|}|;|\'|.|\"|:|\\|/|*|&|(|)|+|\d|-]+'
    result = re.search(pattern, var)
    if result == None:
        return True
    return False

print(is_valid_variable('.abba'))
print(is_valid_variable('/abba'))




# Level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(s):
	clean_str = re.sub('[&|@|$|#|%|;|!]', '', s)
	return clean_str

def the_3_most_freq(text):
    text = text.split()
    dct = {}
    for word in text:
        dct[word] = dct.get(word,0) + 1
    lst = [(val,key) for key,val in dct.items()]
    sorted_list =sorted(lst, reverse=True)
    return sorted_list[:3]
    
clean = clean_text(sentence)

print(the_3_most_freq(clean))

