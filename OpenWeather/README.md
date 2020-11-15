# Purpose

In order to run this program, you will need an OpenWeather API key. If you do not have one or have not been supplied one, please register for it [here](https://home.openweathermap.org/api_keys "OpenWeather API Key").

Following that, input your API key under the ''APIKey' parameter on line 10.

Then you can run `python .\OpenWeatherAPI.py ` or `python .\OpenWeather\OpenWeatherAPI.py` depending on your set up.

The purpose of this program is to place an API call to a weather service and use the returned data to determine if the reflectors should be extended or not.

The code that carries out the main function is short because it is a proof of concept. If we were to really implement this feature, we would need to add in code to enable communication between a server (hosting this program) and the arduino micro-controller that manages the movement of the reflectors. Additional code would also have to be added to create an effective model to determine whether the reflectors should extend under ambiguous weather conditions.

## Returned Response
The response that is returned from OpenWeather contains a number of fields and values. One example of a returned response can be seen in the [accompanying JSON file](https://github.com/rayarka/EG3301R_Data_and_Programs/blob/main/OpenWeather/60Min_Forecast_at_20201115-145723.json)

The returned response also sends minute-by-minute precipitation forecasts in the coming hour. Those forecasts are plotted out for visualisation purposes. An example of one such plot is shown here:

<img src="https://user-images.githubusercontent.com/25000887/99193236-b0466f00-27b2-11eb-8f19-f58b5cacd34d.png" alt="drawing" width="500"/>

## Additional Functions
For the sake of the user's visualisation purposes, a pyplot graph of the precipitation forecast over the next 60 minutes is shown.
For potential machine learning or data analysis purposes, all API calls made are stored in the OpenWeather folder itself. Change the directory within code if needed.
