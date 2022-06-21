from functions.heuristics.random_with_classes import random_function_classes
from visualisation import visualisation, normal_distribution, histogram
#from functions.normal_distribution import barplot
from functions.classes.graph_class import Graph
from functions.heuristics.greedy_time import greedy_time
from functions.heuristics.depth_first import depthfirst
from functions.heuristics.hillclimber_class import Hillclimber
import argparse

def main (input_file_name, algorithm, iteration):

    # Open de input document and create an empty list for connections
    stations_input = f"csvfiles/Stations{input_file_name}.csv"
    connections_input = f"csvfiles/Connecties{input_file_name}.csv"
    station_graph = Graph(stations_input, connections_input)

    # Determine the maximum amount of trajects and time, based on the user input
    if input_file_name == "Holland":
        MAX_AMOUNT_TRAJECTS = 7
        MAX_TIME = 120
    elif input_file_name == "Nationaal":
        MAX_AMOUNT_TRAJECTS = 20
        MAX_TIME = 180

    results = []
    # Determine which algorithm to use based on the user input
    for i in range(iteration):
        print(i)
        if algorithm == "r":
            result = random_function_classes(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
        elif algorithm == "g":
            result = greedy_time(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
        elif algorithm == "h":
            result = Hillclimber()
            results.append(result)


    if iteration > 1:
        histogram(results)
    # depthfirst(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME)
    # print(f" greedy: {greedy_time(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME)}")
    # print(f" random: {random_function_classes(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME)}")
    # results = []
    # # Determine which algorithm to use based on the user input
    # for i in range(iteration):
    #     print(i)
    #     if algorithm == "r":
    #         result = random_function_classes(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME)
    #         results.append(result)

    #     # elif algorithm == "g":
    #     #     greedy_function(all_connections, MAX_AMOUNT_TRAJECTS, MAX_TIME)
    # if iteration > 1:
    #     barplot(results)

if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "run algorithm")

    # Adding arguments
    parser.add_argument("Area", choices=["Holland", "Nationaal"], help="Connections in North - and South-Holland, or the entire Netherlands")
    parser.add_argument("Heuristics", choices=["r", "g", "h"], help="1: Random, 2: Greedy, 3: Hillclimber")
    parser.add_argument("Iterations", type=int, default=1000, help="The amount of iterations which the programm will be run, default is 1000")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.Area, args.Heuristics, args.Iterations)
