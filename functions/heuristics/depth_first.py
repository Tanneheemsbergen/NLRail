from cmath import inf
import random
import copy
import csv
from functions.calculation import calculate_quality
from visualisation import visualisation

def depthfirst(graph, MAX_AMOUNT_TRAJECTS, MAX_TIME):
    value = -float('inf')
    all_connections = graph.all_stations
    check_connections_left = copy.deepcopy(all_connections)
    trajects = []
    total_time_traject = 0
    copy_connections = copy.deepcopy(all_connections)

    for _ in range(MAX_AMOUNT_TRAJECTS):
         
        total_time = 0
        station = random.choices(list(copy_connections.keys()), k=1)[0]

        check = 0
        for i in copy_connections:
            check += len(copy_connections[i].time)

        if check == 0:
            station = ' '
        else:
            while len(list(copy_connections[station].time.keys())) == 0:
                station = random.choices(list(copy_connections.keys()), k=1)[0]
                          
        
        traject = [station]
        if station != ' ':
            states = list(copy_connections[station].time.keys())
    
        while states and len(list(copy_connections[station].time.keys())) > 0 and station != 0:
            # print(f'traject: {traject}')

            next_state = states.pop()
            traject.append(next_state)
            
            # print(f'next_state: {next_state}')
            # print(f"added to traject {traject}")
            # print("hoeveelheid kinderen")
            # print(len(list(copy_connections[next_state].time.keys())))
            # print(station)
            # print(next_state)
            # print(copy_connections[next_state].time)
            # print(copy_connections[next_state].time[station])
            # print(f"time {total_time_traject + copy_connections[next_state].time[station]}")
            if len(list(copy_connections[next_state].time.keys())) > 0 and (total_time + copy_connections[next_state].time[station]) <= MAX_TIME:
                total_time_traject += copy_connections[next_state].time[station]
                total_time += copy_connections[next_state].time[station]
                # print(f'from {station} to {next_state}')
                # print(f'options connections before pop: {list(copy_connections[next_state].time.keys())}')
                copy_connections[station].time.pop(next_state)
                copy_connections[next_state].time.pop(station)
                if next_state in list(check_connections_left[station].time.keys()):
                    check_connections_left[station].time.pop(next_state)
                        
                if station in list(check_connections_left[next_state].time.keys()):
                    check_connections_left[next_state].time.pop(station)
                # print(f'options connections after pop: {list(copy_connections[next_state].time.keys())}')

                children = list(copy_connections[next_state].time.keys())
                for child in children:
                    states.append(child)

                # print(f'states: {states}')
                # print(f'total time: {total_time_traject}')
                station = next_state
                
            else:
                
                # Stop if we find a solution
                break

        #print(f'eind traject {traject}')
        trajects.append(traject)
                # or ontinue looking for better graph
                # check_solution(new_graph)

            # Update the input graph with the best result found.
            # self.graph = self.best_solution

    quality = calculate_quality(trajects, graph, MAX_AMOUNT_TRAJECTS)

    print(trajects)
    print(quality)

