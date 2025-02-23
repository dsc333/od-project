# Object Detection
## DSC 333 - Cloud Services for Data Science

This repo includes code for a server and a test client.  You'll need to clone it 
to both your server (VM on GCP) and client (RPI or Local computer).  On the server 
side, you will just run the code in od-api, and on the client od-client.  

### Server side (od-api):
Defines an API (single post method /detect/) that uses Google Vision API 
to detect objects and text contained in a jpg file uploaded from a client. 
This is intended to run on a VM on GCP.  No API key required (internal to GCP). 
See comments in od-api/main.py for installation requirements and instructions
for accessing using a CURL command instead of the Python client included 
in this repo. 

To run: uvicorn main:app --host=0.0.0.0 --port=8080 --reload

### Client side (od-client):
A Python test program intended to run on an RPI that captures an image and
sends it to the API for object/text detection.  You may supply a filename (.jpg)
on the command line.  
