# In addition to the above requirements, your files must be stored using the convention discussed in the lecture. You will be submitting a ZIP file containing all of your files.


# part 1: creates an empty list
sales_data = []

# part 2: opens up this file (SalesJan2009.csv - you need to download it to your hard drive) and converts the data within it to JSON format. 
#          The fields in the file are listed in order as follows: Transaction_date, Product, Price, Payment_Type, Name, City, State, Country

import csv 
with open(r"D:\1PythonWorks\CSC1500\Lab 10\Lab-10\SalesJan2009.csv", "r") as inFile:
    csvReader = csv.reader(inFile)
    for line in csvReader:
        print(line)





# part 3: You will process this line-by-line and create a dictionary of each line. As you create each dictionary, you will append it to the sales_data list. 
#         You must also clean up extra quote characters from each piece of data you process.



# part 4: At the end of your processing, you will save your sales_data list to a file called "transaction_data.json"
