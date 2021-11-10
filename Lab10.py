import ssl
import csv
#ssl.create_default_https_context = ssl.create_unverified_context()
import json
handle = "SalesJan2009.csv"
sales_data = []
#eData = json.loads(data)

with open(handle) as inFile:
    csvReader = csv.DictReader(inFile)
    for row in csvReader:
        sales_data.append(row)

with open("transaction_data.json", 'w') as outFile:
    jsonString = json.dumps(sales_data,indent=4)
    outFile.write(jsonString)
    
