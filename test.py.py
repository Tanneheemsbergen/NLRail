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

trajects = []
total_time_traject = 0
count = 0
for i in range(MAX_AMOUNT_TRAJECTS):
    traject = []
    total_time = 0
    time = 0
    station = random.choices(all_connections, k=1)[0][0]
    traject.append(station)

    while  total_time < MAX_TIME:
        # print("station: ")
        # print(station)
        options_next_station = []
        for i in all_connections:
            if i[0] == station:
                options_next_station.append(i)
        if len(options_next_station) == 0:
            break
        # print("options: ")
        # print(options_next_station)
        next_station = random.choices(options_next_station, k=1)[0]
        # print("option next station: ")
        # print(next_station)
        all_connections.remove(next_station)

        traject.append(next_station[1])
        count +=1
        total_time += int(connection[2])
        station = next_station[1]

    trajects.append(traject)
    total_time_traject += total_time

    # print(traject)
    # print(total_time)
print(trajects)
# print(total_time_traject)

K = ((count / 28) * 10000) - (len(trajects) * 100 + total_time_traject)
print(K)
