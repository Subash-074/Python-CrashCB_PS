#Using Variables in String 
first_name='subash'
last_name='sapkota'
full_name= f"{first_name} {last_name}"
print(full_name)

#you can do a lot with f_strings 

message=f"Hello, {full_name.title()}!"
print(message)

#strippint whitespaces 
name=' My name is Subash'
identity='I am male '
l_name= ' sapkota '

print(name.lstrip())

print(l_name.rstrip())
print(identity.rstrip())