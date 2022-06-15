import csv

class Station(object):

    def __init__(self, name, xcoordinate, ycoordinate):
        self.name = name
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate
       # self.source_file = source_file
        self.time = self.load_connection_time()

    def load_connection_time(self):
        connection_time = {}
        with open("csvfiles/ConnectiesHolland.csv", 'r') as in_file:
            reader = csv.DictReader(in_file)
          
            for row in reader:
                if row['station1'] == self.name:    
                    connection_time[row['station2']] = row['distance']
                elif row['station2'] == self.name:
                    connection_time[row['station1']] = row['distance']

        return connection_time

    def location(self):
        locations = {
            "Name": "station",
            "lat": "x",
            "lon": "y"
        }
        return locations

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        connections = "["
        for connection in list(self.time.keys()):
            if connection == list(self.time.keys())[-1]:
                connections += (f"{connection}")
            else:
                connections += (f"{connection}, ")
        connections += "]"
        return connections
