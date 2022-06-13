import csv

class Station(object):

    def __init__(self, name, xcoordinate, ycoordinate):
        self.name = name
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate
        self.connections = self.load_connection()


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

    def __repr__(self):
        """
        Make sure that the object is printed properly if it is in a list/dict.
        """
        connections = ""
        for i in self.connections:
            connections += (f"{i}, ")
        return connections