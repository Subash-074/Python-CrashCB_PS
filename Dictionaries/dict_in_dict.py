#A dictionary in a Dictionary 
""" if you have several users for a website, each  with a unique username, you can use the username as the keys in dictionary.
remember ----- username-unique---key 
user ------general ------value """

users= {
      'aeinstein': {'first':'albert',
                    'last':'einstein',
                    'location':'princeton',},
      'mcurie':{
            'first':'marie',
            'last':'curie',
            'location':'paris', 
      },

}


for username, user_info in users.items():
     
      print(f"\nUsername: {username}")
      
      full_name=f"{user_info['first']} {user_info['last']}"

      location=user_info['location']

      print(f"\t Full name: {full_name.title()}")

      print(f"\tLocation:{location.title()}")