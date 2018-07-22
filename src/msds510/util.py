'''
This module includes main functions and include changes after using flake8 and PEP 257 Docstring Conventions.
Avenger class
'''

import csv
import datetime
import operator

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
        ten_rows.sort(key=operator.attrgetter('appearancesInComics'), reverse=True)
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
            write_record.writelines(("# ", str((record + 1)) + ". ", top_ten_rows[record].name, '\n\n'))
            write_record.writelines(("* Number of Appearances: ",
                                     str(top_ten_rows[record].appearancesInComics), '\n'))
            write_record.writelines(("* Year Joined: ", str(top_ten_rows[record].joinYear), '\n'))
            write_record.writelines(("* Years Since Joining: ", str(top_ten_rows[record].yearsSince), '\n'))
            write_record.writelines(("* URL: ", top_ten_rows[record].assignedURL, '\n\n'))
            write_record.writelines(("## Notes\n\n"+top_ten_rows[record].notesData, '\n\n'))


'''Convert a string to boolean'''


def to_bool(stringToMakeBool):
    '''
    :param stringToMakeBool: Potential boolean value
    :return: True, False or None
    '''
    stringToMakeBool = stringToMakeBool.lower()
    if stringToMakeBool == "yes":
        return True
    elif stringToMakeBool == "no":
        return False
    else:
        return None


'''convert month name to month number'''


def getmonth(monthtoparse):
    '''
    :param monthtoparse: month in which avenger joined
    :return: the numerical reference of the month, or 1
    '''
    monthdict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    for key in monthdict:
        if key in monthtoparse:
            return monthdict[key]
    return 1


'''days between two date'''


def datediffcalculator(joinDate):
    '''
    :param joinDate: Date to calculate time elapsed since
    :return: Time elapsed since joinDate
    '''
    try:
        today = datetime.datetime.now().date()
        joinDate
        difference = today - joinDate
        return difference
    except Exception:
        return None
        raise


class Avenger:
    def __init__(self, record):
        """
        Initializes the object with a dictionary-based record.
        Args:
            record (dict): Dictionary-based record of Avenger data
        """
        self.data = record
        self.assignedURL = self.data['url']
        self.name = self.data['name_alias']
        self.appearancesInComics = int(self.data['appearances'])
        self.current_status = to_bool(self.data['current'])
        self.avengerGender = self.data['gender']
        self.notesData = (self.data['notes'].strip('\n'))
        self.joinYear = int(self.data['year'])
        self.first_appearance = self.data['full_reserve_avengers_intro']
        self.dateJoined = datetime.date(int(self.data['year']),
                                        getmonth(self.data['full_reserve_avengers_intro']), 1)
        diff = datediffcalculator(self.dateJoined)
        self.days = int(diff/datetime.timedelta(days=1))
        self.yearsSince = int(diff/datetime.timedelta(days=365))
        self.probationary_introl = self.data["probationary_introl"]
        self.death1 = to_bool(self.data["death1"])
        self.death2 = to_bool(self.data["death2"])
        self.death3 = to_bool(self.data["death3"])
        self.death4 = to_bool(self.data["death4"])
        self.death5 = to_bool(self.data["death5"])
        self.honorary = to_bool(self.data["honorary"])
        self.return1 = to_bool(self.data["return1"])
        self.return2 = to_bool(self.data["return2"])
        self.return3 = to_bool(self.data["return3"])
        self.return4 = to_bool(self.data["return4"])
        self.return5 = to_bool(self.data["return5"])
        self.avengerDict = {'url': self.assignedURL,
                            'name_alias': self.name,
                            'appearances': self.appearancesInComics,
                            'current': self.current_status,
                            'gender': self.avengerGender,
                            'probationary_introl': self.probationary_introl,
                            'full_reserve_avengers_intro': self.first_appearance,
                            'year': self.joinYear,
                            'years_since_joining': self.yearsSince,
                            'honorary': self.honorary,
                            'death1': self.death1,
                            'return1': self.return1,
                            'death2': self.death2,
                            'return2': self.return2,
                            'death3': self.death3,
                            'return3': self.return3,
                            'death4': self.death4,
                            'return4': self.return4,
                            'death5': self.death5,
                            'return5': self.return5,
                            'notes': self.notesData}

    def return_dict(self):
        '''
        :return: dictionary of all data with expected headers
        '''
        return self.avengerDict

    def url(self):
        """
        Returns:
            str: The URL of the comic character on the Marvel Wikia
        """
        return self.assignedURL

    def name_alias(self):
        """
        Returns:
            str: The full name or alias of the character
        """
        return self.name

    def appearances(self):
        """
        Returns:
            int: The number of comic books that character appeared in as of April 30
        """
        return self.appearancesInComics

    def is_current(self):
        """
        Returns:
            bool: Is the member currently active on an avengers affiliated team? (True/False)
        """
        return self.current_status

    def gender(self):
        """
        Returns:
            str: The recorded gender of the character
        """
        return self.avengerGender

    def year(self):
        """
        Returns:
            int: The year the character was introduced as a full or reserve member of the Avengers
        """
        return self.joinYear

    def getmonth(self, monthtoparse):
        monthdict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                     'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        for key in monthdict:
            if key in monthtoparse:
                return monthdict[key]

    def date_joined(self):
        """
        Returns:
            datetime.date: The date the character joined
        """
        return self.dateJoined

    def days_since_joining(self):
        """
        Returns:
            int: The number of integer days since the character joined
        """
        return self.days

    def years_since_joining(self):
        """
        Returns:
            int: The number of integer years since the character joined
        """
        return self.yearsSince

    def notes(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES
        Returns:
            str: Descriptions of deaths and resurrections.
        """
        return self.notesData

    def __str__(self):
        """
        Returns:
            str: A human-readable value for this character
        """
        return '%s' % self.name

    def __repr__(self):
        """
        Returns:
            str: String representation of object.  Useful for debugging.
        """
        return 'Avenger(name_alias=%s, url=%s)' % (self.name, self.assignedURL)
