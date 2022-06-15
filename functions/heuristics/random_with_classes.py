import random
import copy
from functions.calculation import calculate_quality
<<<<<<< HEAD
from functions.plot import plot_function
def random_function_classes(graph, MAX_AMOUNT_TRAJECTS, MAX_TIME):

=======
<<<<<<< HEAD


=======
from visualisation import visualisation
>>>>>>> 47c0623a0c522c32d9fffed8b13197ce8ccd3dc4
def random_function_classes(graph, MAX_AMOUNT_TRAJECTS, MAX_TIME):
>>>>>>> 29630d8350960495e66a12e1f114df0ad02eb9cf
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
            print(f"begin station {station}")
            if len(list(copy_connections[station].time.keys())) > 0:
                next_station = random.choices(list(copy_connections[station].time.keys()), k=1)[0]
            else:
                break
            print(f'next station {next_station}')
            total_time += int(copy_connections[station].time[next_station])
            if total_time + int(copy_connections[station].time[next_station]) <= MAX_TIME:
                traject.append(next_station)

<<<<<<< HEAD
                # print(f" time: {copy_connections[station].time}")
                # print(f" time: {copy_connections[station].time[next_station]}")
                # print(f"connecties before pop: {copy_connections[station].time.keys()}")
=======
>>>>>>> 29630d8350960495e66a12e1f114df0ad02eb9cf
                copy_connections[station].time.pop(next_station)
                copy_connections[next_station].time.pop(station)
<<<<<<< HEAD
                # print(f"netx connecties after pop: {copy_connections[next_station].time.keys()}")


=======
    
>>>>>>> 29630d8350960495e66a12e1f114df0ad02eb9cf
                if next_station in list(check_connections_left[station].time.keys()):
                    check_connections_left[station].time.pop(next_station)
                        
                if station in list(check_connections_left[next_station].time.keys()):
                    check_connections_left[next_station].time.pop(station)
                       
                station = next_station
           
        trajects.append(traject)
        total_time_traject += total_time

    total_connections = 0
    for i in all_connections:
        total_connections += len(all_connections[i].time)

    total_connections = total_connections / 2

    connections_left = 0

    for i in check_connections_left:
        connections_left += len(check_connections_left[i].time)
<<<<<<< HEAD
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
=======

    connections_left = connections_left / 2

    amount_of_connections = total_connections - connections_left
    quality = calculate_quality(amount_of_connections, total_connections, total_time_traject, MAX_AMOUNT_TRAJECTS)
  
    visualisation(graph, trajects, 'random_visualisation.png')
    return quality
>>>>>>> 47c0623a0c522c32d9fffed8b13197ce8ccd3dc4
