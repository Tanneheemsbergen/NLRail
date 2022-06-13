import matplotlib.pyplot as plt
import pandas as pd

stations = pd.read_csv("csvfiles/StationsHolland.csv")
print(stations["x"][0])
plt.xlabel("X-Coordinate")
plt.ylabel("Y-Coordinate")
plt.scatter(stations["x"], stations["y"])
plt.plot([stations["x"][0],stations["x"][1]], [stations["y"][0], stations["y"][1]])

plt.savefig("testplot.png")
