#T_shirt
def make_shirt(size, message):
      print(f"The size of the shirt is {size}")
      print(message)
make_shirt(23,'HEll NO')

#laarge shirt 

def large_shirt(size, message='I love python'):
      if size =='large':
            print(f"This is large shirt. {message}")
      elif size=='medium':
            print(f"This is medium size shirt.{message} ")
      else:
            print(f"no shirt {message}")

large_shirt('large', )


#name and city 

def describe_city( name, country):
      print(f"{name} is in {country}")

describe_city('Subash', 'Germany')
