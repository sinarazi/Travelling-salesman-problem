"""
-------------------------------------------
Author : Sina Razi Moftakhar

Number : 975361014

Date : 1399/10/15
-------------------------------------------
"""

from myLib.genetic import selection, mutation, crossover
import time


class GeneticAlgorithm:
    def __init__(self, size, mutation_rate=0.01, p_type=None, args=tuple()):
        # used when sth is not true
        assert p_type is not None, 'Population type cannot be None'
        assert type(args) == tuple, 'Arguments must be a tuple instead of ' + str(type(args))
        # initialize first class objects
        self._population = [p_type(*args) for _ in range(size)]
        self._mutation_rate = mutation_rate
        self._generation = 0
        self._fittest = self._population[0]
        self.evaluation()

    # chromosomes of populations
    def individuals(self):
        for chromosome in self._population:
            yield chromosome

    # aggregate two chromosome and dividing to numbers to get the probabilities
    def evaluation(self):
        fitness_sum = sum(chromosome.fitness for chromosome in self._population)
        for chromosome in self._population:
            chromosome.chance = chromosome.fitness / fitness_sum

    # to get elite population by finding maximum value of population
    def best(self):
        return max(self._population, key=lambda k: k.fitness)

    @property
    def all_time_best(self):
        return self._fittest

    @property
    def generation(self):
        return self._generation

    """
    Inorder to get next generation we have to select random chromosomes
    then by crossover function, combine them, then append them to new_population,
    then, by mutation, the function to generate next generation,
    we are going to evaluate them and find the probability and chance value.  
    """
    def next_generation(self):
        new_population = []
        for _ in range(len(self._population)):
            chromosome1 = selection(self._population)
            chromosome2 = selection(self._population)
            new_population.append(crossover(chromosome1, chromosome2))
            mutation(new_population, self._mutation_rate)
        self._population = new_population
        self.evaluation()

    def run(self, seconds=5, reps=None):
        if reps is not None:
            assert isinstance(reps, int), 'Argument `reps` must be of integer type'

            for _ in range(reps - 1):
                pretender = self.best()
                if pretender.fitness > self._fittest.raw_fitness:
                    self._fittest = pretender.copy()

                self._generation += 1
                self.next_generation()
            pretender = self.best()
            """
            fitness of chromosomes by evaluate their success of life,
            by comparing their high fitness. 
            """
            if pretender.fitness > self._fittest.raw_fitness:
                self._fittest = pretender.copy()
            self._generation += 1
        else:
            t0 = time.time()
            while True:
                pretender = self.best()
                if pretender.fitness > self._fittest.raw_fitness:
                    self._fittest = pretender.copy()

                self._generation += 1
                if time.time() - t0 >= seconds:
                    break
                self.next_generation()
