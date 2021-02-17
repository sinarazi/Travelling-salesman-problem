"""
-------------------------------------------
Author : Sina Razi Moftakhar

Number : 975361014

Date : 1399/10/15
-------------------------------------------
"""

from TSP import *  # the module that we made
from myLib.Genetic_Algorithm import GeneticAlgorithm  # the module that we made in myLib folder


def main():
    """
    I have decided to write your dataset here and instead of numbers I've written city's names.
    """
    iran = Country()  # call TSP.py Country class
    iran.add([
        City('Urmia', (37, 52)),
        City('Tabriz', (49, 49)),
        City('Tehran', (52, 64)),
        City('Mashhad', (20, 26)),
        City('Isfahan', (40, 30)),
        City('Karaj', (21, 47)),
        City('Shiraz', (17, 63)),
        City('Qom', (31, 62)),
        City('Ahvaz', (52, 33)),
        City('Kermanshah', (51, 21)),
        City('Rasht', (42, 41)),
        City('Zahedan', (31, 32)),
        City('Kerman', (5, 25)),
        City('Yazd', (12, 42)),
        City('Ardabil', (36, 16)),
        City('Bandar Abbas', (52, 41)),
        City('Arak', (27, 23)),
        City('Eslamshahr', (17, 33)),
        City('Qazvin', (13, 13)),
        City('Zanjan', (57, 58)),
        City('Khorramabad', (62, 42)),
        City('Sanandaj', (42, 57)),
        City('Jolfa', (16, 57)),
        City('Bonab', (8, 52)),
        City('Qods', (7, 38)),
        City('Kashan', (27, 68)),
        City('Gorgan', (30, 48)),
        City('Golestan', (43, 67)),
        City('Sari', (58, 48)),
        City('Shahriar', (58, 27)),
        City('Dezful', (37, 69)),
        City('Borujerd', (38, 46)),
        City('Nishapur', (46, 10)),
        City('Sabzevar', (61, 33)),
        City('Ilam', (62, 63)),
        City('Birjand', (63, 69)),
        City('Maragheh', (32, 22)),
        City('Hamadan', (45, 35)),
        City('Bukan', (59, 15)),
        City('Semnan', (5, 6)),
        City('Marand', (10, 17)),
        City('Bam', (21, 10)),
        City('Miandoab', (5, 64)),
        City('Ahar', (30, 15)),
        City('Iranshahr', (39, 10)),
        City('Mahabad', (32, 39)),
        City('Zabol', (25, 32)),
        City('Khoy', (25, 55)),
        City('Maku', (48, 28)),
        City('Quchan', (56, 37)),
        City('Lahijan', (30, 40))
    ])

    print('Cities:', end=' ')
    print(*(city for city in iran.cities), sep=', ')  # to iterate the cities
    # call GeneticAlgorithm class
    ga = GeneticAlgorithm(100, mutation_rate=0.5, p_type=Route, args=(iran.cities,))
    ga.run(seconds=10)

    fittest = ga.all_time_best
    best_fitness = fittest.fitness

    print('Best route:', fittest)
    print('Best fitness:', best_fitness)
    print('Generations:', ga.generation)


if __name__ == '__main__':  # to begin main function
    main()


