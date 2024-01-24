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


shopping_cart = {}

while True:
    response=input('What would you like to do? : \n -add \n -delete \n -show \n -quit ')
    clear_output

    if response.lower()=='add':
        item=input('Enter the item : ')
        quantity=int(input('Enter the quantity: '))
        shopping_cart[item]= quantity
    elif response.lower()== 'delete':
        itemToDelete= input('Enter the item you want to delete')
        if itemToDelete in shopping_cart:
            del shopping_cart[itemToDelete]
        else:
            print('item is not found')
    elif response.lower()=='show':
        for item, quantity in shopping_cart.items():
            print(f'{item}: {quantity}')
    elif response.lower()== 'quit':
        print(your cart is: \n {shopping_cart}')
        print('Thank you for shopping with us!!!')
        break
    else:
        print('Please enter a valid option' )

### 2) Create a Module in VS Code and Import It into Jupyter Notebook <br>
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
