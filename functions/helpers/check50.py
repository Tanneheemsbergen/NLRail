import csv

"""
Makes an output file with the output of an algorithm (trajects and quality),
so it can be checked with check50.
"""
def check(trajects, quality):

    # Creates a new file
    with open('output.csv', 'w') as file:
        writer = csv.writer(file)

        # Creates a header for the file
        header = ['train', 'stations']
        writer.writerow(header)

        # Adds all the trains to the file
        i = 1
        for traject in trajects:
            data = [f"train_{i}", ('[%s]' % ', '.join(map(str, traject)))]
            i += 1
            writer.writerow(data)

        # Adds the quality score to the file
        writer.writerow(['score', quality])