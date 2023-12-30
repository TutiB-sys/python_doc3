# Exercises
### 1) Build a Shopping Cart <br>
# <p><b>You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
# 1) Takes in input <br>
# 2) Stores user input into a dictionary or list <br>
# 3) The User can add or delete items <br>
# 4) The User can see current shopping list <br>
# 5) The program Loops until user 'quits' <br>
# 6) Upon quiting the program, print out all items in the user's list <br>
# </p>



from IPython.display import clear_output

# Ask the user 5 bits of input: Do you want to : Show/Add/Delete/clear or Quit?

items=[]

while True:
    item=input("Do you want to add item: ")
    if item.lower()== "quit":
        break
    else:
        items.append(item)
        Delete_item= input("Do you want to delte item: ")
        if Delete_item.lower()=="yes":
            items.remove(item)
        
        

print ("======= my shopping cart list========")

for item in items:
    print(f' Here is you items:  {items}')


### 2) Create a Module in VS Code and Import It into jupyter notebook <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a house <br>
#     <b>Reminder of Formula: Length X Width == Area<br>
#         <hr>
# 2) Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>
    

def module(length, width):
    area =length*width
    return area 

import math
def model2 (radius):
    circumstance=2* math.pi *radius
    return circumstance

from modeules import module
Areaofhouse=module(2,4)
print(f'area is {Areaofhouse}')

from modeules import model2
Circ=model2(7)
print(f'The circmastance of the circle is: {Circ}')