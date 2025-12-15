#the if elif else chain

age=12 
if age<4:
      print('your admission cost is 0 ')
elif age<18:
      print('your adimssion cost is 25')
else:
      print('your admission cost is 40')

#here you cna also use multiple elif consditions and omit else statement if you do not want it 

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
 print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")

print("\nFinished making your pizza!")


"""   In summary, if you want only one block of code to run, use an if-elifelse chain. If more than one block of code needs to run, use a series of
independent if statements.  """