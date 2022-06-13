import random
from functions.calculation import calculate_quality
def greedy_function(all_connections, MAX_AMOUNT_TRAJECTS, MAX_TIME):

    check_connections_left = all_connections.copy()
    trajects = []
    total_time_traject = 0
    quality = 0

    for i in range(MAX_AMOUNT_TRAJECTS):
        copy_connecties = all_connections.copy()
        traject = []
        total_time = 0
        randomconnection = random.choices(all_connections, k=1)[0]
        station = random.choices([randomconnection[0],randomconnection[1]], k=1)[0]
        traject.append(station)

        while  total_time < MAX_TIME:
            options_next_station = []
            for i in copy_connecties:
                if i[0] == station or i[1] == station:
                    if  total_time + int(i[2]) <= MAX_TIME:
                        options_next_station.append(i)
            if len(options_next_station) == 0:
                break

            next_station = random.choices(options_next_station, k=1)[0]
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
        connections_used = len(all_connections) - len(check_connections_left)
        total_time_traject += total_time
        trajects.append(traject)
        new_quality = calculate_quality(connections_used, len(all_connections),total_time_traject,MAX_AMOUNT_TRAJECTS)
        # if new_quality > quality and len(trajects) == 0:
        #     trajects.append(traject)
        #     quality = new_quality
        if new_quality > quality:
            trajects.remove(traject)
            quality = new_quality
    print(trajects)
    print(f"total time of all trajects: {total_time_traject}")
    print(f"connections not used {check_connections_left}")

    print(calculate_quality(connections_used, len(all_connections),total_time_traject,MAX_AMOUNT_TRAJECTS))
