import csv
import sys
import operator
from msds510.util import *

#1. Read file .csv

def read_file(file_name):
    with open(file_name, 'r') as lines:
        records = csv.reader(lines)
        column_names = next(records)

        for keys in range(len(column_names)):
            column_names[keys] = column_names[keys].lower()
            column_names[keys] = column_names[keys].strip('\n').strip('?').rstrip().lstrip()
            column_names[keys] = column_names[keys].replace('/','_').replace(' ', '_')

        #Note: Avenger class is code reused!
        #I tested this class, for the avenger file, and I could see it is useful for initializing a dictionary-based record.

        ten_rows = [Avenger(dict(zip(column_names, row))) for row in records]
        ten_rows.sort(key=operator.attrgetter('appearancesInComics'), reverse=True)
        return ten_rows[0:10]

#2. Create report

def create_report(report_name, top_ten_rows):
    with open(report_name, 'w') as write_record:
        for record in range(len(top_ten_rows)):
            write_record.writelines(("# ",str((record+ 1))+". ", top_ten_rows[record].name, '\n\n'))
            write_record.writelines(("* Number of Appearances: ", str(top_ten_rows[record].appearancesInComics), '\n'))
            write_record.writelines(("* Year Joined: ", str(top_ten_rows[record].joinYear), '\n'))
            write_record.writelines(("* Years Since Joining: ", str(top_ten_rows[record].yearsSince), '\n'))
            write_record.writelines(("* URL: ", top_ten_rows[record].assignedURL, '\n\n'))
            write_record.writelines(("## Notes\n\n"+top_ten_rows[record].notesData, '\n\n'))

#Main function

if __name__ == "__main__":
    create_report(sys.argv[2], read_file(sys.argv[1]))
