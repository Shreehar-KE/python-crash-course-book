"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city's dictionary should be something like
country, population, and fact. Print the name of each city and all of the infor-
mation you have stored about it.

6-12. Extensions: We're now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example pro-
grams from this chapter, and extend it by adding new keys and values, chang-
ing the context of the program, or improving the formatting of the output.
"""

cities = {
    "paris": {
        "country": "france",
        "language": "french",
        "population": "11.2M",
        "fact": 'Paris was originally a Roman City called "Lutetia"',
    },
    "rome": {
        "country": "italy",
        "language": "italian",
        "population": "258K",
        "fact": "There are no cars in Venice",
    },
    "seoul": {
        "country": "south korea",
        "language": "korean",
        "population": "10M",
        "fact": "It is surrounded by 44 breathtaking mountains ",
    },
}

for city, info in cities.items():
    print(f'{city.title()} is a city in {info["country"].title()}.')
    print(f'The widely spoken language of {city.title()} is {info["language"].title()}.')
    print(f'It has a {info["population"]} population.')
    print(f'Interesting fact about {city.title()} is that {info["fact"]}.\n')
