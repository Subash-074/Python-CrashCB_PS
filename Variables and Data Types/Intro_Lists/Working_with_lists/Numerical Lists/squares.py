#You can create almost any set of numbers you want using the range() function 
#consider how you might make a square of first 10 square numbers 

squares=[] #here we created a list so that we could put squared values

for values in range (1,11):
      square=values**2 #we squared each values
      squares.append(square) #we kept each squared values to the squares using append method 

print(squares)


#simple statistics with a list of numbers 

digits=[1,2,3,4,5,6,7,8,9,0]

print(min(digits))
print(max(digits))
print(sum(digits))



#list comprehension 

""" A list comptehension allows you to generate list in just one line of code. It combines for loop and the creation of new elements into one line. """


cubes=[value**3 for value in range(1,11)]
print(cubes)
