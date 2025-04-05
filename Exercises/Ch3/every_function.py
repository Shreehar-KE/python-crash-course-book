"""
3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you'd like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.
"""

locations = ["svalbard", "paris", "maldives", "venice", "ha long bay"]
print("Original List:")
print(locations)
print("\nAppending Santorini")
locations.append("santorini")
print(locations)
print("\nInserting Switzerland at index 1")
locations.insert(1, "switzerland")
print(locations)
print("\nDeleting the location at index 5")
del locations[5]
print(locations)
print("\nInserting Ha Long Bay at index 5")
locations.insert(5, "ha long bay")
print(locations)
print("\nTemporary sorting using sorted() function")
print(sorted(locations))
print("\nOriginal List:")
print(locations)
print("\nPermanent sorting using sort() method")
locations.sort()
print(locations)
print("\nReversing the list using reverse() method")
locations.reverse()
print(locations)
print("\nLength of the list")
print(len(locations))
print("\nPopping the last location")
print(locations.pop())
print(locations)
print("\nPopping the location at index 2")
print(locations.pop(2))
print(locations)
print("\nRemoving Paris")
locations.remove("paris")
print(locations)
