import copy

def calculate_quality(trajects, start_graph, T):
    all_connections = start_graph.all_stations
    connections_left = copy.deepcopy(all_connections)
    for traject in trajects:
        for i in range(len(traject)-1):
            if traject[i+1] in list(connections_left[traject[i]].time.keys()):
                connections_left[traject[i]].time.pop(traject[i+1])

            if traject[i] in list(connections_left[traject[i+1]].time.keys()):
                connections_left[traject[i+1]].time.pop(traject[i])

    total_connections = 0
    for i in all_connections:
        total_connections += len(all_connections[i].time)

    total_connections = total_connections / 2

    connections_left_count = 0
    for i in connections_left:
        connections_left_count += len(connections_left[i].time)

    connections_left_count = connections_left_count / 2

    amount_of_connections = total_connections - connections_left_count

    total_time = calculate_total_time(all_connections, trajects)
    quality = formula_quality(amount_of_connections, total_connections, total_time, T)
    return quality

def calculate_total_time(all_connections, trajects):
    total_time = 0
    for traject in trajects:
        for i in range(len(traject)-1):
            print(all_connections[traject[i]].time)
            total_time += all_connections[traject[i]].time[traject[i+1]]
    return(total_time)

def formula_quality(amount_of_connections, total_connections, total_time, T):

    """ Explanation formula:
    K = quality score of trajects
    p = percentage ridden train connections
    T = amount of trajects
    Min = total amount of minutes
    """

    p = amount_of_connections / total_connections

    K = p * 10000 - (T * 100 + total_time)
    return K
