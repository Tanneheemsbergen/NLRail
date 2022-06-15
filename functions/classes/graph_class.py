import csv
from .station_class import Station

class Graph():
    def __init__(self, source_file):
        self.all_stations = self.load_nodes(source_file)


    def load_nodes(self, source_file):
        """
        Load all the nodes into the graph.
        """
        all_stations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                all_stations[row['station']] = Station(row['station'], row['x'], row['y'])
<<<<<<< HEAD
        # print(all_stations)
=======
>>>>>>> 29630d8350960495e66a12e1f114df0ad02eb9cf
        return all_stations
