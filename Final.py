import csv
data = []
with open("final.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)
headers = data[0]
planetdata = data[1:]
for a in planetdata:
    a[2] = a[2].lower()
planetdata.sort(key = lambda planetdata:planetdata[2])

with open("sortedfinal.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)