import random
import copy
from functions.helpers.check50 import check50
from functions.helpers.calculation import calculate_quality
from functions.helpers.visualisation import visualisation


def random_function(graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
    """
    The random algorithm takes a random start station and from there make random
    connections to create a traject. Every step is completely random.
    """
    all_connections = graph.all_stations
    check_connections_left = copy.deepcopy(all_connections)
    trajects = []

    for i in range(MAX_AMOUNT_TRAJECTS):
        copy_connections = copy.deepcopy(all_connections)
        traject = []
        total_time = 0
        station = random.choices(list(all_connections.keys()), k=1)[0]
        traject.append(station)
        while total_time < MAX_TIME:
            if len(list(copy_connections[station].time.keys())) > 0:
                # Takes a random station from list and makes connection
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
        trajects.append(traject)
    # Only make a visualisation if the algorithm runs once to prevent confusing plots
    if iteration == 1:
        visualisation(graph, trajects, 'Random.png')

    quality = calculate_quality(trajects, graph, MAX_AMOUNT_TRAJECTS)

    check50(trajects, quality)
    return quality, trajects
