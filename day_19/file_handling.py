#Day 19 (File Handling)
#Exercises: Level 1
#  1

import os
def counter(file_name):
    num_words = 0
    num_lines = 0

    with open(file_name, "r") as f:
        for line in f:
            line = line.strip(os.linesep)
            words_list = line.split()
            num_lines += 1
            num_words += len(words_list)

    print("Number of words: ", num_words)
    print("Number of lines: ", num_lines)


print()
print("Obama Speech ")
counter('./data/obama_speech.txt')


print()
print("Michelle Obama Speech")
counter("./data/michelle_obama_speech.txt")


print()
print("Donald Speech ")
counter("./data/donald_speech.txt")


print()
print("Melania Trump Speech")
counter("./data/melina_trump_speech.txt")

#  2
import json

def most_spoken_languages(filename,value):

    languages_lst = []
    for i in json.load(open(filename,encoding="UTF8")):
        languages_lst.extend(i['languages'])

    #print('Total number of languages is',len(set(languages_lst)))
    languages_dict = {}
    for j in languages_lst:
        if j in languages_dict:
            languages_dict[j] += 1
        else:
            languages_dict[j] = 1
    # sort languages dictionary by value to get top language
    sorted_language_dict= dict(sorted(languages_dict.items(),key=lambda x:x[1],reverse=True))

    # get top languages list by passing value
    top_language = list(sorted_language_dict.items())[:value]
    print("top {} most spoken languages from the data".format(value))
    return [(i[1],i[0]) for  i in top_language]

print(most_spoken_languages('./data/countries_data.json',10))
print(most_spoken_languages('./data/countries_data.json',4))


print()
#  3
def most_populated_countries(filename,value):
    populations = {}
    for i in json.load(open(filename,encoding="UTF8")):
        populations[i["name"]] = i["population"]
    sorted_populations_dict= dict(sorted(populations.items(),key=lambda x:x[1],reverse=True))
    top_most_populated_countries = []
    for l in list(sorted_populations_dict.items())[:value]:
        top_most_populated_countries.append({'country':l[0],'populations':l[1]})

    print("top {} most populated countries in the world".format(value))
    return top_most_populated_countries

print(most_populated_countries('./data/countries_data.json',10))
print(most_populated_countries('./data/countries_data.json',4))

#Exercises: Level 2
#  4


