#work to be done
#run the loop for word and their meaning in dictionary

dictionary={
      'apple':'fruit',
      'ball':'toy',
      'cat':'animal',
      'car':'transport'
}
for word, meaning in dictionary.items():
      print(word)
      print(meaning)

dictionary['lion']='king'
dictionary['tiger']='queen'
dictionary['cheeta']='minister'

print(dictionary)

for word, meaning in dictionary.items():
      print(word,':', meaning)
      

#Make a dictionary for three major rivers and the country each river runs 

c_river={
      'Nepal':'Narayani',
      'India':'Ganga',
      'Egypt':'Nile'
}
#Make a sentence about each river such as The Nile runs through Egypt

for country, river in c_river.items():
      print(f"The {river} runs through {country}.")

#Use the loop to print through each river inclueded in the dictionary 

print('\n rivers')
for river in c_river.values():
      print(river)


#Use the loop to print the name of each country included in the dictionary 
print('\n country')
for country in c_river.keys():
      print(country)



#Make a list of people who should take the pool. If they have already taken the pool, print a message thanking them for responding. If they have not yet taken the pool, print a message inviting them to take the pool. 

pool_participation ={
      'sagar':'yes',
      'niroj':'no',
      'brinda':'yes',
}

for name, status in pool_participation.items():
      if status=='yes':
            print(f"thank you {name}")
      else:
            print(f"please participate in pool {name}")