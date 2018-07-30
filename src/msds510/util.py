'''
This module uses Avenger class.
This module includes main functions and include changes after using flake8 and PEP 257 Docstring Conventions.
Avenger class
'''

import csv
import operator
from msds510.avenger import Avenger


'''Read a file .csv, improve its field names, and get 10 first records'''


def read_file(file_name):
    '''
    :param get a file .csv:
    :return: return a list of the top ten Avengers sorted by the number of appearances.
    '''
    with open(file_name, 'r') as lines:
        records = csv.reader(lines)
        column_names = next(records)

        for keys in range(len(column_names)):
            column_names[keys] = column_names[keys].lower()
            column_names[keys] = column_names[keys].strip('\n').strip('?').rstrip().lstrip()
            column_names[keys] = column_names[keys].replace('/', '_').replace(' ', '_')

        ten_rows = [Avenger(dict(zip(column_names, row))) for row in records]
        ten_rows.sort(key=operator.attrgetter('appearances'), reverse=True)
        return ten_rows[0:10]


'''Create a markdown report'''


def create_report(report_name, top_ten_rows):
    '''
    :param get a markdown report name to create:
    :param get a list of the top ten Avengers sorted by the number of appearances
    :return: not return
    '''
    with open(report_name, 'w') as write_record:
        for record in range(len(top_ten_rows)):
            write_record.writelines(("# ", str((record + 1)) + ". ", top_ten_rows[record].name_alias, '\n\n'))
            write_record.writelines(("* Number of Appearances: ", str(top_ten_rows[record].appearances), '\n'))
            write_record.writelines(("* Year Joined: ", str(top_ten_rows[record].year), '\n'))
            write_record.writelines(("* Years Since Joining: ", str(top_ten_rows[record].years_since_joining), '\n'))
            write_record.writelines(("* URL: ", top_ten_rows[record].url, '\n\n'))
            write_record.writelines(("## Notes\n\n"+top_ten_rows[record].notes, '\n\n'))
