import csv

class Station(object):

    def __init__(self, name, xcoordinate, ycoordinate):
        self.name = name
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate
        self.connections = self.load_connection()
        self.time = self.load_connection_time()


    def load_connection(self):
        connections = []
        with open("csvfiles/ConnectiesHolland.csv", 'r') as in_file:
            reader = csv.DictReader(in_file)
             
            for row in reader:
                if row['station1'] == self.name:
                    connections.append(row['station2'])

                elif row['station2'] == self.name:
                    connections.append(row['station1'])

        return connections
    def load_connection_time(self):
        connections = []
        connection_time = {}
        with open("csvfiles/ConnectiesHolland.csv", 'r') as in_file:
            reader = csv.DictReader(in_file)
             
            for row in reader:
                if row['station1'] == self.name:
    
                    connection_time[row['station2']] = row['distance']
                elif row['station2'] == self.name:
                    connection_time[row['station1']] = row['distance']
            # connections.append(connection_time)
        return connection_time


    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        connections = "["
        for connection in self.connections:
            if connection == self.connections[-1]:
                connections += (f"{connection}")
            else:
                connections += (f"{connection}, ")
        connections += "]"
        return connections