from functions.heuristics.random_alg import random_function
#from classes.graph_class import Graph
import argparse
#from functions.visualisation import visualisation

def main (input_file_name, algorithm):  
    # Open de input document and create an empty list for connections
    input_file = f"csvfiles/{input_file_name}.csv"
    with open(input_file) as f:
        connecties = f.readlines()
    all_connections = []

    # Fill the connections list with all connections
    for line in connecties[1:]:
        connection = []
        for i in line.strip().split(','):
            connection.append(i)
        all_connections.append(connection)

    # Determine the maximum amount of trajects and time, based on the user input
    if input_file_name == "ConnectiesHolland":
        MAX_AMOUNT_TRAJECTS = 7
        MAX_TIME = 120
    elif input_file_name == "ConnectiesNationaal":
        MAX_AMOUNT_TRAJECTS = 20
        MAX_TIME = 180

    # Determine which algorithm to use based on the user input
    if algorithm == "r":
        random_function(all_connections, MAX_AMOUNT_TRAJECTS, MAX_TIME)
    elif algorithm == "g":
        greedy_function(all_connections, MAX_AMOUNT_TRAJECTS, MAX_TIME)
    # elif algorithm = "":

    # Visualization
    #Graph("csvfiles/ConnectiesHolland.csv")
    #visualisation(traject, all_stations)
    # from classes.graph_class import Graph
    # test_graph = Graph("csvfiles/StationsHolland.csv")
    # print(random_function_classes(test_graph, 7, 120))

if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "run algorithm")

    # Adding arguments
    parser.add_argument("Area", choices=["ConnectiesHolland", "ConnectiesNationaal"], help="1: Connections in North - and South-Holland, 2: The entire Netherlands")
    parser.add_argument("Heuristics", choices=["r", "g"], help="1: Random, 2: Greedy")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.Area, args.Heuristics)
