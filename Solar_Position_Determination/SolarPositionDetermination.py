from pvlib import solarposition
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CHANGE THE FOLLOWING PARAMETERS TO GET DIFFERENT RESULTS
# Timezone - Singapore's timezone taken from online tz database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
timezone = 'Asia/Singapore'
# Latitude and Longitude
lat, lon = 1.4, 103.8
# Datetime Range
startdate = '2020-01-01 00:00:00'
enddate = '2021-01-01'

# Finding solar position for year 2020, in an hourly frequency. Date range can be changed if need be.
times = pd.date_range(startdate, enddate, closed='left', freq='H', tz=timezone)

# Use inbuilt solarposition function to derive a dataframe with information about solar position, such as zenith, elevation, azimuth, and equation of time.
solpos = solarposition.get_solarposition(times, lat, lon)

# Remove nighttime timings as they don't affect us. To do this, we remove values from solar position dataframe where the sun's elevation is below 0 i.e. Sun is below the horizon
solpos = solpos.loc[solpos['apparent_elevation'] > 0, :]

# The following lines are written so that we only calculate and retain the solar positions of the sun between 12 pm to 2 pm i.e. the time period around solar noon.
# Removing/commenting out the following 2 lines will show the whole range of solar positions while the sun is above the horizon.
solpos = solpos.loc[solpos.index.hour > 11, :]
solpos = solpos.loc[solpos.index.hour < 15, :]

# Given that we're trying to plot the position of the sun in the sky, a polar projection is the most appropriate graphical representation.
ax = plt.subplot(1, 1, 1, projection='polar')

# Plot the analemma loops by using a scatter diagram for each point of the year, and a colourbar to represent the distance of the plotted date from the start of the year
points = ax.scatter(np.radians(solpos.azimuth), solpos.apparent_zenith, s=2, label=None, c=solpos.index.dayofyear)
ax.figure.colorbar(points)

# For each hour in the solar position dataframe, get the azimuth and zenith positions. Then prepare to plot them for each hour's analemma loop.
for hour in np.unique(solpos.index.hour):
    subset = solpos.loc[solpos.index.hour == hour, :]
    r = subset.apparent_zenith
    pos = solpos.loc[r.idxmin(), :]
    ax.text(np.radians(pos['azimuth']), pos['apparent_zenith'], str(hour))

# Now that the hours are saved, highlight the key dates you want to show. For our case, because we're presenting this (originally) near Septermber 21, I've included that date.
for date in pd.to_datetime(['2020-06-21', '2020-09-21', '2020-12-21']):
    times = pd.date_range(date, date+pd.Timedelta('24h'), freq='5min', tz=timezone)
    solpos = solarposition.get_solarposition(times, lat, lon)
    solpos = solpos.loc[solpos['apparent_elevation'] > 0, :]
    label = date.strftime('%Y-%m-%d')
    ax.plot(np.radians(solpos.azimuth), solpos.apparent_zenith, label=label)

# Add the legend of the dates
ax.figure.legend(loc='upper left')

# Orientate the polar diagram such that North is on top.
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rmax(90)

plt.show()