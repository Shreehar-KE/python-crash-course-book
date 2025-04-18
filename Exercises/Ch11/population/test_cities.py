"""
11-2. Population: Modify your function so it requires a third parameter, population.
It should now return a single string of the form City, Country - population xxx,
such as Santiago, Chile - population 5000000. Run the test again, and make sure
test_city_country() fails this time.

      Modify the function so the population parameter is optional. Run the test,
and make sure test_city_country() passes again.

      Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago', 'chile', and 'population
=5000000'. Run the tests one more time, and make sure this new test passes.
"""

from city_functions import city_country


def test_city_country():
    """verifying city_country() with Santiago, Chile"""
    output = city_country("santiago", "chile")
    assert output == "Santiago, Chile"


def test_city_country_population():
    """verifying city_country() with Santiago, Chile - population 5000000"""
    output = city_country("santiago", "chile", population=5000000)
    assert output == "Santiago, Chile - population 5000000"
