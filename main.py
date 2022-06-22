from functions.heuristics.random_with_classes import random_function_classes
from visualisation import histogram
from functions.classes.graph_class import Graph
from functions.heuristics.greedy_time import greedy_time
from functions.heuristics.depth_first import depthfirst
from functions.heuristics.hillclimber_class import Hillclimber
from functions.calculation import calculate_quality, values
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
            result, trajects = random_function_classes(station_graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
            print(result)
        elif algorithm == "g":
            result = greedy_time(station_graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
        elif algorithm == "df":
            result = depthfirst(station_graph, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
        elif algorithm == "hc":
            hc = Hillclimber(station_graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            hc.run(250, verbose=True)
            print(hc.trajects)

    if iteration > 1:
        histogram(results)


if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "run algorithm")

    # Adding arguments
    parser.add_argument("Area", choices=["Holland", "Nationaal"], help="Connections in North - and South-Holland, or the entire Netherlands")
    parser.add_argument("Heuristics", choices=["r", "g", "df", "hc"], help="r: Random, g: Greedy, df: Depth-first")
    parser.add_argument("Iterations", type=int, default=1000, help="The amount of iterations which the programm will be run, default is 1000")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.Area, args.Heuristics, args.Iterations)
