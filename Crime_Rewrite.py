import csv
import sys

file = 'incidents_part1_part2.csv'
data = []

with open(file, mode='r') as infile:
    reader = csv.reader(infile)
    header = next(reader)
    for row in reader:
        data.append(row)

crime_count = 0
counter_thefts = 0
other_assaults = 0
midnight_crimes = 0
total_instance = dict()

for r in range(0, len(data)):
    crime_count += 1
    total_instance[data[r][12]] = total_instance.get(data[r][12], 0) + 1
    if data[r][12] == "Thefts":
        counter_thefts += 1
    if data[r][12] == "Other Assaults":
        other_assaults += 1
    try:
        time = int(data[r][16])
        if data[r][12] == "Thefts" and 0 <= time <= 6:
            midnight_crimes += 1
    except:
        continue

print("Total number of crimes:", crime_count)
print("Thefts:", counter_thefts)
print("Other Assaults:", other_assaults)
print("Midnight thefts:", midnight_crimes)

numbers = total_instance.items()
most_committed = list()

for c, n in numbers:
    most_committed.append((n, c))

most_committed = sorted(most_committed, reverse=True)
print('The most committed crime:', most_committed[1])

infile.close()
sys.exit(-1)
