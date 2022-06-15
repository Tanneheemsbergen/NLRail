import random
import copy
from functions.calculation import calculate_quality


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
            # print(f"begin station {station}")
            if len(list(copy_connections[station].time.keys())) > 0:
                next_station = random.choices(list(copy_connections[station].time.keys()), k=1)[0]
            else:
                break
            # print(f'next station {next_station}')
            total_time += int(copy_connections[station].time[next_station])
            if total_time + int(copy_connections[station].time[next_station]) <= MAX_TIME:
                traject.append(next_station)
            
                # print(f" time: {copy_connections[station].time}")
                # print(f" time: {copy_connections[station].time[next_station]}")
                # print(f"connecties before pop: {copy_connections[station].time.keys()}")
                copy_connections[station].time.pop(next_station)
                # print(f"connecties after pop: {copy_connections[station].time.keys()}")
                # print(f"next connecties before pop: {copy_connections[next_station].time.keys()}")
                copy_connections[next_station].time.pop(station)
                # print(f"netx connecties after pop: {copy_connections[next_station].time.keys()}")
    
         
                if next_station in list(check_connections_left[station].time.keys()):
                    check_connections_left[station].time.pop(next_station)
                if station in list(check_connections_left[next_station].time.keys()):
                    check_connections_left[next_station].time.pop(station)
            station = next_station
        trajects.append(traject)
        total_time_traject += total_time

    connections_left = 0
    for i in check_connections_left:
        connections_left += len(check_connections_left[i].time)
    print(f"Connections left:{connections_left}")
    print(len(all_connections))
   # print(connections_left)
    #print(f"connections: {len(all_connections)}")
    result = calculate_quality((28 - (connections_left/2)), 28, total_time_traject, MAX_AMOUNT_TRAJECTS)
    if result < -500:
        breakpoint()
    # resultt = dat hierboven
    # Connections_left is voor 7 trajecten 
    return result 
