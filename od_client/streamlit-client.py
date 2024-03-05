'''
Streamlit client app that uploads jpg file to API and
outputs JSON response.

Requirements:
pip3 install streamlit (in virtual environment)

To run:
streamlit run streamlit-client.py 
'''

import streamlit as st
import requests


base_URI = 'http://VM_PUBLIC_IP:8080/'
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read file as bytes:
    bytes_data = uploaded_file.getvalue()

    filename = 'temp.jpg'
    with open('temp.jpg', 'wb') as f_out:
        f_out.write(bytes_data)

    files = {'uploaded_file': open(filename, 'rb')}

    headers = {'Content-Type': 'multipart-form-data',
                'accept': 'application/json'}

    r = requests.post(base_URI + 'detect/', data=headers, files=files)
    st.write(r.text)

        

 
