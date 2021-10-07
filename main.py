import streamlit as st
from PIL import Image
import requests
import json
from PIL import ImageDraw
import io

st.title('My second App.')
st.title('顔認識アプリ')
subscription_key='2496658c4e074de7b826384d1a2fa904'
assert subscription_key
face_api_url='https://20211006fumi.cognitiveservices.azure.com/face/v1.0/detect'
uploaded_file=st.file_uploader("Choose an image ... ",type='jpg')
if uploaded_file is not None:
    img=Image.open(uploaded_file)
#    img=Image.open('FF.jpg')
#with open('FF.jpg','rb') as f:
#    binary_img=f.read()
    with io.BytesIO() as output:
        img.save(output,format="JPEG")
        binary_img=output.getvalue() #get binary code
            
    headers={
        'Content-Type':'application/octet-stream',
        'Ocp-Apim-Subscription-Key':subscription_key
    }
    params={
        'returnFaceId':'true',
        'returnFaceAttributes':'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    res=requests.post(face_api_url,params=params,headers=headers,data=binary_img)
    results=res.json()
    result=results[0]
    for result in results:
        rect=result['faceRectangle']
        draw=ImageDraw.Draw(img)
        draw.rectangle([(rect['left'],rect['top']),(rect['left']+rect['width'],rect['top']+rect['height'])],fill=None,outline='red',width=5)
    st.image(img,caption='Uploaded Image.',use_column_width=True)

