# Welcome-note
The repo contains python code for Real-Time Video Display with Greetings and Date/Time Overlay is a Python code that utilizes the Pygame library to create an engaging multimedia application.
## **Description and Instruction**

### Description:
Real-Time Video Display with Greetings and Date/Time Overlay

This Python code uses the Pygame library to create a real-time video display window with various elements. The program loads a video file, rotates it 90 degrees counterclockwise, and centers it on the window. It also displays a custom greeting message in the center of the window.

In addition, the code overlays the current date and time in the top-right corner of the window. The date is displayed in the "dd-mm-yyyy" format, and the time is displayed in the 12-hour format with AM/PM indication.

The window has a curved border drawn with a transparent surface, giving it an elegant look. The code also plays an audio file after a 1-second delay.

This code can be used as a simple welcome screen or as a starting point for more advanced multimedia applications. It demonstrates the usage of Pygame, video processing with OpenCV, text rendering, and audio playback.

Dependencies: Pygame, OpenCV (cv2)
```
**Note: Add a video to the directory and name it vid**
```
Usage:
1. Install the required dependencies using pip:
   - pygame:
   ```
   pip install pygame
   ```
   - opencv-python: 
   ```
   pip install opencv-python
   ```
   
2. Modify the file paths in the code to specify your custom video, font, and audio files.

3. Run the script and enjoy the real-time video display with greetings and date/time overlay.

Note: Make sure to have the necessary video, font, and audio files in the specified paths for the program to work correctly.

### Instruction:
Move to the directory
```
cd Welcome-note
```
Run the code
```
python hello.py
```
## Start the program at startup
1. Make a shortcut of the hello.py program in the same directory
2. Press *Windows key + R*
3. Paste the below line and press enter
   ```
   shell:startup
   ```
4. Copy the shortcut created to the newly opened window

**Now the program will start at startup**

## Changes you can make
1. You can change the font of your requirement  which you can download from the internet. There are two fonts required one for message and another for time and date. In this repo the font name are **font.otf** and **font1.otf**
2. You can change the audio of your requirement. In this repo the audio file is **hello_yajnesh.mp3**.
3. You can have your own video for the background. In this repo the video the file is not uploaded. Name the video file as **vid**.
4. You can change the volume of the audio in the line:
```
sound.set_volume(0.1)
```
5. You can chnage the welocome text in the line:
```
pygame.display.set_caption("Hello Yajnesh")
```
