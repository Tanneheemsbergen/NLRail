import random
import copy
import csv
from functions.calculation import values
from visualisation import visualisation

def random_function_classes(graph, MAX_AMOUNT_TRAJECTS, MAX_TIME):
    all_connections = graph.all_stations
    check_connections_left = copy.deepcopy(all_connections)
    trajects = []
    total_time_traject = 0

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
    
    quality = values(all_connections, check_connections_left, total_time_traject, MAX_AMOUNT_TRAJECTS)

    with open('output.csv', 'w') as file:
        writer = csv.writer(file)
        header = ['train', 'stations']
        writer.writerow(header)
        i = 1
        for traject in trajects:
            data = [f"train_{i}", ('[%s]' % ', '.join(map(str, traject)))]
            i += 1
            writer.writerow(data)
        writer.writerow(['score', quality])

    #visualisation(graph, trajects, 'random_visualisation.png')
    return quality