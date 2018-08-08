# msds510

DSC510 - Programming (Python)

Final Project


Steps:

1. Run process_csv.py

    This module transforms the .cvs original file and convert it to utf8.
    Then, the column names are improved into the utf8 new file.

    Executes as,
        python process_csv.py ../data/raw/avengers.csv ../data/processed/avengers_processed.csv


2. Run make_report.py

    This module creates a markdown report of the top ten Avengers sorted by the number of appearances.
    In this module, we should use the utf8 new file.

    The user should type two parameters:
        1. The .cvs utf8 new file
        2. A markdown report name to create

    Executes as,
        python make_report.py ../data/processed/avengers_processed.csv ../reports/top_ten_appearances.md


Other modules:

A. util.py

    This module uses a class called Avenger.
    It includes the main functions:

        read_file()
            Read the .cvs utf8 new file and return a list of the top ten Avengers sorted by the number of appearances.

        create_report()
            Get a markdown report name and create it with the top ten Avengers sorted by the number of appearances.

B. test_avenger.py

    This module tests the Avenger class.

    Executes as,
        cd ..msds510\src\msds510
        python test_avenger.py
