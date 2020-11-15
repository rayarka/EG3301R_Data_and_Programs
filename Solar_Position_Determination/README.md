# Purpose of this program
This program will create a diagram showing the sun's position in the sky through the year. The sun's positions, especially the extremes, will help us determine the angles our reflectors should be at in order to accomodate for the extremes sun positions to the North and South.

***The findings are discussed in the report.***

This function was created thanks to the pvlib library. Either install the requirements.txt file or install the pvlib and matplotlib libraries independently.

To run from this directory, use the terminal to run python `.\Solar_Position_Determination\SolarPositionDetermination.py` or `python .\SolarPositionDetermination.py` depending on your set up. This will generate a solar position diagram.

If you wish to change parameters (`latitude`, `longitude`, `timezone`, `start date` or `end date`), they have to be changed in code. The varibles which may be of interest to change have been placed towards the top of the code. Plot manipulation has to be done in the code itself.

[Solarposition for all sunhours, annual.png](https://github.com/rayarka/EG3301R_Data_and_Programs/blob/main/Solar_Position_Determination/Solarposition%20for%20all%20sunhours%2C%20annual.png) and [Solarposition between 12 PM to 2PM, annual.png](
https://github.com/rayarka/EG3301R_Data_and_Programs/blob/main/Solar_Position_Determination/Solarposition%20between%2012%20PM%20to%202PM%2C%20annual.png) show the solar position diagrams through the year for all sunhours (when the sun is above the horizon) and more specifically between 12 PM to 2 PM respectively.
