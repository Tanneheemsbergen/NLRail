def calculate_quality(amount_of_connections, total_connections, total_time, T):

    """ Explanation formula:
    K = quality score of trajects
    p = percentage ridden train connections
    T = amount of trajects
    Min = total amount of minutes
    """
  
    p = amount_of_connections / total_connections

    K = p * 10000 - (T * 100 + total_time)
    return K

def values(all_connections, check_connections_left, total_time, T):
    total_connections = 0
    for i in all_connections:
        total_connections += len(all_connections[i].time)

    total_connections = total_connections / 2

    connections_left = 0
    for i in check_connections_left:
        connections_left += len(check_connections_left[i].time)

    connections_left = connections_left / 2

    amount_of_connections = total_connections - connections_left
    quality = calculate_quality(amount_of_connections, total_connections, total_time, T)
    return quality