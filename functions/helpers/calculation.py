import copy

"""
Calculates the quality of the given trajects
"""


def calculate_quality(trajects, start_graph, T):

    # Gets all the stations
    all_connections = start_graph.all_stations

    # All the connections that are not used
    connections_left = copy.deepcopy(all_connections)
    for traject in trajects:
        for i in range(len(traject) - 1):

            # Checks if a connection is still in the dictionary connections_left,
            # if it is it is removed for both ways
            if traject[i + 1] in list(connections_left[traject[i]].time.keys()):
                connections_left[traject[i]].time.pop(traject[i + 1])

            if traject[i] in list(connections_left[traject[i + 1]].time.keys()):
                connections_left[traject[i + 1]].time.pop(traject[i])

    # Counts the total connections
    total_connections = 0
    for i in all_connections:
        total_connections += len(all_connections[i].time)

    # We only want to count the connections one way so it is divided by 2
    total_connections = total_connections / 2

    # Counts the amount of connections left
    connections_left_count = 0
    for i in connections_left:
        connections_left_count += len(connections_left[i].time)

    # We only want to count the connections one way so it is divided by 2
    connections_left_count = connections_left_count / 2

    # Calculates the total connections used
    amount_of_connections = total_connections - connections_left_count

    total_time = calculate_total_time(all_connections, trajects)
    quality = formula_quality(amount_of_connections, total_connections, total_time, T)
    return quality


def calculate_total_time(all_connections, trajects):

    # Adds all the time of all the connections
    total_time = 0
    for traject in trajects:
        for i in range(len(traject) - 1):
            total_time += all_connections[traject[i]].time[traject[i + 1]]

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
