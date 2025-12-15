#Guest List 
""" if you could invite anyone living or deceased to dinner, who would you invite? Make a list that includes at least three people you would like to invite to dinner. Then use your list to print a message to each person inviting them to  dinner."""

dinner_guest=['tikaram','gita', 'jyoti', 'sovakhar', 'sandhya']

print(f"{dinner_guest[0].title()}, Brother I am hosting a dinner this Friday you are invited.")
#do same to other as well 


#Changing a guest list 
""" You just heard that one of your guest can't make the dinner, so you need to sent out a new set of invitations. You will have to think of someone else to invite.
"""
dinner_guest.pop(1)
dinner_guest.insert(1, 'ram')
print(dinner_guest)

#more guest 

""" You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner"""

#Use insert() to add one new guest to the beginning of your list.
dinner_guest.insert(0, 'sagar')
#Use insert() to add one new guest to the middle of your list.
dinner_guest.insert(2, 'bimala')
#Use append() to add one new guest to the end of your list.
dinner_guest.append('hari')

print(dinner_guest)



#Shrinking Guest list 
print('I can invite only two people for dinner.')

dinner_guest.pop()
dinner_guest.pop()
dinner_guest.pop()
dinner_guest.pop()
dinner_guest.pop()
dinner_guest.pop()

print(dinner_guest)

print(f"{dinner_guest[0].title()}, brother you are still invited for dinner.")
print(f"{dinner_guest[1].title()}, brother you are still invited for dinner.")

#use del statemsnt to empty your list
del dinner_guest[0]#first index element deleted 
del dinner_guest[0]#now there is only one element
print(dinner_guest)