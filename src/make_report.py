'''
This module creates a markdown report of the top ten Avengers sorted by the number of appearances.
The user should type two parameters:
1. The .cvs file name
2. A markdown report name to create
'''

import csv
import sys
import operator
from msds510.util import Avenger

'''1. Read a file .csv'''


def read_file(file_name):
    '''
    :param get a file .csv:
    :return: return a list of the top ten Avengers sorted by the number of appearances
    '''
    with open(file_name, 'r') as lines:
        records = csv.reader(lines)
        column_names = next(records)

        for keys in range(len(column_names)):
            column_names[keys] = column_names[keys].lower()
            column_names[keys] = column_names[keys].strip('\n').strip('?').rstrip().lstrip()
            column_names[keys] = column_names[keys].replace('/', '_').replace(' ', '_')

        ten_rows = [Avenger(dict(zip(column_names, row))) for row in records]
        ten_rows.sort(key=operator.attrgetter('appearancesInComics'), reverse=True)
        return ten_rows[0:10]

'''2. Create report'''


def create_report(report_name, top_ten_rows):
    '''
    :param get a markdown report name to create:
    :param get a list of the top ten Avengers sorted by the number of appearances
    :return: not return
    '''
    with open(report_name, 'w') as write_record:
        for record in range(len(top_ten_rows)):
            write_record.writelines(("# ", str((record + 1)) + ". ", top_ten_rows[record].name, '\n\n'))
            write_record.writelines(("* Number of Appearances: ", str(top_ten_rows[record].appearancesInComics), '\n'))
            write_record.writelines(("* Year Joined: ", str(top_ten_rows[record].joinYear), '\n'))
            write_record.writelines(("* Years Since Joining: ", str(top_ten_rows[record].yearsSince), '\n'))
            write_record.writelines(("* URL: ", top_ten_rows[record].assignedURL, '\n\n'))
            write_record.writelines(("## Notes\n\n"+top_ten_rows[record].notesData, '\n\n'))

'''Main function'''


if __name__ == "__main__":
    '''
    call main function with tow input parameters:
    1. a file .csv
    2. markdown report name to create
    '''
    create_report(sys.argv[2], read_file(sys.argv[1]))
