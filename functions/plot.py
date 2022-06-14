import matplotlib.pyplot as plt
import pandas as pd
from classes.graph_class import Graph

def plot_function():
    stations = pd.read_csv("csvfiles/StationsHolland.csv")
    print(stations["x"][0])
    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.scatter(stations["x"], stations["y"])

    x_coordinates = []
    y_coordinates = []

    for traject in trajects:
        for station in stations:
            x_coordinates.append(station.x)
            y_coordinates.append(station.y)
        plt.plot(x_coordinates, y_coordinates)

    plt.savefig("test.png")
