"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print
a message saying you'll add that topping to their pizza.
"""

topping = ""

while topping != "quit":
    topping = input("What topping do you want? Enter 'quit' to stop\n---> ")
    if topping != "quit":
        print(f"Adding {topping} to your pizza")
