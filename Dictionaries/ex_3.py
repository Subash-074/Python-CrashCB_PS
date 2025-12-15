"""Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person."""

people={
    'sagar':  {'first':'sagar',
               'last': 'bhandari',
                'fav_music':'jancheu_rah_maili',
                  'girlfriend':'akriti'},

      'subash':{'first':'subash',
                'last':'sapkota',
                'fav_music':'classic',
                'girlfriend':'not avaibale'
                
                
                }
       }

print('Three information of Sagar and Subash: ')

for name,  info in people.items():
      print(f"\n{name.title()}")
      for first, last in info.items():
            print(f"{first.title()}:{last.title()}")
