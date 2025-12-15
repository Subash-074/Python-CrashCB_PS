motorcycles=['honda', 'yamaha', 'suzuki']

#modifying elements in a list 
motorcycles[0]='ducati'

print(motorcycles)

#adding elements to a list using append 
motorcycles.append('pulsar')
print(motorcycles)


#inserting elements into a list 
motorcycles.insert(0, 'duke')
print(motorcycles)

#removing items using del statement 
del motorcycles[4]
print(motorcycles)

#removing items using pop method 
poped_motorcycles=motorcycles.pop()
print(poped_motorcycles)

print(f"My favouriate motorcytles among all the motorcycles I have bought was {poped_motorcycles.title()}.")

#poping motorcyles form any position
first_owned=motorcycles.pop(0)
print(f"The first motorcycle that I purchased was {first_owned.title()}.")


#remember each time you use the pop() method, hte item you work with is no longer stored in the list.
print(motorcycles)#see duke and suzuki gone in terminal because they were popped hehe you got it right!!



#removing items by value 
friends=['sagar', 'basantey', 'krishney']
friends.remove('sagar')
print(friends)

nautty_friend='basantey'
friends.remove(nautty_friend)
print(friends)

print(f"{nautty_friend.title()} was the nauttiest among my three closest friends.")
