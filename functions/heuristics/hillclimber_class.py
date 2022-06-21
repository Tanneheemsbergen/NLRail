import random
import copy
from functions.calculation import calculate_quality
from visualisation import visualisation

class Hillclimber:

    def __init__(self, graph):

        self.graph = graph

    def get_solution(self, graph, MAX_AMOUNT_TRAJECTS, MAX_TIME):

        all_connections = graph.all_stations
        check_connections_left = copy.deepcopy(all_connections)
        trajects = []
        total_time_traject = 0
        quality = 0
        for i in range(MAX_AMOUNT_TRAJECTS):
            copy_connections = copy.deepcopy(all_connections)
            traject = []
            total_time = 0
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
            trajects.append(traject)
            total_connections = 0
            for i in all_connections:
                total_connections += len(all_connections[i].time)

            total_connections = total_connections / 2

            connections_left = 0

            for i in check_connections_left:
                connections_left += len(check_connections_left[i].time)

            connections_left = connections_left / 2

            amount_of_connections = total_connections - connections_left
            total_time_traject += total_time
        self.trajects = copy.deepcopy(trajects)
        self.quality = calculate_quality(amount_of_connections, total_connections, total_time_traject, MAX_AMOUNT_TRAJECTS)

    def mutate_traject(self, new_trajects):

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
        new_traject = traject
        print(new_traject)

    def mutate_solution():
        for _ in range(trajects):
            self.mutate_traject(new_trajects)

    def check_solution(self, new_traject):

        new_quality = new_trajects.calculate_quality()
        old_quality = self.quality

        if new_quality <= old_quality:
            self.trajects = new_trajects
            self.quality = new_quality

    def run(self, iterations):

        self.iterations = iterations

        for iteration in range(iterations, verbose = False):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.value}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_trajects = copy.deepcopy(self.trajects)

            self.mutate_solution(new_trajects)

            # Accept it if it is better
            self.check_solution(new_trajects)

    # visualisation(graph, trajects, 'random_visualisation.png')

    # print(new_quality)
    # if new_quality >= quality and len(besttrajects) == 0:
    #      quality = new_quality
    #      besttraject = traject
    #      besttrajects.append(besttraject)
    # elif new_quality >= quality and len(besttrajects) != 0:
    #     besttrajects.remove(besttraject)
    #     quality = new_quality
    #     besttraject = traject
    #     besttrajects.append(besttraject)
    # elif new_quality < quality:
    #     trajects.remove(traject)
    #     new_quality = quality
    # return quality
        # elif new_quality >= quality and len(trajects) != 0:
        #     trajects.remove(traject)
        #     quality = new_quality
        #     besttraject = traject
        #     besttrajects.append(besttraject)
        #     if len(besttrajects) == 0:
        #         besttraject = traject
        #     elif len(besttrajects) != 0:
        #         besttrajects.remove(besttraject)
        #         besttrajects.append(besttraject)
    # print(besttrajects)
    # print(trajects)
    # print(f"total time of all trajects: {total_time_traject}")
    # print(f"connections not used {check_connections_left}")
    #
    # print(calculate_quality(connections_used, len(all_connections),total_time_traject,MAX_AMOUNT_TRAJECTS))
