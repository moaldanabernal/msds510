
This project uses a Avengers dataset and transforms the .cvs original file to utf8 in Python. Then, the column names are improved into the utf8 new file. In the end, it creates a markdown report of the top ten Avengers sorted by the number of appearances.

Steps:

1. Run process_csv.py

    Executes as,
        python process_csv.py ../data/raw/avengers.csv ../data/processed/avengers_processed.csv


2. Run make_report.py

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
