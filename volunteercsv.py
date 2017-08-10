import csv
#import the basic python csv module
#load out input file into a variable and create a blank csv file to output
input_file = 'python_volunteer.csv'
output_file = "volunteer_deduped.csv"
#Loop through the CSV

with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
    reader = csv.reader(file_in)
    #makes a variable
    writer = csv.writer(file_out)
    d = []
    #list in computer
    for row in reader:
        email = row[7]
        #csv is a list of lists
        if email not in d:
            d.append(email)
            writer.writerow(row)
            #emails that are not already in the list are then added
