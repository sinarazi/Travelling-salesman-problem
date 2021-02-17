"""
-------------------------------------------
Author : Sina Razi Moftakhar

Number : 975361014

Date : 1399/10/15
-------------------------------------------
"""

from random import random, randint  # by default system function
from TSP import Route as Chromosome


def selection(pop):  # inorder to make random numbers
    i = -1
    rand = random()

    while rand > 0:
        i += 1
        rand -= pop[i].chance
    return pop[i]


# to maintain genetic diversity from one generation of a
# population of genetic algorithm chromosomes to the next.
def mutation(population, rate):

    for chromosome in population:
        if random() < rate:
            r1 = randint(0, len(chromosome.genes) - 1)
            r2 = randint(0, len(chromosome.genes) - 1)
            # to change the place of two chromosome
            chromosome.genes[r1], chromosome.genes[r2] = chromosome.genes[r2], chromosome.genes[r1]


# to combine the genetic information of two parents to generate new offspring
def crossover(chromosome1, chromosome2):

    end = randint(0, len(chromosome1.genes))
    start = randint(0, end)
    # to select all part of chromosome1
    section = chromosome1.genes[start:end]
    # whole part of chromosome 2 in list
    offspring_genes = list(gene if gene not in section else None for gene in chromosome2.genes)
    g = (x for x in section)

    for i, x in enumerate(offspring_genes):
        if x is None:
            offspring_genes[i] = next(g)
    # finally combine two chromosomes in new offspring
    offspring = Chromosome(offspring_genes, shuffled=True)

    return offspring
