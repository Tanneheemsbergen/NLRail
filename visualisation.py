import matplotlib.pyplot as plt

from functions.classes.graph_class import Graph
test_graph = Graph("csvfiles/StationsHolland.csv")

plt.rcParams["figure.figsize"] = [20, 20]
plt.rcParams["figure.autolayout"] = True

x = []
y = []
name_stations = []
for station in test_graph.all_stations:
    x.append(float(test_graph.all_stations[station].xcoordinate))
    y.append(float(test_graph.all_stations[station].ycoordinate))
    name_stations.append(test_graph.all_stations[station].name)

plt.xlabel("y-Coordinate")
plt.ylabel("X-Coordinate")

plt.plot(y, x, 'r*')

for name in name_stations:
    connections = list(test_graph.all_stations[name].time.keys())
    index_first_station = name_stations.index(name)
    for connection in connections:
        index_destination = name_stations.index(connection)
        plt.plot([y[index_first_station], y[index_destination]],[x[index_first_station], x[index_destination]], 'b')

plt.axis([4.2, 5.2, 51.2, 53.2])

for y, x, s in zip(y, x, name_stations):
    plt.text(y, x, s)


plt.savefig("testplotnew.png")