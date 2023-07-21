import csv
with open ('userdata.csv','w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(["ID","Activity","Description","Level"])