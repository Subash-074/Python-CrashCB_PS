#Passing Arguments 
"""
Passing Arguments 
Because a function definition can have multipele parameters a function call may need multiple arguments.
You can pass arguments to your function in a number of ways. You can use positional arguments,which needs to be in the same order the parameters were written.
"""

#Positional Arguments 

def describe_pet(animal_type, pet_name):
      print(f"\nI have a {animal_type}")
      print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')

#multiple function call
describe_pet('dog', 'willie')

#order matters in positional arguments
describe_pet('harry','hamster')

#keyword argument- end the worries of order of arguments 
describe_pet(animal_type='harry', pet_name='hamster')

#Default Values 
#When writing a function, you can define a default value for each parameter. 
"""def describe_pet(pet_name, animal_type='dog'):"""


#when you call function which have parameters  without argument you will end up in argument error