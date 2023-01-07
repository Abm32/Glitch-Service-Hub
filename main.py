# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("automobile.csv") 
# Preview the first 5 lines of the loaded data 
name = data['NAME'].tolist()
phone = data['Phone'].tolist()
dist = data['distance'].tolist()

def Convert(string):
    li = list(string.split(","))
    return li

user = input('Query: ')

help1 = ["help","Help","HELP"]
string1 = "Available peeps : "
newname = ','.join(map(str,name))
distance  = ','.join(map(str,dist))
newdist = distance.replace('m', '')
#neww = newding.split("delimiter")
aa = Convert(newdist)

listn = [] #index number of distances within 1 km radius
for inn in aa:
    if int(inn) < 1000:
        listn.append(aa.index(inn))
        
#litnew = listn.sort()
cldistance = ','.join(map(str,listn))
print(listn)


for ele in help1:
    if user == ele:
        user2 = input('Emergency Service (Y/N): ')
        if user2 == "Y" or user2 == "y":
            print(string1 + newdist)
        else:
            print(phone)
