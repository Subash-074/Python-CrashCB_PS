""" Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next loop through your list and as you do, print everything you know about each pet"""


cat={ 'name':'cat',
      'type':'pet',
      'owner':'sagar',
      

}

dog={ 'name':'dog',
      'type':'pet',
      'owner':'edwardo'

}

cow={  'name':'cow',
      'type':'domestic',
      'owner':'niroj'

}

pets=[cat, dog, cow]

print('Here is the information on three animals:\n')
for animals in pets:
      for key, value in animals.items():
            print(f"{key.title()}:{value.title()}")
            


