#A simple dictionary 
""" A dictionary in python is a collection of key value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. 
"""
alien_0={ 'color':'green', 'points':5}

# to access value form dictionary call dictionary and its associated key then value will be displayed as an output
print(alien_0['color'])
print(alien_0['points'])


"""A key-value pair is a set of values associated with each other. When you
provide a key, Python returns the value associated with that key"""


new_points=alien_0['points']
print(f"you just earned {new_points} points. ")


#Adding a new key_value pairs 

alien_0['x_position']=0
alien_0['y_position']=25


print(alien_0)


#starting with an empty dictioinary 

hallios={}

hallios['color']='green'
hallios['points']=5

print(hallios)
print(f"The hallios is {hallios['color']}.")

#modifying values in a dictionary 
hallios['color']='yellow'

print(f"The hallios is now {hallios['color']}.")


#Now let's track the position of an alien that can move at different speeds. we'll store a value representing the alien's current speed and then use it to determine how far to the right the alien should move.



alien= {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"The original position {alien['x_position']}")
#move the alien to the right 

if alien['speed']=='slow':
      x_increment=1
elif alien['speed']=='medium':
      x_increment=2
else:
      x_increment=3

alien['x_position']=alien['x_position']+ x_increment


print(f"The new positoin: {alien['x_position']}")



#Removing key_value pair 

del alien_0['points']

print(alien_0)


#A Dictionary of similar objects 
favouriate_languages={
'jen':'python',
'edward':'c',
'phil':'python',
}


language=favouriate_languages['edward'].title()


print(f"Sarah's favouriate language is {language}.")

#Using get to access value 
""" using key in square bracket to retrive the value you are interested in from a dictionary might cause one potential problem if the key you ask for doesn't exist you will get an error """

alienn_0={'color':'green', 'speed':'slow'}
"""  print(alienn_0['points'])
this will cause error """
point_value=alienn_0.get('points', 'no point value assigned')
print(point_value)