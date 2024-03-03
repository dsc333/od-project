'''
API method can be accessed using curl:

curl -X 'POST' \
  'http://VM_EXTERNAL_IP:8080/detect/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@IMAGE_FILE.jpg;type=image/jpeg'


Google sample test code for vision API:
https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/vision/snippets/detect/detect.py

GCP requirement:
Before running, go to the Google Vision API menu in the GCP console
and enable the API

Python requirements (create a Python virtual environment):
google-cloud-vision==3.4.2, fastapi, uvicorn, python-multipart
'''

from fastapi import FastAPI, File, UploadFile
from google.cloud import vision

app = FastAPI()

@app.post('/detect/')
async def object_detect(uploaded_file: UploadFile):
    path = f"img/{uploaded_file.filename}"
    response = {}
    
    content = None
    with open(path, "wb") as out_file:
        content = uploaded_file.file.read()
        out_file.write(content)

    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)

    # Object detection
    objects = client.object_localization(image=image).localized_object_annotations
    print(f"Number of objects found: {len(objects)}")
    response['objects'] = {}
    for object_ in objects:
        response['objects'][object_.name] = f"{object_.score:0.2f}" 
        print(f"{object_.name} (confidence: {object_.score:0.2f})")

    # Text detection
    text_detected = client.text_detection(image=image)
    texts = text_detected.text_annotations

    # Detected text copied to a list that's keyed by 'texts' in
    # response dictionary 
    texts_list = []
    for text in texts:
        texts_list.append(text.description)
        print(f'"{text.description}"')
    response['texts'] = texts_list
    
    return response
