'''
This module uses Utils and Avenger class.
This module includes changes after using flake8 and PEP 257 -- Docstring Conventions.
This module creates a markdown report of the top ten Avengers sorted by the number of appearances.
The user should type two parameters:
1. The .cvs file name
2. A markdown report name to create
Executes as, python make_report.py ../data/processed/avengers_processed.csv ../reports/top_ten_appearances.md
'''

import sys
from msds510.util import create_report, read_file


def main():
    '''
    call main function with tow input parameters:
    1. a file .csv
    2. markdown report name to create
    '''
    create_report(sys.argv[2], read_file(sys.argv[1]))


'''Main function'''

if __name__ == '__main__':
    main()
