#Alien colors  using if else 

alien='yellow'
if alien=='green':
      print('You earned 5 points')
else:
      print('You earned 0 points')
#alien colors _if block executed 

alien2='green' 
if alien2=='green':
      print('You earned 5 points.')
elif alien2!='green':
      print('you earned 10 points')


#alien colors else block executed 

alien3='yellow'
if alien3=='green':
      print('you earned 5 points ')
elif alien3!='green':
      print('You earned 10 points')



#stages of life 

age=int(input('your age '))
if age<2:
      print('you are baby')
elif age>=2 and age<4:
      print('you are toddler')
elif age>=4 and age<13:
      print('you are a kid')
elif age>=13 and age<20:
      print('you are a teenager')
elif age>=20 and age<65:
      print('You are an adult')
elif age>=65:
      print('You are an elder citizen')
