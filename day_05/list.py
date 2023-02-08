#Exercises: Day 5
#Exercises: Level 1
from math import ceil

empty_list = []
list_5_items= [ 'a', 'b', 'c', 'd', 'e']

print(len(list_5_items))

print(list_5_items[0])
print(list_5_items[len(list_5_items)//2])
print(list_5_items[-1])

mixed_data_types = ["Abdullahi Bello", 20, 1.68, "single", "Kaduna"]

it_companies = [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon" ]
print(it_companies)

print(len(it_companies))

print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[-1])

it_companies[0] = "Telegram"
print(it_companies)

it_companies.append("Whatsapp")
it_companies.insert(len(it_companies)//2, "Tik Tok")
it_companies[1] = it_companies[1].upper()

print('#; '.join(it_companies))
print('Amazon' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

print(it_companies[:3])
print(it_companies[-3:])

print(it_companies[len(it_companies)//2])

print(it_companies.pop(0))
print(it_companies)

print(it_companies.pop(len(it_companies)//2))
print(it_companies)
print(it_companies.pop(-1))
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)

full_stack = front_end.extend(back_end)
print(full_stack)

# full_stack.insert(5, 'Python')
# full_stack.insert(6, "SQL")

print(full_stack)


# Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
print(ages[len(ages)//2])

sum_age = 0
age_counter = 0
for i in ages:
    sum_age += i
    age_counter += 1
average = sum_age/age_counter
print(average)  #AVERAGE

print( max(ages) - min(ages) )
print(abs(min(ages) - average) == abs(max(ages) - average) )

countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(countries_list[len(countries_list)//2])

if (len(countries_list)%2) == 1:
    print( (len(countries_list)//2) + 1)

first, second, third, *scandic = countries_list
print(scandic)
print(f"countries: {countries[:20]}")
