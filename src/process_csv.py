import sys
import csv

# UTF-8 encoded CSV

with open(sys.argv[1], 'rb') as file:
    my_oldfile = file.read()

file_iso = my_oldfile.decode('iso-8859-1')
file_utf8 = file_iso.encode('utf8')

with open(sys.argv[2], 'wb') as emptyfile:
    emptyfile.write(file_utf8)

# Friendly headers

with open(sys.argv[2], 'r') as in_file:
    in_line = csv.DictReader(in_file)

    fieldnames = []
    for column in in_line.fieldnames:
        new_header = column.lower()
        new_header = new_header.replace('/', '_').replace(' ', '_')
        new_header = new_header.strip('\n').strip('?')
        fieldnames.append(new_header)

    in_line.fieldnames = fieldnames

    record = []
    for row in in_line:
        record.append(row)

with open(sys.argv[2], 'w', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=in_line.fieldnames)

    firstRow = {}
    for i in in_line.fieldnames:
        firstRow[i] = i
    writer.writerow(firstRow)
    for row in record:
        writer.writerow(row)
