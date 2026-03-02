#Garbage Collection in Python
""" A virtual assistant in Python Virtual Machine that helps to remove and delete useless objects in python code. It is always running in the background. This is Garbage collector 

The useless objects collected in PVM are Garbage collection.   


What are useless objects?
Those objects that have 0 refrence variable. These objects are eligible for garbage collection. 


"""

import gc
gc.enable()

#we will always keep our garbage collector on and enabled. 

#Destructor 
""" 
Destructor helps in deallocation or (disconnection)of  resources form object before being removed or destroyed by garbage collector. 
"""

"""
def __init__(self):
...............
...............
...............     ==== constructor 


def __init__(self):
..............
..............
..............   ==== Destructor 





"""

