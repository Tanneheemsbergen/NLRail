import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 
import statistics

from functions.classes.graph_class import Graph
def barplot(results):
    plt.rcParams["figure.figsize"] = [10, 10]
    plt.rcParams["figure.autolayout"] = True

    x_axis = sorted(results, reverse=True)
    print(f"ordered!{x_axis}")

    # Calculating mean and standard deviation
    mean = statistics.mean(x_axis)
    sd = statistics.stdev(x_axis)
    

    plt.figure(0)
    plt.xlabel("Probabilty Density")
    plt.ylabel("K-value")
    #plt.axis([2500, 10000, 0, 0.0005])
    plt.grid()
    #plt.text(, 0.007, "mean, sd")
    plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
    
    plt.savefig("NormalDistribution.png")

def visualisation(graph, trajects, filename):
    plt.rcParams["figure.figsize"] = [15, 20]
    plt.rcParams["figure.autolayout"] = True

    x = []
    y = []
    name_stations = []
    for station in graph.all_stations:
        x.append(float(graph.all_stations[station].xcoordinate))
        y.append(float(graph.all_stations[station].ycoordinate))
        name_stations.append(graph.all_stations[station].name)

    plt.xlabel("y-Coordinate")
    plt.ylabel("X-Coordinate")

    plt.figure(1)
    plt.plot(y, x, 'r*')
    plt.axis([4.2, 5.2, 51.2, 53.2])

    for name in name_stations:
        connections = list(graph.all_stations[name].time.keys())
        index_first_station = name_stations.index(name)
        for connection in connections:
            index_destination = name_stations.index(connection)
            plt.plot([y[index_first_station], y[index_destination]],[x[index_first_station], x[index_destination]], 'b', alpha=0.1)
    

    colors = ['g', 'r', 'c', 'm', 'y', 'k', 'w']
    
    i = 0 
    linewidth=10
    for traject in trajects:
        color = colors[i]
        for station in range(len(traject) - 1):
            index_first_station = name_stations.index(traject[station])
            index_next_station =  name_stations.index(traject[station + 1])
            plt.plot([y[index_first_station], y[index_next_station]],[x[index_first_station], x[index_next_station]], color,linewidth=linewidth, alpha=0.3)
        if i > 6:
            i = 0
        else:
            i += 1
        linewidth -= 2

    for y, x, s in zip(y, x, name_stations):
        plt.text(y, x, s)

    plt.savefig(filename)

