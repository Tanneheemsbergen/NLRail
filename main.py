from functions.heuristics.random_alg import random_function
from functions.heuristics.greedy import greedy_function

# from functions.visualisation import visualisation
with open("csvfiles/ConnectiesHolland.csv") as f:
    connecties = f.readlines()
all_connections = []

for line in connecties[1:]:
    connection = []
    for i in line.strip().split(','):
        connection.append(i)
    all_connections.append(connection)
MAX_AMOUNT_TRAJECTS = 7
MAX_TIME = 120
greedy_function(all_connections, MAX_AMOUNT_TRAJECTS, MAX_TIME)
#visualisation(traject, all_stations)

# if __name__ == "__main__":
#     # Set-up parsing command line arguments
#     parser = argparse.ArgumentParser(description = "run algorithm")
#
#     # Adding arguments
#     parser.add_argument("area", type=int, choices=[1, 2], help="1: North/South-Holand, 2: Holland")
#     parser.add_argument("heuristics", type=int, choices=[1, 2],, help="1: random, 2: greedy")
#
#     # Read arguments from command line
#     args = parser.parse_args()
#
#     # Run main with provide arguments
#
