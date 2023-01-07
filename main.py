import csv
import pandas
 
# reading the CSV file
csvFile = pandas.read_csv('automobile.csv')
 
# displaying the contents of the CSV file
print(csvFile)