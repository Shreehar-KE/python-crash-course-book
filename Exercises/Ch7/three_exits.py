"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:

• Use a conditional test in the while statement to stop the loop.

• Use an active variable to control how long the loop runs.

• Use a break statement to exit the loop when the user enters a 'quit' value.
"""

print("\nUsing a conditional test in the while statement to stop the loop.\n")
topping = ""
while topping != "quit":
    topping = input("What topping do you want? Enter 'quit' to stop\n---> ")
    if topping != "quit":
        print(f"Adding {topping} to your pizza")


print("\nUsing an active variable to control how long the loop runs.\n")
topping = ""
active = True
while active:
    topping = input("What topping do you want? Enter 'quit' to stop\n---> ")
    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping} to your pizza")


print("\nUse a break statement to exit the loop when the user enters a 'quit' value\n")
topping = ""
while True:
    topping = input("What topping do you want? Enter 'quit' to stop\n---> ")
    if topping == "quit":
        break
    else:
        print(f"Adding {topping} to your pizza")
