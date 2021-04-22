import csv

with open("./data/StudentsPerformance.csv", "r") as path:
    data = csv.reader(path, delimiter=",")
    for line in data:
        print(line)