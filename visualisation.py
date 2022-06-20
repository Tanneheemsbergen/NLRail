import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 
import statistics

from functions.classes.graph_class import Graph

# def barplot(results):
#     plt.figure(3)
#     import matplotlib.pyplot as plt
#     fig = plt.figure()
#     ax = fig.add_axes([0,0,1,1])
#     langs = ['C', 'C++', 'Java', 'Python', 'PHP']
#     students = [23,17,35,29,12]
#     ax.bar(langs,students)
#     plt.show()


def histogram(results):
    plt.rcParams["figure.figsize"] = [10, 10]
    plt.rcParams["figure.autolayout"] = True
    x = sorted(results)
    print(x)
    #print(x[-1])
    iterations = len(x)
    q25, q75 = np.percentile(x, [25, 75])
    bin_width = 2 * (q75 - q25) * len(x) ** (-1/3)
    bins = round((x[-1] - x[0]) / bin_width)
    #print("Freedman–Diaconis number of bins:", bins)
    plt.grid()
    plt.hist(x, density=True, bins=bins, label="Data")
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel("Probabilty Density", fontsize=18)
    plt.xlabel("K-value", fontsize=18)
    plt.title(f"Nationaal - Random Algorithm of {iterations} iterations", fontsize=24)
# mn, mx = plt.xlim()
# plt.xlim(mn, mx)
# kde_xs = np.linspace(mn, mx, 300)
# kde = st.gaussian_kde(x)
# plt.plot(kde_xs, kde.pdf(kde_xs), label="PDF")
# plt.legend(loc="upper left")
# plt.ylabel("Probability")
# plt.xlabel("Data")
# plt.title("Histogram");

    plt.savefig(f"N-Histogram{iterations}Random.png")

def normal_distribution(results):
    plt.rcParams["figure.figsize"] = [10, 10]
    plt.rcParams["figure.autolayout"] = True

    x_axis = sorted(results)
    iterations = len(x_axis)
    print(f"ordered!{x_axis}")

    # Calculating mean and standard deviation
    mean = statistics.mean(x_axis)
    sd = statistics.stdev(x_axis)
    

    plt.figure(0)
    plt.hist(results)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel("Probabilty Density", fontsize=18)
    plt.xlabel("K-value", fontsize=18)
    plt.title(f"Normal distribution of {iterations} iterations - Holland", fontsize=24)

    x = x_axis[0]
   
    
    plt.grid()
    plt.text(x, 0.0001, f"mean: {mean},\n sd: {sd}", fontsize=15)
    plt.tight_layout()
    plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
    
    plt.savefig(f"NormalDistribution{iterations}.png")

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

    plt.xlabel("y-Coordinate", fontsize = 25)
    plt.ylabel("X-Coordinate", fontsize = 25)
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
        if i > 5:
            i = 0
        else:
            i += 1
        linewidth -= 2

    for y, x, s in zip(y, x, name_stations):
        plt.text(y, x, s, fontsize = 15)

    plt.savefig(filename)

