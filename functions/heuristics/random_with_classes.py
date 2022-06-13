"""
Een copy maken werkt volgensmij nog niet daarom kan het nog niet verwijderd worden uit de lijsten dus hij checkt nu niet
of een verbinding al gebruikt is
"""
import random
from functions.calculation import calculate_quality
def random_function_classes(graph, MAX_AMOUNT_TRAJECTS, MAX_TIME):
    all_connections = graph.all_stations
    check_connections_left = all_connections.copy()
    trajects = []
    total_time_traject = 0

    for i in range(MAX_AMOUNT_TRAJECTS):
        copy_connections = all_connections.copy()
        traject = []
        total_time = 0
        station = random.choices(list(all_connections.keys()), k=1)[0]
        traject.append(station)

        while total_time < MAX_TIME:
            next_station = random.choices(copy_connections[station].connections, k=1)[0]
            traject.append(next_station)
            total_time += int(copy_connections[station].time[next_station])
 
            # copy_connections[station].time.pop(next_station)
            # copy_connections[next_station].time.pop(station)
            
            # if next_station in check_connections_left[station]:
            #     check_connections_left[station].time.pop(next_station)
            # if station in check_connections_left[next_station]:
            #     check_connections_left[next_station].time.pop(station)
 
        total_time_traject += total_time
        trajects.append(traject)

    # for i in check_connections_left:
    #     if check_connections_left[i] == []:
    #         del check_connections_left[i]

    return trajects
