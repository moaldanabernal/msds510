'''
This module transforms a cvs original file and convert it to utf8
Then, the file names are improved into the utf8 new file
'''

import sys
import csv


'''UTF-8 encoded CSV'''


with open(sys.argv[1], 'rb') as file:
    '''
    read the cvs original file and convert it to utf8 
    '''
    my_oldfile = file.read()
    file_iso = my_oldfile.decode('iso-8859-1')
    file_utf8 = file_iso.encode('utf8')


with open(sys.argv[2], 'wb') as emptyfile:
    '''
    write to disk new utf8 file
    '''
    emptyfile.write(file_utf8)


'''Friendly headers'''


with open(sys.argv[2], 'r') as in_file:
    '''
    read utf8 file and extract first line, which is the original field names, in order to improve them
    '''
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
    '''
    write in utf8 file the new field names improved
    '''
    writer = csv.DictWriter(new_file, fieldnames=in_line.fieldnames)

    firstRow = {}
    for i in in_line.fieldnames:
        firstRow[i] = i
    writer.writerow(firstRow)
    for row in record:
        writer.writerow(row)
