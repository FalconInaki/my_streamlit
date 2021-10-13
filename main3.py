import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time


st.title('Streamlit for neginners')
st.write('Progress bar')
'start !!'
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done'
left_column,right_column=st.columns(2)
button=left_column.button('Put strings in right column')
if button:
    right_column.write('Here is right column')

expander=st.expander('Question?')
expander.write('detail')

#condition=st.slider('Your condition ',0,100,50)
#if st.checkbox('Show Image'):
#    img=Image.open('FF.jpg')
#    st.image(img,caption='My Friend',use_column_width=True)
#text=st.text_input('Please tell me your hobby')
#'Your favorite hobby is ',text,'.'
#'your condition is ',condition,'.'
