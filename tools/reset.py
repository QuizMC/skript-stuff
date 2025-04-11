import csv
import time

savesFile = "names.txt"

startTime = time.time()

with open("names.txt", "r") as savesFileReader:
    validVariables = {line.strip() for line in savesFileReader}

with open("variables.csv", "r", encoding="utf-8") as csvFileReader:
    csvReader = csv.reader(csvFileReader)
    processedRows = []
    wipedRows = []
    for row in csvReader:
        if row and (row[0].startswith(tuple(validVariables))):
            processedRows.append(row)
        else:
            wipedRows.append(row)

with open("variables.csv", "w", newline="") as csvFileWriter:
    csvWriter = csv.writer(csvFileWriter)
    csvWriter.writerows(processedRows)

endTime = time.time()

print(f"Total rows processed: {len(processedRows) + len(wipedRows)}")
print(f"Rows kept: {len(processedRows)}")
print(f"Rows wiped: {len(wipedRows)}")
print(f"Time taken: {endTime - startTime:.2f} seconds")

"""
How to use:
1. Put your variables.csv file in the same directory.
2. Create a text file named `names.txt` with the start of the variables you want to keep (one per line).
3. Run the script
"""