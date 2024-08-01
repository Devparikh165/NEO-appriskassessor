import joblib
import streamlit as st
import pickle
import pandas as pd
import numpy as np

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]  > .main {{
background-image: url("https://content.api.news/v3/images/bin/7e24714a1f449f21607db66357b2c60a");
background-size: 100%;
background-position: top left;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right:2rem;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("neo.jpg");
background-position: center;
}}
</style>
"""

# Correct usage of raw string literal
neo_dict = joblib.load(open('prediction.pkl','rb'))

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("NEO Risk Assessor")

am = st.text_input("absolute_magnitude")
edmin = st.text_input("estimated_diameter_min")
edmax = st.text_input("estimated_diameter_max")
rv = st.text_input("relative_velocity")
md = st.text_input("miss_distance")

st.write('Prediction:')
if st.button("Predict") == 1:
    st.write('This Object is Probably affect to Earth')
else:
    st.write('This Object is not Probably affect to Earth')

