import random
import copy
from functions.calculation import calculate_quality, values
from visualisation import visualisation
from functions.heuristics.random_with_classes import random_function_classes

class Hillclimber:

    def __init__(self, graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
        # self.value = self.run
        self.trajects = self.get_solution(graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
        self.quality = values(all_connections, check_connections_left, total_time_traject, MAX_AMOUNT_TRAJECTS)

    def get_solution(self, graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
        result, trajects = random_function_classes(graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
        return trajects

    def mutate_traject(self):

        traject = []
        station = random.choices(list(all_connections.keys()), k=1)[0]
        traject.append(station)
        while total_time < MAX_TIME:

            if len(list(copy_connections[station].time.keys())) > 0:
                next_station = random.choices(list(copy_connections[station].time.keys()), k=1)[0]
            else:
                break

            if (total_time + copy_connections[station].time[next_station]) <= MAX_TIME:
                traject.append(next_station)
                total_time += copy_connections[station].time[next_station]
                copy_connections[station].time.pop(next_station)
                copy_connections[next_station].time.pop(station)
                if next_station in list(check_connections_left[station].time.keys()):
                    check_connections_left[station].time.pop(next_station)
                if station in list(check_connections_left[next_station].time.keys()):
                    check_connections_left[next_station].time.pop(station)

                station = next_station
            else:
                break
            total_time_traject += total_time

        return traject

    def mutate_solution(trajects):
        trajects.pop(random.randrange(len(trajects)))

        new_traject = self.mutate_traject()

        trajects.append(new_traject)
        # for _ in range(trajects):
        #     self.mutate_traject(new_trajects)

    def check_solution(self, new_traject):

        new_quality = values(all_connections, check_connections_left, total_time_traject, MAX_AMOUNT_TRAJECTS)
        old_quality = self.quality

        if new_quality <= old_quality:
            self.trajects = new_trajects
            self.quality = new_quality

    def run(self, iterations, verbose=False):

        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.quality}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_trajects = copy.deepcopy(self.trajects)

            self.mutate_solution(new_trajects)

            # Accept it if it is better
            self.check_solution(new_trajects)
