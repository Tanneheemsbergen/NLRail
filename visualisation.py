import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 
import statistics

#from Collections import sort

from functions.classes.graph_class import Graph

<<<<<<< HEAD
def visualisation(station_inputs, connections_input, check_connections_left):

    stations = Graph(station_inputs).all_stations
    connections = connections_input
    check_connections_left = check_connections_left
    #test_graph = Graph("csvfiles/StationsHolland.csv")

    plt.rcParams["figure.figsize"] = [20, 20]
    plt.rcParams["figure.autolayout"] = True

    x = []
    y = []
    name_stations = []
    for station in stations:
        x.append(float(stations[station].xcoordinate))
        y.append(float(stations[station].ycoordinate))
        name_stations.append(stations[station].name)

    plt.xlabel("y-Coordinate")
    plt.ylabel("X-Coordinate")

    plt.plot(y, x, 'r*')

    for name in name_stations:
        connections = list(stations[name].time.keys())
        index_first_station = name_stations.index(name)
        for connection in connections:
            index_destination = name_stations.index(connection)
            plt.plot([y[index_first_station], y[index_destination]],[x[index_first_station], x[index_destination]], 'b')

    plt.axis([4.2, 5.2, 51.2, 53.2])

    for y, x, s in zip(y, x, name_stations):
        plt.text(y, x, s)


    plt.savefig("testplotnew.png")

def barplot(results):
    #print("Hello")
    #print(results)
    # Plot between -10 and 10 with .001 steps.
    #x_axis = np.arange[results]
    x_axis = sorted(results, reverse=True)#results.sorted()
    print(x_axis)

    # Calculating mean and standard deviation
    mean = statistics.mean(x_axis)
    sd = statistics.stdev(x_axis)
    
    plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
    plt.savefig("barplot.png")
    #plt.show()
    #print(results)
    # x-coordinates of left sides of bars 
#left = len(results)
    
    # heights of bars
    #height = results
    
    # labels for bars
    #tick_label = ['one', 'two', 'three', 'four', 'five']
    
    # # plotting a bar chart
    # plt.bar(left, height, width = 0.1, align="center", color = ['black'])
    
    # # naming the x-axis
    # plt.xlabel('x - axis')
    # # naming the y-axis
    # plt.ylabel('y - axis')
    # # plot title
    # plt.title('My bar chart!')
    
    # # function to show the plot
    # #plt.show()
    # plt.savefig("barplot.png")
=======
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

    plt.plot(y, x, 'r*')

    for name in name_stations:
        connections = list(graph.all_stations[name].time.keys())
        index_first_station = name_stations.index(name)
        for connection in connections:
            index_destination = name_stations.index(connection)
            plt.plot([y[index_first_station], y[index_destination]],[x[index_first_station], x[index_destination]], 'b', alpha=0.1)
    

    colors = ['g', 'r', 'c', 'm', 'y', 'k', 'w']
    
    i = 0 
    linewidth=1
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
        linewidth += 2


    plt.axis([4.2, 5.2, 51.2, 53.2])

    for y, x, s in zip(y, x, name_stations):
        plt.text(y, x, s)


    plt.savefig(filename)

>>>>>>> 47c0623a0c522c32d9fffed8b13197ce8ccd3dc4
