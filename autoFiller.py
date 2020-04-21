import os, re, sys, time

try:
    import xlrd
except:
    print("No module name 'xlrd' found. \nInstall the module using 'pip install xlrd'")

try:
    import requests
except:
    print("No module name 'requests' found. \nInstall the module using 'pip install requests'")

url = str(sys.argv[1])
form = requests.get(url)
soureCode = form.text

formKeys = re.findall(r'entry\.[0-9_a-zA-Z]+', soureCode)

spreadSheet = xlrd.open_workbook(str(sys.argv[2]))
sheet = spreadSheet.sheet_by_index(0)

start_idx = 0
choice = int(input("Do your sheet have columns mentioned? \nIf yes, press 1. Else press 0. And enter.\n"))
if(choice == 1):
    start_idx = 1

for r in range(start_idx, sheet.nrows):
    
    formData = {}
    data = sheet.row_values(r)
    
    for i in range(len(formKeys)):
        if(type(data[i]) == float):
            data[i] = int(data[i])        
        formData[formKeys[i]] = data[i]

    print(formData)

    try:
        response = requests.post(url, formData)
        print(response)
        print('Form Submitted!')
        time.sleep(2)
    except:
        print("Error Occured!")
