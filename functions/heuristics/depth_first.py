from cmath import inf
import random
import copy
import csv
from functions.calculation import calculate_quality
from visualisation import visualisation

def depthfirst(graph, MAX_AMOUNT_TRAJECTS, MAX_TIME):
    all_connections = graph.all_stations
    check_connections_left = copy.deepcopy(all_connections)
    trajects = []
    total_time_traject = 0
    
    for _ in range(MAX_AMOUNT_TRAJECTS):
        copy_connections = copy.deepcopy(all_connections)
        
        total_time = 0
        station = random.choices(list(all_connections.keys()), k=1)[0]
        # station = 'Den Helder'
        traject = [station]
        states = list(copy_connections[station].time.keys())
    
        # print(station)
        # print(states)
        while states and len(list(copy_connections[station].time.keys())) > 0:
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

        print(f'eind traject {traject}')
        trajects.append(traject)
                # or ontinue looking for better graph
                # check_solution(new_graph)

            # Update the input graph with the best result found.
            # self.graph = self.best_solution


    print(trajects)
    print(check_connections_left)

    total_connections = 0
    for i in all_connections:
        total_connections += len(all_connections[i].time)

    total_connections = total_connections / 2

    connections_left = 0
    for i in check_connections_left:
        connections_left += len(check_connections_left[i].time)

    connections_left = connections_left / 2

    amount_of_connections = total_connections - connections_left
    quality = calculate_quality(amount_of_connections, total_connections, total_time_traject, MAX_AMOUNT_TRAJECTS)
    print(quality)
# class DepthFirst:
#     """
#     A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
#     """
#     def __init__(self, graph, transmitters):
#         self.graph = copy.deepcopy(graph)
#         self.transmitters = transmitters

#         self.states = [copy.deepcopy(self.graph)]

#         self.best_solution = None
#         self.best_value = float('inf')

#     def get_next_state(self):
#         """
#         Method that gets the next state from the list of states.
#         """
#         return self.states.pop()

#     def build_children(self, graph, node):
#         """
#         Creates all possible child-states and adds them to the list of states.
#         """
#         # Retrieve all valid possible values for the node.
#         values = node.get_possibilities(self.transmitters)

#         # Add an instance of the graph to the stack, with each unique value assigned to the node.
#         for value in values:
#             new_graph = copy.deepcopy(graph)
#             new_graph.nodes[node.id].value = value
#             self.states.append(new_graph)

#     def check_solution(self, new_graph):
#         """
#         Checks and accepts better solutions than the current solution.
#         """
#         new_value = new_graph.calculate_value()
#         old_value = self.best_value

#         # We are looking for maps that cost less!
#         if new_value <= old_value:
#             self.best_solution = new_graph
#             self.best_value = new_value
#             print(f"New best value: {self.best_value}")

#     def run(self):
#         """
#         Runs the algorithm untill all possible states are visited.
#         """
#         while self.states:
#             new_graph = self.get_next_state()

#             # Retrieve the next empty node.
#             node = new_graph.get_empty_node()

#             if node is not None:
#                 self.build_children(new_graph, node)
#             else:
#                 # Stop if we find a solution
#                 # break

#                 # or ontinue looking for better graph
#                 self.check_solution(new_graph)

#         # Update the input graph with the best result found.
#         self.graph = self.best_solution