'''
Sample app using picam3
https://www.tomshardware.com/how-to/raspberry-pi-camera-module-3-python-picamera-2

Sample app using picam2
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/0

NOTES:

To run ON RPI:
Do NOT create a virtual environment to run the client as it interferes with the 
camera packages.  Just install requests: 
    pip3 install requests

To run on local computer:
Create a virtual environment and install requests:
    pip3 install requests
'''
from picamera2 import Picamera2
import requests
import sys
from datetime import datetime

# Replace with the external IP address of your VM where FastAPI is running
base_URI = 'http://VM_EXTERNAL_IP:8080/'

# If filename not supplied as command line argument, capture still image 
# from camera
if len(sys.argv) < 2:
    filename = f'capture{datetime.now()}.jpg'
    picam2 = Picamera2()
    picam2.start_and_capture_files(filename)
    picam2.stop()
else:
    filename = sys.argv[1]

# uploaded_file is the field expected on the FastAPI side
files = {'uploaded_file': open(filename, 'rb')}

headers = {'Content-Type': 'multipart-form-data', 
            'accept': 'application/json'}

# Detect objects and text in the captured image
r = requests.post(base_URI + 'detect/', data=headers, files = files)
print(r.text)

