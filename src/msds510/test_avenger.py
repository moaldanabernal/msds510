'''
This module tests Avenger class.
The user should type:
  cd ..msds510\src\msds510
  python test_avenger.py
'''
from avenger import Avenger

def main():
    pym_record = {
        'appearances': '1269',
        'current': 'YES',
        'death1': 'YES',
        'death2': '',
        'death3': '',
        'death4': '',
        'death5': '',
        'full_reserve_avengers_intro': 'Sep-63',
        'gender': 'MALE',
        'honorary': 'Full',
        'name_alias': 'Henry Jonathan "Hank" Pym',
        'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held. \n',
        'probationary_introl': '',
        'return1': 'NO',
        'return2': '',
        'return3': '',
        'return4': '',
        'return5': '',
        'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
        'year': '1963',
        'years_since_joining': '52'
    }

    hank_pym = Avenger(pym_record)
    print('Name/Alias: {}'.format(hank_pym.name_alias_method()))
    print('URL: {}'.format(hank_pym.url_method()))
    print('Is Current?: {}'.format(hank_pym.is_current_method()))
    print('Gender: {}'.format(hank_pym.gender_method()))
    print('Year Joined: {}'.format(hank_pym.year_method()))
    print('Date Joined: {}'.format(hank_pym.date_joined_method()))
    print('Days Since Joined: {}'.format(hank_pym.days_since_joining_method()))
    print('Years Since Joined: {}'.format(hank_pym.years_since_joining_method()))
    print('Notes: {}'.format(hank_pym.notes_method()))
    print('__str__: {}'.format(hank_pym))
    print('__repr__: {}'.format(hank_pym.__repr__()))


'''Main function'''

if __name__ == '__main__':
    main()
