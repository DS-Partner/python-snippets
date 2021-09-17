# Look for a dictionary key

my_dict = {"name": "DS-Partner", "age": 1}

my_dict["last_name"] # -> KeyError: 'last_name'

my_dict.get("last_name") # -> None
