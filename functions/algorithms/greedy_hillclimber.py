import random
import copy
from functions.algorithms.hillclimber import Hillclimber
from functions.algorithms.greedy_time import greedy_time


class GreedyHillclimber(Hillclimber):
    """
    The GreedyHillClimber class first creates a solution using the greedy algorithm.
    Thereafter, a random traject will be replaced by a new greedytraject. Each
    improvement will be used for the next iteration.
    """
    def __init__(self, graph, rounds, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
        
        # Use the init of the Hillclimber class
        super().__init__(graph, rounds, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)


    def get_solution(self, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
        """
        Gets a greedy solution from the greedy_time algorithm.
        """
        result, trajects = greedy_time(self.graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
        return trajects


    def mutate_traject(self, MAX_TIME):
        """
        Creates a greedy traject.
        """
        all_connections = copy.deepcopy(self.graph.all_stations)
        traject = []
        total_time = 0
        station = random.choices(list(all_connections.keys()), k=1)[0]
        traject.append(station)
        while total_time < MAX_TIME:
            if len(list(all_connections[station].time.keys())) > 0:

                # Gets station with the least amount of time and make connection
                next_station = min(all_connections[station].time, key=all_connections[station].time.get)
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
<<<<<<< HEAD

    def mutate_solution(self, trajects,  MAX_TIME):
        """
        Changes a random traject from the solution with a created greedy traject.
        """
        check_trajects = copy.deepcopy(trajects)
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

        if new_quality >= old_quality:
            self.trajects = check_trajects
            self.quality = new_quality


    def run(self, iterations, MAX_TIME, MAX_AMOUNT_TRAJECTS, verbose=False):
        """
        Runs the hillclimber for a chosen amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            #print(f'Iteration {iteration}/{iterations}, current value: {self.quality}') if verbose else None

            new_trajects = copy.deepcopy(self.trajects)
            # Creates new solution by replacing one traject
            check_trajects = self.mutate_solution(new_trajects, MAX_TIME)

            # Accepts solution it if it is better
            self.check_solution(check_trajects, MAX_AMOUNT_TRAJECTS)

            # When the code is only run 1 time create a visualisation
            if iteration == 1:
                visualisation(self.graph, self.trajects, 'Greedy_hillclimber.png')

        return(self.quality)
=======
>>>>>>> 469b19d74239a85cf54c725d4ac20b0fb4335f8f
