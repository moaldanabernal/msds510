'''
Avenger class
'''

import datetime


class Avenger:
    def __init__(self, avenger_record):
        """
        Constructor takes 1 argument.
        Args:
            avenger_record: a line of avenger file which is a dictionary record.
        """
        self.row = avenger_record
        self.url = self.row['url']
        self.name_alias = self.row['name_alias']
        self.appearances = int(self.row['appearances'])
        self.current = self.convert_boolean(self.row['current'])
        self.gender = self.row['gender']
        self.probationary_introl = self.row["probationary_introl"]
        self.full_reserve_avengers_intro = self.row['full_reserve_avengers_intro']
        self.year = int(self.row['year'])
        self.date_joined = self.month_number(self.row['full_reserve_avengers_intro'])
        self.days_since_joining = datetime.datetime.now().date() - datetime.date(int(self.row['year']), self.date_joined, 1)
        self.years_since_joining = int(self.days_since_joining/datetime.timedelta(days=365))
        self.honorary = self.convert_boolean(self.row['honorary'])
        self.death1 = self.convert_boolean(self.row["death1"])
        self.return1 = self.convert_boolean(self.row["return1"])
        self.death2 = self.convert_boolean(self.row["death2"])
        self.return2 = self.convert_boolean(self.row["return2"])
        self.death3 = self.convert_boolean(self.row["death3"])
        self.return3 = self.convert_boolean(self.row["return3"])
        self.death4 = self.convert_boolean(self.row["death4"])
        self.return4 = self.convert_boolean(self.row["return4"])
        self.death5 = self.convert_boolean(self.row["death5"])
        self.return5 = self.convert_boolean(self.row["return5"])
        self.notes = (self.row['notes'].strip('\n'))

        self.avenger_dictionary = {'url': self.url,
                                   'name_alias': self.name_alias,
                                   'appearances': self.appearances,
                                   'current': self.current,
                                   'gender': self.gender,
                                   'probationary_introl': self.probationary_introl,
                                   'full_reserve_avengers_intro': self.full_reserve_avengers_intro,
                                   'year': self.year,
                                   'years_since_joining': self.years_since_joining,
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
                                   'notes': self.notes}

    def appearances(self):
        """
        Returns:
            int: The number of comic books that character appeared in.
        """
        return self.appearances

    def year(self):
        """
        Returns:
            int: The year the character was introduced as a full or reserve member of the Avengers.
        """
        return self.year

    def is_current(self):
        """
        Returns:
            bool: Is the member currently active on an avengers affiliated team? (True/False)
        """
        return self.current

    def notes(self):
        """
        Returns:
            str: Descriptions of deaths and resurrections.
        """
        return self.notes

    def date_joined(self):
        """
        Returns:
            datetime.date: The date the character joined
        """
        return self.year

    def name_alias(self):
        """
        Returns:
            str: The full name or alias of the character
        """
        return self.name_alias

    def url(self):
        """
        Returns:
            str: The URL of the comic character. Example, http://marvel.wikia.com/wiki/Dane_Whitman
        """
        return self.url

    def gender(self):
        """
        Returns:
            str: The recorded gender of the character
        """
        return self.gender

    def days_since_joining(self):
        """
        Returns:
            int: The number of integer days since the character joined
        """
        return self.days_since_joining

    def years_since_joining(self):
        """
        Returns:
            int: The number of integer years since the character joined
        """
        return self.years_since_joining

    def month_number(self, month_name):
        '''
        :param month_name: month in which avenger joined
        :return: the numerical reference of the month, or 1
        '''
        month_dictionary = {'Jan': 1,
                            'Feb': 2,
                            'Mar': 3,
                            'Apr': 4,
                            'May': 5,
                            'Jun': 6,
                            'Jul': 7,
                            'Aug': 8,
                            'Sep': 9,
                            'Oct': 10,
                            'Nov': 11,
                            'Dec': 12}
        for key in month_dictionary:
            if key in month_name:
                return month_dictionary[key]
        # if month was not found because wrong data, return 1 by default.
        return 1

    def convert_boolean(self, string_data):
        '''
        :param string_data: string value
        :return: True, False or None
        '''
        string_data = string_data.lower()
        if string_data == "yes":
            return True
        elif string_data == "no":
            return False
        else:
            return None

    def return_dict(self):
        '''
        :return: dictionary of all data with expected headers
        '''
        return self.avenger_dictionary

    def __str__(self):
        """
        Returns:
            str: A human-readable value for this character
        """
        return '%s' % self.name_alias

    def __repr__(self):
        """
        Returns:
            str: String representation of object.  Useful for debugging.
        """
        return 'Avenger(name_alias=%s, url=%s)' % (self.name_alias, self.url)
