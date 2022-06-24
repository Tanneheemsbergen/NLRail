from functions.algorithms.randomise import random_function
from functions.helpers.visualisation import histogram
from functions.classes.graph_class import Graph
from functions.algorithms.greedy_time import greedy_time
from functions.algorithms.get_first_option import get_first_option
from functions.algorithms.greedy_hillclimber import GreedyHillclimber
from functions.algorithms.hillclimber import Hillclimber
from functions.algorithms.depth_hillclimber import DepthFirstHillclimber
from functions.algorithms.simulating_anealing import SimulatedAnnealing
import argparse


def main(input_file_name, algorithm, iteration):

    # Opens input document and create an empty list for connections
    stations_input = f"csvfiles/Stations{input_file_name}.csv"
    connections_input = f"csvfiles/Connecties{input_file_name}.csv"
    station_graph = Graph(stations_input, connections_input)
    space = input_file_name
    algorithm = algorithm

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
            result, trajects = random_function(station_graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
            print(result)
        elif algorithm == "g":
            result, trajects = greedy_time(station_graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
        elif algorithm == "df":
            result, trajects = get_first_option(station_graph, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            results.append(result)
        elif algorithm == "hc":
            hc = Hillclimber(station_graph, 200000, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            hc.get_best_traject
        elif algorithm == "ghc":
            hc = GreedyHillclimber(station_graph, 20000, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            hc.get_best_traject
        elif algorithm == "dfhc":
            hc = DepthFirstHillclimber(station_graph, 60000, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)
            hc.get_best_traject
        elif algorithm == "sa":
            sa = SimulatedAnnealing(station_graph, 5000, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME, 3000)
            sa.get_best_traject
            

    # Creates a histogram When a algorithm is runs more than 1 time
    if iteration > 1:
        histogram(results, space, algorithm)


if __name__ == "__main__":

    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description="run algorithm")

    # Adding arguments
    parser.add_argument("Area", choices=["Holland", "Nationaal"], help="Connections in North - and South-Holland, or the entire Netherlands")
    parser.add_argument("algorithms", choices=["r", "g", "df", "hc", "ghc", "dfhc", "sa"], help="r: Random, g: Greedy, df: Depth-first, hc: Hill-Climber, ghc: Greedy hill-climber")
    parser.add_argument("Iterations", type=int, default=1000, help="The amount of iterations which the programm will be run, default is 1000")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.Area, args.algorithms, args.Iterations)
