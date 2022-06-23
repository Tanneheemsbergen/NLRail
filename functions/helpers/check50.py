import csv

def check(trajects, quality):
    with open(f'output.csv', 'w') as file:
        writer = csv.writer(file)
        header = ['train', 'stations']
        writer.writerow(header)
        i = 1
        for traject in trajects:
            data = [f"train_{i}", ('[%s]' % ', '.join(map(str, traject)))]
            i += 1
            writer.writerow(data)
        writer.writerow(['score', quality])