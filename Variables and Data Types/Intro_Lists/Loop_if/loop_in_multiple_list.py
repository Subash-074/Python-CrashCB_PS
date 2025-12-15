# Let's say we have toppings options available which is usual and some customers might request for unusual toppings in that case we have minimus options available as well in that case we can use multiple lists.

available_toppings=['mushrooms', 'olives', ' green peppers', 'pepperoni', 'extra cheese']
requested_toppings=['mushrooms','french fries','olives']



for requested_topping in requested_toppings:
      if requested_topping in available_toppings:
            print(f"adding {requested_topping}")
      else:
            print(f"sorry we dont have {requested_topping}")
print('finished making your pizza')
