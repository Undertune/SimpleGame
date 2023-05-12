import csv


with open("recources1.csv", 'r') as f:
    csv_reader=csv.reader(f)
    for line in csv_reader:
        print(line[0],line[1])