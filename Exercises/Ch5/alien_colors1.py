"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

• Write an if statement to test whether the alien's color is green. If it is, print
  a message that the player just earned 5 points.

• Write one version of this program that passes the if test and another that
  fails. (The version that fails will have no output.)
"""

print("\nVersion 1--------------------------\n")

alien_color1 = "green"

print("Alien Color - ", alien_color1)

if alien_color1 == "green":
    print("You have earned 5 points.")


print("\nVersion 2--------------------------\n")

alien_color2 = "red"

print("Alien Color - ", alien_color2)

if alien_color2 == "green":
    print("You have earned 5 points.")
