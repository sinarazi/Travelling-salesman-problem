"""
-------------------------------------------
Author : Sina Razi Moftakhar

Number : 975361014

Date : 1399/10/15
-------------------------------------------
"""

from math import hypot  # python by default libraries
from random import shuffle


class City:
    def __init__(self, name: str, coordinate: tuple):
        self._name = name
        self._x, self._y = coordinate

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    # the formula to find distance between two city with special coordinate
    @staticmethod
    def distance(city1, city2):
        return hypot(city2.x - city1.x, city2.y - city1.y)

    def __repr__(self):
        return f'{self._name}'


class Country:
    def __init__(self):
        self._cities = []

    def add(self, x):
        if isinstance(x, list):
            self.cities.extend(x)
        elif isinstance(x, City):
            self.cities.append(x)
        else:
            assert False, "Wrong type"

    @property
    def cities(self):
        return self._cities


class Route:
    def __init__(self, cities, shuffled=False):
        self._genes = cities[:]
        if not shuffled:
            shuffle(self._genes)  # shuffled and random genes should be selected
        self._fitness = None
        self.chance = None

    # to fit algorithm by the distance formula in city class
    @property
    def fitness(self):
        distances = (City.distance(self._genes[i], self._genes[i + 1]) for i in range(-1, len(self._genes) - 1))
        self._fitness = 10 / sum(distances)
        return self._fitness

    @property
    def raw_fitness(self):
        return self._fitness

    @property
    def genes(self):
        return self._genes

    def copy(self):  # inorder to duplicate
        clone = Route(self._genes, shuffled=True)
        clone._fitness = self.raw_fitness
        clone.chance = None
        return clone

    def __repr__(self):  # simple function to print the routes between 2 cities
        return f'<Route ({self._fitness})>'

    def __str__(self):  # simple function to print '->' in output
        return '->'.join(repr(city) for city in self._genes)
