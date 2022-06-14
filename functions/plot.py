# import matplotlib.pyplot as plt
# import pandas as pd
# from functions.classes.graph_class import Graph

# def plotting(stations_input, connection_input):
#     stations = Graph(stations_input).all_stations
#     print("stations")
#     print(stations)
#     connections = connection_input
#     #print("con")
#     #print(connections)

# # for i in range(len(stations)):
# #     for j in range(len(connections)):
# #         if i["station"] == j["station1"]:
# #             print(i)
# #             print(j["x"])

#     #print(stations["x"][0])
#     plt.xlabel("X-Coordinate")
#     plt.ylabel("Y-Coordinate")
#     plt.xticks(rotation=90)

#     # #plt.scatter(stations.all_stations["x"], stations.all_stations["y"] )
#     # for i in range(len(connections) -1):
#     #     # For connectie in connecties
#     #     # kijk de 
#     #     x_values = [stations.all_stations[i].xcoordinate, stations.all_stations[i+1].xcoordinate]
#     #     y_values = [stations.all_stations[i].ycoordinate, stations.all_stations[i + 1].ycoordinate]
#     #     #plt.plot(x_values, y_values)
#     #     plt.plot((connections["station1"][x_values]), (connections["station1"][y_values]))
#     #     # connections["station1"][int(stations.all_stations[i + 1].xcoordinate)]],
#     #     # # [connections["station2"][int(stations.all_stations[i].ycoordinate)], connections["station2"][int(stations.all_stations[i + 1].ycoordinate)]])


# # from functions.classes.graph_class import Graph
# # test_graph = Graph("csvfiles/StationsHolland.csv")
# # x = []
# # y = []
# # for station in test_graph.all_stations:
# #     x.append(test_graph.all_stations[station].xcoordinate)
# #     y.append(test_graph.all_stations[station].ycoordinate)

# # new_x, new_y = zip(*sorted(zip(x, y)))


#     plt.savefig("test2.png")
#     #return "test2.png"

import matplotlib.pyplot as plt

from functions.classes.graph_class import Graph
def plotting(stations_input, connection_input):
    test_graph = Graph("csvfiles/StationsHolland.csv")


    # plt.plot([stations["x"][0],stations["x"][1]], [stations["y"][0], stations["y"][1]])

    plt.rcParams["figure.figsize"] = [10, 10]
    plt.rcParams["figure.autolayout"] = True

    x = []
    y = []
    name_stations = []
    for station in test_graph.all_stations:
        x.append(float(test_graph.all_stations[station].xcoordinate))
        y.append(float(test_graph.all_stations[station].ycoordinate))
        name_stations.append(test_graph.all_stations[station].name)
    print(y)

    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.plot(x, y, 'r*')
    plt.axis([51, 54, 4, 5])

    for x, y, s in zip(x, y, name_stations):
        plt.text(x, y, s)

    # plt.plot([x[0],y[]],[])
    plt.savefig("testplotnew.png")