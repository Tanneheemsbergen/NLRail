import copy
import random
from functions.calculation import values
from visualisation import visualisation

def greedy_time(graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME):
    all_connections = graph.all_stations
    # check_connections_left = copy.deepcopy(all_connections)
    trajects = []
    total_time_traject = 0
    copy_connections = copy.deepcopy(all_connections)

    for _ in range(MAX_AMOUNT_TRAJECTS):
      
        traject = []
        total_time = 0
        station = random.choices(list(copy_connections.keys()), k=1)[0]
        traject.append(station)
        while total_time < MAX_TIME:

            if len(list(copy_connections[station].time.keys())) > 0:
                next_station = min(copy_connections[station].time, key=copy_connections[station].time.get)
            else:
                break

            if total_time + int(copy_connections[station].time[next_station]) <= MAX_TIME:
                traject.append(next_station)
                total_time += int(copy_connections[station].time[next_station])

                copy_connections[station].time.pop(next_station)
                copy_connections[next_station].time.pop(station)

                # if next_station in list(check_connections_left[station].time.keys()):
                #     check_connections_left[station].time.pop(next_station)
                        
                # if station in list(check_connections_left[next_station].time.keys()):
                #     check_connections_left[next_station].time.pop(station)
                       
                station = next_station
            else:
                break
           
        trajects.append(traject)
        total_time_traject += total_time


    quality = values(all_connections, copy_connections, total_time_traject, MAX_AMOUNT_TRAJECTS)

    if iteration == 1:
        visualisation(graph, trajects, 'greedy_time_visualisation.png')


    return quality