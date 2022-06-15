import matplotlib.pyplot as plt
import pandas as pd
from functions.classes.station_class import Station
import matplotlib.pyplot as plt
import pandas as pd
import itertools
from functions.classes.graph_class import Graph

def plotting(stations_input, connection_input):
    test_graph = Graph("csvfiles/StationsHolland.csv")
    x_coordinates = []
    y_coordinates = []
    for station in test_graph.all_stations:
        for connection in test_graph.all_stations[station].time:
            x_coordinates.append(test_graph.all_stations[station].xcoordinate)
            y_coordinates.append(test_graph.all_stations[station].ycoordinate)
    # print(x_coordinates)
    new_x, new_y = zip(*sorted(zip(x_coordinates, y_coordinates)))

    # stations = pd.read_csv("csvfiles/StationsHolland.csv")
    # print(stations["x"][0])
    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.figure(figsize=(15,15))
    plt.xticks(rotation=90)
    plt.scatter(new_x, new_y)
    # plt.plot([stations["x"][0],stations["x"][1]], [stations["y"][0], stations["y"][1]])
    plt.plot(x_coordinates, y_coordinates)
    plt.savefig("testplotnew.png")
# def plotting(stations_input, connection_input):
#     stations = pd.read_csv(stations_input)
#     print("stations")
#     print(stations)
#     connections = pd.read_csv(connection_input)
#     print("con")
#     print(connections)

# for i in range(len(stations)):
#     for j in range(len(connections)):
#         if i["station"] == j["station1"]:
#             print(i)
#             print(j["x"])

    # print(stations["x"][0])
    # plt.xlabel("X-Coordinate")
    # plt.ylabel("Y-Coordinate")
    # plt.xticks(rotation=90)
    # plt.scatter(stations["x"], stations["y"])
    # x_coordinates = []
    # y_coordinates = []

    # for station in stations:
    #     for connection in connections:
    #         x_coordinates.append(station)
    #         y_coordinates.append(station)
    #     plt.plot(x_coordinates, y_coordinates)
    # # for i in range(len(connections) -1):
    # #     plt.plot([connections["station1"][i],connections["station1"][i+1]], [connections["station2"][i], connections["station2"][i+1]])
    #
    # plt.savefig("test3.png")
    # return "test3.png"
