
from functions.heuristics.random_with_classes import random_function_classes
from visualisation import visualisation, barplot
#from functions.normal_distribution import barplot
from functions.classes.graph_class import Graph
from functions.heuristics.greedy_time import greedy_time
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
    
    print(greedy_time(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME))
    results = []
    # Determine which algorithm to use based on the user input
    for i in range(iteration):
        print(i)
        if algorithm == "r":
            result = random_function_classes(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
     
        # elif algorithm == "g":
        #     greedy_function(all_connections, MAX_AMOUNT_TRAJECTS, MAX_TIME)
    if iteration > 1:
        barplot(results)

if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "run algorithm")

    # Adding arguments
    parser.add_argument("Area", choices=["Holland", "Nationaal"], help="Connections in North - and South-Holland, or the entire Netherlands")
    parser.add_argument("Heuristics", choices=["r", "g"], help="1: Random, 2: Greedy")
    parser.add_argument("Iterations", type=int, default=1000, help="The amount of iterations which the programm will be run, default is 1000")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.Area, args.Heuristics, args.Iterations)

