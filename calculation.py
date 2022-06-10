def calculate_quality(amount_of_connections, total_connections, total_time, T):

    """ Explanation formula:
    K = quality score of trajects
    p = percentage ridden train connections
    T = amount of trajects
    Min = total amount of minutes
    """


    p = 1 - amount_of_connections / total_connections
    
    K = p * 10000 - (T * 100 + total_time)
    return K
