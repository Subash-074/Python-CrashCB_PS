#looping Through a Dictionary 
""" sometimes key value pairs in dictionary might be huge and you might go through looping in dictionary."""

#looping through all key value pairs 
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in user_0.items():   
      print(f"\nKey:{key}")
      print(f"Value:{value}")



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil':'python',
}


for name, language in favorite_languages.items():
      print(f"{name.title()}'s favouriate language is {language.title()}.")


#looping through all the keys in a dictionary 

for name in favorite_languages.keys():
      print(name.title())


#looping through a dictionary's keys in a particular order 
print(
'The following languages have been mentioned:'
)

for name in sorted(favorite_languages.keys()):
      print(f"{name.title()}, thank you for taking the pool.")

#loopint through values in particular order 
for language in favorite_languages.values():
      print(language.title())

""" This approach pulls all the valus form the dictionaty without checking for repeats. That might work fine with a small number of values, but in a poll with a large number of respodents, this would result in very repetitive list to see each language chosen without repetition, we can use a set. 


 A set is a collection in which each item must be unique"""

print(" The following languages have been mentioned:")

for language in set(favorite_languages.values()):
      print(language.title())

#now you can see  values are not repeated

