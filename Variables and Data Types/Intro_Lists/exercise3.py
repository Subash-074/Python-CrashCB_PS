#Think of at least five place in the world you would like to visit 
visit=['california','chicago','paris', 'thailand', 'switzerland']

#print your list in its original order 
print(visit)

#use sorted to print your list in alphabetic order without modifying the actual list 
print(sorted(visit))

#show that your list is still in its original order by printing it 
print(visit)

#use reverse() to change the order of your list. print the list to show that its order has changed 
print(visit.reverse())
print(visit)

#use sort() to change your list so its stored in alphabetical order. Print the list to show that its order has been changed
visit.sort()
print(visit)

#use the sort() to change your list so its stored in reverse alphabetical order.Print the list to show that its order has changed.
visit.sort(reverse=True)
print(visit)
