# Day 17 - Exception Handling

try:
    names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
    *nordic_countries, es, ru = names
    print("Nordic Countries: ", nordic_countries)
    print(f"es: {es}")
    print(f"ru: {ru}")
except Exception as e:
    print(f"Error Occured: {e}")

