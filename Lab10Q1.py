import ssl
import csv
#ssl.create_default_https_context = ssl.create_unverified_context()
import json
handle = "SalesJan2009.csv" #filename as a string
sales_data = [] #initialize sales_data list Number 1
#eData = json.loads(data)

with open(handle) as inFile:                    #opens handle var and creates a var to look in the file NUMBER 2
    csvReader = csv.DictReader(inFile)          #initializes a csv file reader to intake Dicts
    for row in csvReader:                       #every row in csvReader
        #NUMBER 3
        sales_data.append(row)                  #is appended to sales_data list


#NUMBER 4
with open("transaction_data.json", 'w') as outFile: #creates transaction_data.json file
    jsonString = json.dumps(sales_data,indent=4)#json.dumps takes sales_data and assigns it to jsonString
    outFile.write(jsonString) #outputs jsonString to outFile
    
