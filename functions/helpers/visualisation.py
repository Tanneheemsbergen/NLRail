import matplotlib.pyplot as plt
import numpy as np
import statistics
import datetime

def histogram(results, input_file_name, algorithm):

    # Set figure base
    plt.rcParams["figure.figsize"] = [10, 10]
    plt.rcParams["figure.autolayout"] = True

    # Information
    x = sorted(results)
    print(x)
    iterations = len(x)
    current_time = datetime.datetime.now()
    mean = statistics.mean(x)
    sd = statistics.stdev(x)

    # Figure information and settings
    plt.grid()
    plt.hist(x, density=False, bins=100, label="Data")
    plt.xticks(range(0, 11000, 1000), fontsize=15)
    plt.yticks(range(0, 450, 50), fontsize=15)
    plt.ylabel("Frequency", fontsize=18)
    plt.xlabel("K-value", fontsize=18)

    # Figure layout
    plt.title(f"Result of {iterations} iterations in space: {input_file_name}, with algorithm: {algorithm}", fontsize=18)
    plt.text(200, 25, f"mean: {mean},\n sd: {sd}", fontsize=18)
    plt.savefig(f"Result-pictures/Histogram-{iterations}-{input_file_name}-{algorithm}-{current_time}.png")


"""
Creates visualistion of the connections that the train has used
"""
def visualisation(graph, trajects, filename):

    # Set figure base
    plt.rcParams["figure.figsize"] = [15, 20]
    plt.rcParams["figure.autolayout"] = True

    # Makes a list of all the x and y coordinates
    x = []
    y = []
    name_stations = []
    for station in graph.all_stations:
        x.append(float(graph.all_stations[station].xcoordinate))
        y.append(float(graph.all_stations[station].ycoordinate))
        name_stations.append(graph.all_stations[station].name)

    # Figure information and settings
    plt.xlabel("y-Coordinate", fontsize=25)
    plt.ylabel("X-Coordinate", fontsize=25)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.figure(1)
    plt.plot(y, x, 'r*')
    plt.axis([min(y) - 0.2, max(y) + 0.2, min(x) - 0.2, max(x) + 0.2])

    for name in name_stations:
        connections = list(graph.all_stations[name].time.keys())
        index_first_station = name_stations.index(name)
        for connection in connections:
            index_destination = name_stations.index(connection)

            # Plots all the possible connections
            plt.plot([y[index_first_station], y[index_destination]], [x[index_first_station],
                        x[index_destination]], 'b', alpha=0.1)

    # List of colors that can be used for the train tracks
    colors = ['g', 'r', 'c', 'm', 'y', 'k', 'w']

    i = 0
    linewidth = 10
    for traject in trajects:
        color = colors[i]
        for station in range(len(traject) - 1):
            index_first_station = name_stations.index(traject[station])
            index_next_station = name_stations.index(traject[station + 1])

            # Plot the lines between the connections of the trajects
            plt.plot([y[index_first_station], y[index_next_station]], 
                        [x[index_first_station], x[index_next_station]], 
                            color, linewidth=linewidth, alpha=0.3)

        # If all the colors are used, it takes the first color from the list again
        if i > 5:
            i = 0
        else:
            i += 1
        linewidth -= 2

    # Add name of the station to the points in the visualisation
    for y, x, s in zip(y, x, name_stations):
        plt.text(y, x, s, fontsize=15)

    plt.savefig(f"Result-pictures/{filename}")
