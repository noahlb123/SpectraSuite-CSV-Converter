import csv
import os

def TXTToCSV(name):
    root = name.split("/")[-1]
    root = root.split(".")[0]
    return root + ".csv"

for name in os.listdir("./spectrasuite-files"):
    f = open("./spectrasuite-files/" + name, "r")
    r = f.read()
    endIndex = r.index(">>>>>End Processed Spectral Data<<<<<") - 1
    startIndex = 1 + r.index(">>>>>Begin Processed Spectral Data<<<<<") + len(">>>>>Begin Processed Spectral Data<<<<<")
    values = r[startIndex:endIndex]
    specialChar = values[6]
    values = values.split("\n")
    for line in values:
        line = line.split(specialChar)

    with open("./output/" + TXTToCSV(name), 'w') as newFile:
        writer = csv.writer(newFile)
        for i in values:
            writer.writerow([i])

    print("processed", name)