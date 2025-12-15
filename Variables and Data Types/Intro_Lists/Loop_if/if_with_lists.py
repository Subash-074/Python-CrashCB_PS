#Using if statements with lists 
requested_toppings=['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
      print('sorry, we are out of green peppers right now. ')
    else:
       print(f"adding{requested_topping}")

print('\n Finished making your pizza')


#checking that a list is not empty

requested_toppings1 = []
 
if requested_toppings1:
   for requested_tppping in requested_toppings1:
      print(f"adding{requested_topping}")
      print('finished making your pizza')
else:
   print('are you sure you want plain pizza')



