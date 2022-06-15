import csv
from .station_class import Station

class Graph():
    def __init__(self, source_file, source_file_connections):
        self.all_stations = self.load_nodes(source_file, source_file_connections)


    def load_nodes(self, source_file, source_file_connections):
        """
        Load all the nodes into the graph.
        """
        all_stations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                all_stations[row['station']] = Station(row['station'], row['x'], row['y'], source_file_connections)

        return all_stations
