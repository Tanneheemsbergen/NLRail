import random
from calculation import calculate_quality
MAX_AMOUNT_TRAJECTS = 7
MAX_TIME = 120

with open("csvfiles/ConnectiesHolland.csv") as f:
    connecties = f.readlines()
all_connections = []

for line in connecties[1:]:
    connection = []
    for i in line.strip().split(','):
        connection.append(i)
    all_connections.append(connection)

check_connections_left = all_connections.copy()
trajects = []
total_time_traject = 0

for i in range(MAX_AMOUNT_TRAJECTS):
    copy_connecties = all_connections.copy()
    traject = []
    total_time = 0
    randomconnection = random.choices(all_connections, k=1)[0]
    station = random.choices([randomconnection[0],randomconnection[1]], k=1)[0]
    traject.append(station)

    while  total_time < MAX_TIME:
        # print("station: ")
        # print(station)
        options_next_station = []
        for i in copy_connecties:
            if i[0] == station or i[1] == station:
                options_next_station.append(i)
        if len(options_next_station) == 0:
            break
        # print("options: ")
        # print(options_next_station)

        next_station = random.choices(options_next_station, k=1)[0]
        # print("option next station: ")
        # print(next_station)
        copy_connecties.remove(next_station)
        if next_station in check_connections_left:
            check_connections_left.remove(next_station)

        total_time += int(next_station[2])
        if next_station[0] == station:
            traject.append(next_station[1])
            station = next_station[1]

        elif next_station[1] == station:
            traject.append(next_station[0])
            station = next_station[0]

    total_time_traject += total_time

    trajects.append(traject)


print(trajects)
print(f"total time of all trajects: {total_time_traject}")
print(f"connections not used {check_connections_left}")
connections_used = len(all_connections) - len(check_connections_left)
print(connections_used)
print(len(all_connections))
print(total_time_traject)
print(MAX_AMOUNT_TRAJECTS)
# calculate_quality(connections_used, len(all_connections))
print(calculate_quality(connections_used, len(all_connections),total_time_traject,MAX_AMOUNT_TRAJECTS))
