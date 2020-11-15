import requests
import json
from matplotlib import pyplot as plt
from datetime import datetime

url = 'https://api.openweathermap.org/data/2.5/onecall'

print("\nRemember to write a VALID API KEY below. The appid parameter will still be accepted as input but no results will be returned unless a VALID API KEY is used", end = "\n\n")

APIKey = None #OpenWeather Generated API Key (https://home.openweathermap.org/api_keys)

if APIKey == None:
    print ("A VALID API KEY HAS NOT BEEN ENTERED. Either register for a new key at https://home.openweathermap.org/api_keys or use the one that has been supplied to you.\n")
    exit(0)

params = dict(
    appid = APIKey,     #OpenWeather Generated API Key (https://home.openweathermap.org/api_keys)
    lat = 1.4544,         #Micron Latitude
    lon = 103.794,        #Micron Longitude
    exclude = 'hourly, daily, alerts'     #Exclusions in response
)

r1 = requests.get(url = url, params= params)

def extendReflectors(APIrequest):
    """This function is extremely simple and minimal at this moment - it looks at the current weather description and decides whether to extend the reflectors or not. However, should the API apporach be pursued, a large amount of climate modelling, statistical probability, and other parameters can be programmed in order to determine if the reflectors should bother extending. We can also see other current data, like wind speed and humidity, to make more advanced calculations regarding the reflectors.

    If it is raining, for example, and the forecast suggests that it will keep raining for the next hour, we can choose not to extend at all. If it claims that rain will stop in 20 minutes, we can schedule another API call in 20 minutes to check. Moreover, we can check with past data to see how often the forecast has been correct and even use machine learning to determine the best course of action.

    The fuction will ultimately return a 'True' (extend) or 'False' (don't extend) call after doing the relevant calculations within the function itself.
    """
    current_weather = r1.json()['current']['weather'][0]['main']
    acceptable_weather = ['Clear', 'Clouds', 'Smoke', 'Haze', 'Dust'] #Can be adjusted according to need - ist of weather conditions codes available at https://openweathermap.org/weather-conditions 
    if current_weather in acceptable_weather:    
        return True
    else:
        return False

print("Should the reflectors be extended? " + str(extendReflectors(r1)))

# %% FOR USER'S VISUALISATION BENEFIT

print()
print('Current Cloud Level: ' + str(r1.json()['current']['clouds']) + '%\n')
print('Current Weather: ' + str(r1.json()['current']['weather'][0]['main']) + " --- " + str(r1.json()['current']['weather'][0]['description']) + '\n')
if str(r1.json()['current']['weather'][0]['main']).lower() == 'Rain'.lower():
    print('Rain Volume in Past 1 Hour: ' + str(r1.json()['current']['rain']['1h']) + 'mm\n')

ppt_value = []
for i in range(60):
    ppt_value.append(r1.json()['minutely'][i]['precipitation'])

plt.plot(ppt_value)
plt.ylabel('Precipitation Level /mm')
plt.xlabel('Time from now /minutes')
plt.title('Precipitation Forecast Over Next Hour\n' + str(r1.json()['current']['weather'][0]['main']) + " - " + str(r1.json()['current']['weather'][0]['description']))
plt.show()

# %% FOR POTENTIAL MACHINE LEARNING OR DATA ANALYSIS PURPOSES - Saves each API call that is made

fname = "60Min_Forecast_at_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".json"
with open(".\OpenWeather\\" + fname, 'w') as f:
    json.dump(r1.json(), f)
