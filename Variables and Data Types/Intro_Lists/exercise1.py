#Store the names of a few friends in a list called names. Print each person's name by accessing each elementi in the list one at a time.

names= ['sagar', 'bunu', ' bimala', 'madhu']

print(names[0])
print(names[1])
print(names[2].lstrip())
print(names[3])


#Now instead of printing just names only print a message to them. 

print(f"{names[0].title()}, you are so Handsome.")
print(f"{names[1].upper()}, you are so intelligent.")
print(f"{names[2].upper().lstrip()}, you are gorgeous.")
print(f"{names[3].title()}, you are a gentleman.")