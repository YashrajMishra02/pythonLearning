
# Writing to Comma Seperated Value (csv) files Dictonary write methods

import csv
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open('new_names.csv','w') as new_file:

        # with DictWriter we need to initialize the fieldnames first 
        fieldnames = ['first_name','last_name','email']
        
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')

        # Allow to write the filednames as a header
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)