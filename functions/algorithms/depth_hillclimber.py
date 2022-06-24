import random
import copy
from functions.helpers.calculation import calculate_quality
from functions.helpers.visualisation import visualisation
from functions.algorithms.randomise import random_function
from functions.algorithms.get_first_option import get_first_option

class DepthFirstHillclimber:
    """
    The HillClimber class first creates a random solution. Thereafter, a random traject
    will be replaced by a new random traject. Each improvement will be used for the
    next iteration.
    """
    def __init__(self, graph, rounds, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
        self.graph = graph
        self.trajects = self.get_solution(iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
        self.quality = calculate_quality(self.trajects, self.graph, MAX_AMOUNT_TRAJECTS)
        self.get_best_traject = self.run(rounds, MAX_TIME, MAX_AMOUNT_TRAJECTS, verbose=True)


    def get_solution(self, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
        """
        Gets a random solution from the randomise.py algorithm.
        """
        result, trajects = get_first_option(self.graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
        return trajects

    def mutate_traject(self, MAX_TIME):
        """
        Creates a random traject.
        """
        all_connections = copy.deepcopy(self.graph.all_stations)
        traject = []
        total_time = 0
        station = random.choices(list(all_connections.keys()), k=1)[0]
        traject.append(station)
        while total_time < MAX_TIME:
            if len(list(all_connections[station].time.keys())) > 0:
                next_station = random.choices(list(all_connections[station].time.keys()), k=1)[0]
            else:
                break

            if (total_time + all_connections[station].time[next_station]) <= MAX_TIME:
                traject.append(next_station)
                total_time += all_connections[station].time[next_station]
                all_connections[station].time.pop(next_station)
                all_connections[next_station].time.pop(station)
                station = next_station
            else:
                break
        return traject

    def mutate_solution(self, trajects,  MAX_TIME):
        """
        Changes a random traject from the solution with a created random traject.
        """
        check_trajects = copy.deepcopy(trajects)
        # Remove random traject from solution
        check_trajects.pop(random.randrange(len(check_trajects)))
        new_traject = self.mutate_traject(MAX_TIME)
        check_trajects.append(new_traject)
        return check_trajects


    def check_solution(self, check_trajects, MAX_AMOUNT_TRAJECTS):
        """
        Checks the solution and remembers and accepts the solution, if better.
        """
        new_quality = calculate_quality(check_trajects, self.graph, MAX_AMOUNT_TRAJECTS)
        old_quality = self.quality

        # If K value improves, replace previous solution
        if new_quality >= old_quality:
            self.trajects = check_trajects
            self.quality = new_quality
            print(new_quality)

    def run(self, iterations, MAX_TIME, MAX_AMOUNT_TRAJECTS, verbose=False):
        """
        Runs the hillclimber for a chosen amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            print(f'Iteration {iteration}/{iterations}, current value: {self.quality}') if verbose else None

            new_trajects = copy.deepcopy(self.trajects)

            # Creates new solution by replacing one traject
            check_trajects = self.mutate_solution(new_trajects, MAX_TIME)

            # Accepts solution it if it is better
            self.check_solution(check_trajects, MAX_AMOUNT_TRAJECTS)

            # When the code is only run 1 time create a visualisation
            if iteration == 1:
                visualisation(self.graph, self.trajects, 'Hillclimber.png')

        return self.quality