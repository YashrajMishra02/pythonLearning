
# csv reader method

import csv

with open('names.csv','r') as csv_file:
    
    # reader method 
    csv_reader = csv.reader(csv_file)
    print(type(csv_reader) )

    # To skip the firest line in csv
    next(csv_reader)

    for line in csv_reader:
        print(line)
        print(type(line)) # here it is a list 
        print(line[2])