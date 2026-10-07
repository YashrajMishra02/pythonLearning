
# Comma Seperated Value (csv) files Dictonary read methods 

import csv
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # print(line)
        print(line['email'])
        # print(type(line))