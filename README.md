# Object Detection API

This repo includes code for a server and a test client:

Server side (od-api):
Define an API (single post method /classify/) that uses Google Vision API 
to detect objects and text contained in a jpg file uploaded from a client.  

Client side (od-client):
A client test program intended to run on an RPI that captures an image and
sends it to the API for object/text detection.  You may supply a filename (.jpg)
on the command line.  
