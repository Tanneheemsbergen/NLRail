def calculate_quality():

    """ Explanation formula:
    K = quality score of trajects
    p = percentage ridden train connections
    T = amount of trajects
    Min = total amount of minutes
    """

    Min = 0
    p = 1 - connection / all_connections
    T = len(trajects)

    for connection in all_connections:
        Min += int(connection[2])

    K = p * 10000 - (T * 100 + Min)
    return K
