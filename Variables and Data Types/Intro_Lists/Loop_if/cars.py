# If Statement 
#Python if statement allows you to examin the current state of a program and respond appropriately to that state.

cars=['audi', 'bmw', 'subaru', 'toyota' ]

for car in cars:
      if car=='bmw':
            print(car.upper())
      else:
            print(car.title())

#testing case sensitivity in python conditional tests
car='bmw'
car=='Bmw'

#python is case sensitive 


#to avoid this we can do 
car.title()=='Bmw'





