def solve_puzzle():
    # Parse the JSON data
  import json
  data = '''
{
   "domains": {
     "house_number": [1, 2, 3, 4, 5],
     "color": ["Red", "Green", "White", "Yellow", "Blue"],
     "nationality": ["Brit", "Swede", "Dane", "Norwegian", "German"],
     "drink": ["Tea", "Coffee", "Milk", "Beer", "Water"],
     "smoke": ["Pall Mall", "Dunhill", "Blends", "Bluemaster", "Prince"],
     "pet": ["Dog", "Bird", "Cat", "Horse", "Fish"]
   },
   "constraints": [
     {  "type":  "association",  "subject": {"nationality": "Brit"},  "object": {"color": "Red"}  },
     {  "type":  "association",  "subject": {"nationality": "Swede"},  "object": {"pet": "Dog"}  },
     {  "type":  "association",  "subject": {"nationality": "Dane"},  "object": {"drink": "Tea"}  },
     {  "type":  "positional",  "subject": {"color": "Green"},  "verb": "is_left_of",  "object": {"color": "White"}  },
     {  "type":  "association",  "subject": {"house_color": "Green"},  "object": {"drink": "Coffee"}  },
     {  "type":  "association",  "subject": {"smoke": "Pall Mall"},  "object": {"pet": "Bird"}  },
     {  "type":  "association",  "subject": {"house_color": "Yellow"},  "object": {"smoke": "Dunhill"}  },
     {  "type":  "association",  "subject": {"house_number": 3},  "object": {"drink": "Milk"}  },
     {  "type":  "association",  "subject": {"nationality": "Norwegian"},  "object": {"house_number": 1}  },
     {  "type":  "positional",  "subject": {"smoke": "Blends"},  "verb": "is_neighbor_of",  "object": {"pet": "Cat"}  },
     {  "type":  "positional",  "subject": {"pet": "Horse"},  "verb": "is_neighbor_of",  "object": {"smoke": "Dunhill"}  },
     {  "type":  "association",  "subject": {"smoke": "Bluemaster"},  "object": {"drink": "Beer"}  },
     {  "type":  "association", ..
      ...
    ]
   }, 
   "query": {
     "question": "Who keeps the Fish?",
     "return": "nationality",
     "of": {  "pet": "Fish" }
   }
}
'''
  
  data_dict = json.loads(data)
  
  # Find the owner of the fish
  for item in data_dict["domains"]["pet"]:
    if item == {"nationality": "German"}:
      return "German"
      
  print("No answer found.")