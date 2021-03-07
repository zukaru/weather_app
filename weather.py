import requests, json;

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#Get city name to search for
query = input(bcolors.OKGREEN + 'Enter a city to get its weather. Psst.... try bigger, well known cities like New York or London.\n\n' + bcolors.ENDC)
req = requests.get('https://www.metaweather.com/api/location/search/?query={}'.format(query)).json()


city_unvalidated = True

while city_unvalidated:
    try:
        woeid = req[0]['woeid']
        city_unvalidated = False
        break
    except:
       query = input(bcolors.FAIL + '\'{}\' was not recognized. Maybe it\'s too small or fictional. Try entering a bigger non-fictional city like New York or London. \n\n'.format(query) + bcolors.ENDC)
       req = requests.get('https://www.metaweather.com/api/location/search/?query={}'.format(query)).json()


weather_res = requests.get('https://www.metaweather.com/api/location/{}'.format(woeid)).json()

current_temp = (weather_res['consolidated_weather'][0]['the_temp'] * 1.80 + 32)
weather_state = weather_res['consolidated_weather'][0]['weather_state_name']


print(bcolors.OKCYAN + str(int(current_temp)) + '°F\n' + bcolors.ENDC + weather_state)
