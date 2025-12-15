""" 4.3 Counting to twenty: use a for loop to print numbers form 1 to 20 """
"""for values in range(1,21):
      print(values)"""

""" 4.4 One Million: Make a list of the numbers form one to one million, and then use a for loop to print the numbers.( if the output is takint too long, stop it by pressing ctrl_c or by choosing output window)"""

"""numbers=[]

for number in range(1, 1000001):
      numbers.append(number)
      print(numbers)"""


""" Summing a Million: Make a list of the numbers form one to one million, and then use min() and max() to make sure you list actually starts at one and end at one million. Also use the sum function to see how quickly python add a million numbers """

"""numbers=[]

for num in range(1, 1000001):
      numbers.append(num)
      
print(min(numbers))
print(max(numbers))
print(sum(numbers))"""


""" 
4.6 Odd Numbers : Use the third argument of the range() function to make a list of the odd numbers form 1 to 20. Use a for loop to pring each number. """

"""numbers=[]
for number in range(1,20,2):
      numbers.append(number)

print(numbers)"""

"""Threes: Make a list of the multiples of 3 form 3 to 30. Use a for loop to print the numbers in your list. 
"""

"""multiples=[]
for multiple in range(3,31,3):
      multiples.append(multiple)

for values in multiples:
      print(values)
"""

""" Cubes : Make a list of first 10 cubes that is the cube form one to 10 and use a for loop to print out the value of each cube. """

"""cubes=[]

for cube in range(1,11):
      cubes.append(cube**3)

for values in cubes:
      print(values)
"""

""" Cube comprehension: Use a cube comprehension to generate a list of first 10 cubes"""

cubes= [value**3 for value in range(1,11)]
print(cubes)

#cheers you did it ...... yayaa!!!