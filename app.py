import csv

f = open("Ru.txt", "r")
r = f.read()
endIndex = r.index(">>>>>End Processed Spectral Data<<<<<") - 1
startIndex = 1 + r.index(">>>>>Begin Processed Spectral Data<<<<<") + len(">>>>>Begin Processed Spectral Data<<<<<")
values = r[startIndex:endIndex]
specialChar = values[6]
values = values.split("\n")
for line in values:
    line = line.split(specialChar)

with open("ru.csv", 'w') as newFile:
    writer = csv.writer(newFile)
    for i in values:
        writer.writerow([i])

print("sucess")
