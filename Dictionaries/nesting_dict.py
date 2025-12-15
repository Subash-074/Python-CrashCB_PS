#Nesting 
#Sometimes you will want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. this is called nesting

#A list of Dictionaries:

"""
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]



for alien in aliens:
      print(alien)"""



#now we will create a fleet of 30 aliens

aliens=[]

for alien_number in range(30):
      new_alien={'color':'green', 'points':'5', 'speed':'slow'}
      aliens.append(new_alien)
 #show first five aliens 


for alien in aliens[:5]:
      print(alien)   


#show total number of aliens 
print(len(aliens))



#here all 30 aliens are same but python considers one a separate object, which allows us to modify each alien individually. 

#let's say we want to modify first three aliens

for alien in aliens[:3]:
      if alien['color']=='green':
          alien['color']='yellow'
          alien['speed']='medium'
          alien['points']=10


for alien in aliens[:5]:
      print(alien)


#A List in a Dictionary 
"""sometimes people could choose more than one favorite
language. """



favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }

for name, languages in favorite_languages.items():
      print(f"\n{name.title()}'s favouriate language are:")
      for language in languages:
                print(f"\t{language.title()}")

#Here in such conditions we can use double for loops. 



