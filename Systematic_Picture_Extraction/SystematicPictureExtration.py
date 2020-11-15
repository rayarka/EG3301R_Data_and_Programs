# from moviepy.editor import *
import os
from tkinter.filedialog import askopenfilename
# from PIL import Image

print("\n\n")
k = input("Enter your desired interval in seconds [NOTE: Enter a Positive Integer. Numbers which are negative and/or contain decimals will be converted to a rounded-down positive number. 0 will be rounded up to 1] : ")
k = int(abs(float(k)))
k = 1 if k < 1 else k

#parameters
source_video_path = askopenfilename(title = "Select The Background Video File", filetypes = (("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi"), ("png", "*.png")))
clip = VideoFileClip(source_video_path, audio=False, fps_source="fps")
output_folder = os.path.join(os.path.split(source_video_path)[0], f'DATA_SEPARATED_BY_{k}_seconds')
os.makedirs(output_folder, exist_ok=True)

fps = round(clip.reader.fps)
print(fps)
for i, frame in enumerate(clip.iter_frames()):   #iterating thru each frame
    if i%(k*fps) == 0:  #every 'fps' number of frames == every second.
        # print(i/fps)
        current_ms = int((i/fps)*1000)  #for filenaming purposes. The reason we convert it to ms is that if we get frames at every 1/2 second, then our name will be "500" or "2500", rather than "1.5" or "2.5". If we end up getting 1.5, then it will be confusing due to the fil extension part.
        new_img_filepath = os.path.join(output_folder, f'{current_ms}ms.jpg')
        new_img = Image.fromarray(frame) #create a picture from frame data
        new_img.save(new_img_filepath)