"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.

• Use a for loop to print each food the restaurant offers.

• Try to modify one of the items, and make sure that Python rejects the
  change.

• The restaurant changes its menu, replacing two of the items with different
  foods. Add a line that rewrites the tuple, and then use a for loop to print
  each of the items on the revised menu.
"""

foods = ("Dosa", "Idli", "Upma", "Poori", "Chappathi")
print("Choose from the following food items:")
for food in foods:
    print(food)

# causes TypeError
# foods[0] = 'Uthaapam'

foods = ("Uthaapam", "Mini-Idli", "Upma", "Poori", "Chappathi")
print("\nFood Items has been modified. \n")
print("Choose from the following food items:")
for food in foods:
    print(food)
