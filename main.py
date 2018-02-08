import requests
import pprint
import sys

api_key = "AIzaSyCvwOFiIK3mt9MdD8gwlGtLmwJiKo-bZPg"

def get_place_data(api_key, params):
  
  r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + 
  params['query'] + '+in+' + params['location'] + 
  '&key=' + api_key)

  return r.json()['results']

def get_attr_list(places_data):

  attr_list = [attr for attr in places_data[0].keys()]
  # Second ret is an example
  return (attr_list, places_data[0])

def places_list_attrs(places_data, attr):

  attr_data = [place[attr] for place in places_data]
  return attr_data

def get_usr_choice(places_data):
  print('Enter [L] for a list of place attributes, [E] for an example of a place, [A] to enter an attribute to look up over all results, [R] for raw data of all results, or [Q] to quit')
  choice = input('>> ')
  if choice is 'L':
    pprint.pprint(get_attr_list(places_data)[0])
    get_usr_choice(places_data)
  elif choice is 'A':
    print('Please enter an attribute to return for all places...')
    attr = input('>> ')
    attr_list = get_attr_list(places_data)
    if attr in attr_list[0]:
      pprint.pprint(places_list_attrs(places_data, attr))
    get_usr_choice(places_data)
  elif choice is 'E':
    pprint.pprint(get_attr_list(places_data)[1])
    get_usr_choice(places_data)
  elif choice is 'R':
    pprint.pprint(places_data)
    get_usr_choice(places_data)
  elif choice is 'Q':
    print('Thanks for using!')
    sys.exit()
  else:
    print('Invalid choice, please try again.')
    get_usr_choice(places_data)

def main():

  params = {}

  print('Please enter a place to search for. (e.g McDonalds, Longos, library)')
  params['query'] = input('>> ')
  print('Please enter a location to search in. (e.g Toronto, New York)')
  params['location'] = input('>> ')
  print('\n')

  places_data = get_place_data(api_key, params)
  get_usr_choice(places_data)
  
if __name__ == '__main__':
  a = main()
