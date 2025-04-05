"""
5-5. Alien Colors #3: Turn your if- else chain from Exercise 5-4 into an if- elif-
else chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed
  for the appropriate color alien.
"""

print("\nVersion 1--------------------------\n")

alien_color1 = "green"

print("Alien Color - ", alien_color1)

if alien_color1 == "green":
    print("You have earned 5 points.")
elif alien_color1 == "yellow":
    print("You have earned 10 points.")
else:
    print("You have earned 15 points.")

print("\nVersion 2--------------------------\n")

alien_color2 = "yellow"

print("Alien Color - ", alien_color2)

if alien_color2 == "green":
    print("You have earned 5 points.")
elif alien_color2 == "yellow":
    print("You have earned 10 points.")
else:
    print("You have earned 15 points.")

print("\nVersion 3--------------------------\n")

alien_color3 = "red"

print("Alien Color - ", alien_color3)

if alien_color3 == "green":
    print("You have earned 5 points.")
elif alien_color3 == "yellow":
    print("You have earned 10 points.")
else:
    print("You have earned 15 points.")
