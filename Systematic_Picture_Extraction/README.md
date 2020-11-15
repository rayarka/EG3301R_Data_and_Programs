# A Helper Program to Extract Images with Required Data Systematically at User-Defined Intervals

Take a video like this:

<img src="https://user-images.githubusercontent.com/25000887/99192575-7c694a80-27ae-11eb-8426-8ec4948930ef.gif" alt="drawing" width="500"/>

And extract out all the images in a systematic way.

<img src="https://user-images.githubusercontent.com/25000887/99192622-afabd980-27ae-11eb-920d-a64d42c9e7af.png" alt="drawing" width="800"/>


**Having an automatic data logger for whatever you're measuring is likely way more useful and efficient. However, in case you're just a poor student :( this may make data collection a bit less painful**

Libraries needed:
*Pillow `pip install Pillow`*
*MoviePy `pip install moviepy`*

## Typical Current Readings Data Collection

During our experimentation and testing, we had to record the *'Voltage'* and *'Current'* produced by the solar panel in order to determine the eventual power output. For the 'Voltage' readings, they were recorded automatically at 1 second intervals by a Hioki Data Logger. The current, however, could only be recorded manually as we only had access to a standard multimeter.

In order to record *'Current'* readings, we attempted to note down the reading on the Multimeter every 15 seconds. 

There were certain issues with that approach:
1. Due to human reaction time and human error, we were likely not taking note of the time at exactly 15 seconds. In all likelihood, we were probably noting the time every 15 ± 5 seconds. However, we were still noting the time down as being at 15 seconds intervals due to the lack of proper recording equipment. Hence, the timing error could have compounded.
2.  Carrying out such a manual recording process over 30 minutes to 1 hour was highly laborious and tasking, due to the amount of attention required. Yet, it was prone to human error (as mentioned above).
3. In certain conditions, the solar irradiance levels change rapidly, resulting in the *'Current'* reading changing rapidly too. If this change coincides with the 15-second mark at which we're supposed to record data, it is hard to choose a number to record. If we wait for the reading to stabilize, the recording of data would no longer be systematic.
4. Lastly, transferring the data from the notepad (where it was manually recorded) to the computer is also somewhat time-consuming.

The above sources of error could be solved if we could automatically collect the data. Given that we did not have a *'Current'* data logger, I thought up a simple solution to use our existing resources to solve problems 1,2 and 3 above. 

## New *'Current'* Readings Data Collection

The steps are as follows and can be used by future batches of EG3301R students to simply extract images of the data they were intending to record.
1. Set up you Camera Phone such that it is facing the screen of your Multimeter (as shown below).
2. Adjust the exposure settings (if needed) and start the video function when you're ready to begin recording your data.
3. Once the testing is done, turn off the video recording.
With this approach (over a notetaking approach), you would still have to manually go through the video and pause every 15 seconds to note down the Multimeter reading. However, with this program you don't have to.
4. Download the required modules via `pip install -r requirements.txt`
5. Run `python .\SystematicPictureExtration.py` or `python .\Systematic_Picture_Extraction\SystematicPictureExtration.py` depending on your set up.
6. When prompted to "Enter your desired interval in seconds", enter a positive integer indicating how many seconds you want between two data points (equivalent to k-value).
7. Use the graphical user interface to select your video.
8. The program will run and output a folder in the same location as your video. If a folder with the intended name 'DATA_SEPARATED_BY_X_seconds' exists, the contents inside with filenames similar to the output filenames will be overwritten. If that original folder is important to you, please change it's name to something else.
9. Once complete, you have images of every 'X' seconds, which you must then manually input into your excel sheet (the automation of this part can be pursued, as explained below)

Assume you have a 60 minute video of your Multimeter screen during the experiment. Entering '60' in Step 6 means that you wish to get the reading that was on the screen every 60 seconds. That will result in 60 readings (for one hour) i.e. 60 extracted images.

### Camera and Multimeter Setup

<img src="https://user-images.githubusercontent.com/25000887/99192750-9d7e6b00-27af-11eb-94b8-f6d9096b1d52.png" alt="drawing" width="500"/>

## Potential Improvements
There are several improvements that can be made to this program to make it even easier to use. These can be implemented fairly easily if needed in future projects.

### Timestamping the pictures
In order to facilitate more accurate data entry and collection, timestamping the pictures by how many seconds has passed or by the time it was taken is easy to implement. However, it requires the user to install the ImageMagick binary to their computer, which may be an annoyance  to do. Since the output filename is already programmed to show how many milliseconds have passed, I didn't implement this extra feature.

Binaries needed:
ImageMagick

### Cropping extracted images
Assuming that the video was taken by placing the phone and multimeter in stationary positions, the pictures extracted can be cropped to only include the screen. This would make the data entry process easier as there would be less distractions or zooming required. Moreover, this would also allow the images to be pre-processed for computer vision applications. However, I did not implement this because it was unnecessary for me - the video my phone took already had the screen well-positioned.

### Using OpenCV to convert numbers in pictures to computer-readable numbers
The only remaining manual step in this process is that we still have to manually transfer the data from the images to an excel sheet. However, using a computer vision program, we can easily extract the digits out of the images. A detailed tutorial of doing exactly this is shown here https://www.pyimagesearch.com/2017/02/13/recognizing-digits-with-opencv-and-python/. Given that we were dealing with a relatively small amount of data, this felt unnecessary, and so I didn't implement it. However, it could be implemented if someone wishes to.

Libraries needed:
*OpenCV-Python*, 
*imutils*
