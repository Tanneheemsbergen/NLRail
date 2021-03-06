import copy
import random
from functions.helpers.calculation import calculate_quality
from functions.helpers.visualisation import visualisation


def greedy_time(graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
    """
    The Greedy algorithm first takes a random start station and afterwards creates
    a random solution using greedy trajects. This step will be repeated for 7 or
    20 times, respectively Holland and Nationaal.
    """
    all_connections = graph.all_stations
    trajects = []
    copy_connections = copy.deepcopy(all_connections)

    for _ in range(MAX_AMOUNT_TRAJECTS):
        traject = []
        total_time = 0
        station = random.choices(list(copy_connections.keys()), k=1)[0]
        traject.append(station)
        while total_time < MAX_TIME:
            if len(list(copy_connections[station].time.keys())) > 0:
                # Gets station with the least amount of time and make connection
                next_station = min(copy_connections[station].time, key=copy_connections[station].time.get)
            else:
                break
            if total_time + int(copy_connections[station].time[next_station]) <= MAX_TIME:
                traject.append(next_station)
                total_time += int(copy_connections[station].time[next_station])
                copy_connections[station].time.pop(next_station)
                copy_connections[next_station].time.pop(station)
                station = next_station
            else:
                break
        trajects.append(traject)

    quality = calculate_quality(trajects, graph, MAX_AMOUNT_TRAJECTS)

    # Only make a visualisation if the algorithm runs once to prevent confusing plots
    if iteration == 1:
        visualisation(graph, trajects, 'greedy_time_visualisation_h.png')

    return quality, trajects
