"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
and write an if- else chain.

• If the alien's color is green, print a statement that the player just earned 5
  points for shooting the alien.

• If the alien's color isn't green, print a statement that the player just earned
  10 points.

• Write one version of this program that runs the if block and another that
  runs the else block.
"""

print("\nVersion 1--------------------------\n")

alien_color1 = "green"

print("Alien Color - ", alien_color1)

if alien_color1 == "green":
    print("You have earned 5 points.")
else:
    print("You have earned 10 points.")

print("\nVersion 1--------------------------\n")

alien_color2 = "red"

print("Alien Color - ", alien_color1)

if alien_color2 == "green":
    print("You have earned 5 points.")
else:
    print("You have earned 10 points.")
