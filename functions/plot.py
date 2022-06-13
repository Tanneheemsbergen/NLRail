import matplotlib.pyplot as plt
import pandas as pd
from classes.station_class import Station

stations = pd.read_csv("../csvfiles/StationsNationaal.csv")
print("stations")
print(stations)
connections = pd.read_csv("../csvfiles/ConnectiesNationaal.csv")
print("con")
print(connections)

# for i in range(len(stations)):
#     for j in range(len(connections)):
#         if i["station"] == j["station1"]:
#             print(i)
#             print(j["x"])

print(stations["x"][0])
plt.xlabel("X-Coordinate")
plt.ylabel("Y-Coordinate")
plt.xticks(rotation=90)
plt.scatter(stations["x"], stations["y"])
for i in range(len(connections) -1):
    plt.plot([connections["station1"][i],connections["station1"][i+1]], [connections["station2"][i], connections["station2"][i+1]])

plt.savefig("test2.png")