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
