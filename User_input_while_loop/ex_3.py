value="give me your age"
value+="\n write 'quit' to not participate in game. "

while True:
      
      age=int(input(value))
      if age<3:
            print("you are small")
      elif age>67:
            print("you are old ")
      elif age==input(value)=='quit':
            break
      